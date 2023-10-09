import requests
import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_webhook(url=os.environ.get('SERVER_URL') + "/webhook_receiver")

def request_handler(base_uri, request_route):
  request = requests.get(base_uri + request_route).json();
  return request['data'];

app = Flask(__name__)

GDP_CHAN_TAG = "@gdp_ufrj_bot"

def command_wrapper(command, expected):
  if command == expected or command == expected + GDP_CHAN_TAG: return True
  else: return False

def private_chat_checker(chat):
  if chat["type"] == "private": return True
  else: return False

@app.route("/webhook_receiver",methods = ['POST'])
def webhook_treater():
  json_request = request.get_json()
  if "message" in json_request and "text" in json_request["message"]:
    try:
      message = json_request["message"]

      chat = message["chat"]
      chat_id = chat["id"]
      command = message["text"]
      
      OUVIDORIA_MESSAGE = "Ouvidoria da GDP\n\nTenha certeza de checar se todas as informações inseridas(ex: se você deseja mandar para o grupo de responsaveis) estão corretas.\n\nO RH será informado e acionado devido a sua demanda em breve!\n\n<b><a href=\"https://forms.gle/Eo6LPqPVcyt8BLEU9\">Link do Form</a></b>"

      if command_wrapper(command=command, expected="/gdp"):
        bot.send_message(chat_id=chat_id, text='Eu sou a GDP-chan! :D')  

        return 'Message sent!'
      elif command_wrapper(command=command, expected="/ouvidoria") and private_chat_checker(chat=chat):
        bot.send_message(chat_id=chat_id, text=OUVIDORIA_MESSAGE, parse_mode="HTML")

        return 'Message sent!'
      else:
        return 'Message Ignored'
    except:
      return 'Message Ignored'
  return 'Message Ignored'

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=int(os.environ.get('PORT', 8080)))
