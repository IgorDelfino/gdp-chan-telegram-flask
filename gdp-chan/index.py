import requests
import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_webhook(url=os.environ.get('SERVER_URL') + "/webhook_receiver")

webhook_log = []

def request_handler(base_uri, request_route):
  request = requests.get(base_uri + request_route).json();
  return request['data'];

app = Flask(__name__)

def send_message(chat_id, text):
  bot.send_message(chat_id=chat_id, text=text);

@app.route("/webhook_receiver",methods = ['POST'])
def webhook_treater():
  json_request = request.get_json()
  if "message" in json_request and "text" in json_request["message"]:
    try:
      message = json_request["message"]
      chat = message["chat"]
      chat_id = chat["id"]
      command = message["text"]

      if command == '/gdp':
        webhook_log.append(json_request)
        send_message(chat_id=chat_id, text='Eu sou a GDP-chan! :D')  

        return 'Message sent!'
      else:
        print('comando: ' + command)
        return 'Command not valid!'
      
    except:
      print(json_request)
      return 'Could not treat message!'
  return 'Unsuported message'


@app.route("/webhook_logger")
def webhook_logger():
  return webhook_log

   

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=int(os.environ.get('PORT', 8080)))
