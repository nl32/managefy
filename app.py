from flask import Flask, render_template, request, jsonify
import json
from alternatives import maker

global_dict = {}
app = Flask(__name__)

# --------------------------------------------------------------------------HOME

@app.route('/')
def home():
    return render_template('home.html', name = "Ethan")

# --------------------------------------------------------------------------LIST

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/list', methods=['POST'])
def list_post():
    item = request.form['itemName']
    price = request.form['itemPrice']
    global_dict = maker(item, price)
    print("Rout List: ")
    print(global_dict)
    with open("data.json","w",encoding="utf8") as json_file:
        json.dump(global_dict,json_file,ensure_ascii=True)
    return global_dict

# --------------------------------------------------------------------------DASHBOARD

@app.route('/dashboard')
def about():
    return render_template('dashboard.html', name = "Ethan")

# --------------------------------------------------------------------------LOGIN

@app.route('/login')
def login():
    return render_template('login.html')

# --------------------------------------------------------------------------FUTURE FINANCE

@app.route('/futurefinance')
def futurefinance():  
    with open("data.json","r",encoding="utf8") as json_file:
        global_dict = json.load(json_file)
    return render_template('futurefinance.html', data=global_dict)



if __name__ == '__main__':
    app.run(debug=True)

