from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from authlib.integrations.flask_client import OAuth
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app=Flask(__name__)
app.secret_key='super_secret_key'

login_manager = LoginManager(app)
users={'testuser': generate_password_hash('password')}

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    return User()

oauth=OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id='29nyOv9DuGnM1jzhFPoOY5sGqDnt7wEs',
    client_secret='ykHakockj-xfLHVGJxbGjjxlaf6rMj4B4JE1SsTpTFoDGXO1Ijkss_zj0cRbAMzH',
    api_base_url='https://dev-pdkb0flcbcin5n38.us.auth0.com',
    access_token_url='https://dev-pdkb0flcbcin5n38.us.auth0.com/oauth/token',
    authorize_url='https://dev-pdkb0flcbcin5n38.us.auth0.com/authorize',
    client_kwargs={'scope': 'openid profile email'}
)

@app.route('/')
def index():
    error_message = session.pop('error', None)
    html_error = '<dive style="color: red; text-align: center; margin-bottom: 20px; margin-top: 10px;">Invalid credentials</div>' if error_message else ''

    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
    </head>
    <body>
        <form action="/login_direct" method="post">
            <label for="username">Username:</label>
            <input type="text" name="username" id="username">

            <label for="password">Password:</label>
            <input type="password" name="password" id="password">

            html_error

            <input type="submit" value="Login Directly">
            <p>OR</p>
            <a href="/login">Login via SSO</a>
        </form>
    </body>
    </html>  
    '''
@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_url='http://localhost:3000/callback')

@app.route('/callback')
def callback_handling():
    resp=auth0.authorize_access_token()
    session['jwt_payload']=resp.json()
    user=User()
    user.id=session['jwt_payload']['sub']
    login_user(user)
    return redirect('/dashboard')

@app.route('/login_direct', methods=['POST'])
def login_direct():
    if check_password_hash(users.get(request.form['username'], ''), request.form['password']):
        user=User()
        user.id=request.form['username']
        login_user(user)
        return redirect('/dashboard')
    else:
        session['error']='Invalid credentials please try again!'
        return redirect('/')

@app.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to the dashboard!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)