from flask import Flask, render_template, request, jsonify
import json
from alternatives import maker
from dotenv import load_dotenv
import os
import openai

load_dotenv()

global_dict = {}
openai.api_key = (os.environ["OPENAI_KEY"])

app = Flask(__name__)

# --------------------------------------------------------------------------HOME


@app.route('/')
def home():
    return render_template('home.html', name="Ethan")

# --------------------------------------------------------------------------LIST


@app.route('/list')
def list():
    return render_template('list.html')


@app.route('/list', methods=['POST'])
def list_post():
    item = request.form['itemName']
    price = request.form['itemPrice']
    global_dict = maker(item, price)
    arr = []
    with open("data.json", "r", encoding="utf8") as json_file:
        arr = json.load(json_file)
    arr.append(global_dict)
    print("Rout List: ")
    print(global_dict)
    with open("data.json", "w", encoding="utf8") as json_file:
        json.dump(arr, json_file, ensure_ascii=True)
    return global_dict

# --------------------------------------------------------------------------DASHBOARD


@app.route('/dashboard')
def about():
    return render_template('dashboard.html', name="Ethan")

# --------------------------------------------------------------------------LOGIN


@app.route('/login')
def login():
    return render_template('login.html')

# --------------------------------------------------------------------------FUTURE FINANCE


@app.route('/futurefinance')
def futurefinance():
    arr = []
    with open("data.json", "r", encoding="utf8") as json_file:
        arr = json.load(json_file)
    return render_template('futurefinance.html', data=arr)

# --------------------------------------------------------------------------CHATBOT FUNCTION


@app.route("/chat")
def chat():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat_post():
    msg = request.form["msg"]
    input = msg
    return chat_with_bot(input)


def chat_with_bot(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Financial Bot: {message}",
        max_tokens=100
    )
    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run(debug=True)
