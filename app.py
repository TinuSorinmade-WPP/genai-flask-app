from flask import Flask, render_template, request
from crypto_bot import ask_question #NEED A FUNCTION IN CRYPTO BOT

app = Flask(__name__)

# set up our landing page
@app.route('/')
def index(): # left from index, right is coming form me (i,e vriable or somehting you have typed in)
	return render_template('index.html', question="Type questions here!", chatbot_response= "")

# only use this when posting data!
@app.route('/', methods=['POST'])
def index_post():
	user_question = request.form['req_question']
	chatbot_response = ask_question(user_question) 
	return render_template('index.html', question = user_question, chatbot_response= chatbot_response)