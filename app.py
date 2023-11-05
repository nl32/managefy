from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define a route that responds to the root URL
@app.route('/')
def home():
    return render_template('home.html', name = "Ethan")

@app.route('/dashboard')
def about():
    return render_template('dashboard.html', name = "Ethan")

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

