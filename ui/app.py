from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot( 
    'SQLMemoryTerminal', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter', 
    logic_adapters=[ 
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
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
