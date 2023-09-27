import requests
import os
import telebot
import time, atexit
from flask import Flask

anime_api_base_url = 'https://api.jikan.moe/v4'

def request_handler(base_uri, request_route):
  request = requests.get(base_uri + request_route).json();
  return request['data'];

app = Flask(__name__)

scheduler_chats = []

@app.route("/get_anime")
def get_anime():
  return request_handler(anime_api_base_url, 'random/anime')
