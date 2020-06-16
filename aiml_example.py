from chatterbot import ChatBot
import datetime

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'SQLMemoryTerminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.RetrievalCustom'
    ]
)

# Get a few responses from the bot

# print(bot.get_response('What time is it?'))

# print(bot.get_response('What is 7 plus 7?'))
#%%
#response = bot.get_response('What is your name?')
#print(response)

while True:
    try:
        user_input = input("User : ")
        start = datetime.datetime.now()
        bot_response = bot.get_response(user_input)

        print("Bot : {}".format(bot_response))
        print(">>> Response time: {}".format(datetime.datetime.now()-start))
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
