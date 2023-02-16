from flask import Flask, request
import requests
import os
from telegram import Bot, Update
from main import(
    start
)
# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method=='GET':
        return 'hi'
    elif request.method=='POST':
        data=request.get_json(force=True)
        
        dispatcher:Dispatcher=Dispatcher(bot,None,worker=0)
        update:Update=Update.de_json(data,bot)
        
        dispatcher.add_handler(CommandHandler('start',callback=start))
        dispatcher.add_handler(MessageHandler('start',callback=start))
        dispatcher.process_update(update)
        
        return 'hi'