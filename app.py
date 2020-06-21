from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Kim-BOT")

trainer = ListTrainer(bot)
trainer.train(['Hello?', 'Hi'])
trainer.train(['Goodmorning?', 'Goodmoring'])
trainer.train(['How can i register', 'Go to Home page'])
trainer.train(['Need to talk to customer care?', 'Call 08011100'])
trainer.train(['What is the name of the program?', 'HNG internship'])
trainer.train(['Can i learn programming?', 'Yes'])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home(): 
 return render_template("index.html") 
@app.route("/get")
def get_bot_response(): 
 userText = request.args.get('msg') 
 return str(bot.get_response(userText)) 
if __name__ == "__main__": 
 app.run()