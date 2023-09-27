import requests
import os
from flask import Flask

anime_api_base_url = 'https://api.jikan.moe/v4'

def request_handler(base_uri, request_route):
  request = requests.get(base_uri + request_route).json();
  return request['data'];

app = Flask(__name__)

@app.route("/")
def ping():
  target = os.environ.get('TARGET', 'World')
  return 'Hello {}!\n'.format(target)

@app.route("/get_anime")
def get_anime():
  return request_handler(anime_api_base_url, '/random/anime')

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=int(os.environ.get('PORT', 8080)))
