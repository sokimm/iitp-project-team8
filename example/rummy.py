from flask import Flask, render_template, request
from chatterbot import ChatBot
from datetime import datetime
import csv

app = Flask(__name__)

bot = ChatBot( 
    'Rummy', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter', 
    database_uri='sqlite:///rummy.db',
    logic_adapters=[ 
        'chatterbot.logic.ContextAdapter',
        'chatterbot.logic.MathematicalEvaluation', 
        'chatterbot.logic.TimeLogicAdapter', 
        'chatterbot.logic.RetrievalCustom', 
	'chatterbot.logic.ParlAI'
    ] 
) 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    f = open("log.csv", 'a')

    userText = request.args.get('msg')
    time1 = datetime.now()

    response = str(bot.get_response(userText))
    time2 = datetime.now()

    response_time = time2-time1
    writer = csv.writer(f)
    writer.writerow(("user1", userText, time1))
    writer.writerow(("chatbot8", response, time2, response_time))
 
    f.close()
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
