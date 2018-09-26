from flask import Flask
from datetime import datetime
from bot import *
import os, threading
import urllib.request as urllib
import json

app = Flask(__name__)

def fetchLogs():
  url = 'https://papertrailapp.com/api/v1/events/search.json?limit=200'
  token = os.environ.get("PAPERTRAIL_API_TOKEN")

  req = urllib.Request(url, 
    headers={'X-Papertrail-Token': token})
  response = urllib.urlopen(req)

  jsonStr = str(response.read().decode('utf-8'))
  obj = json.loads(jsonStr)

  messages = []
  for event in obj['events']:
    row = "%s %s %s" \
      % (event['display_received_at'], 
         event['program'], 
         event['message'])
    messages.append(row)

  return messages

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    version = os.environ.get("HEROKU_RELEASE_VERSION")
    logs = "\n".join(fetchLogs())

    return """
    <h1>Dragon's Blessings!</h1>
    <p>I am alive at {time}.</p>
    <p>{version}</p>
    <p><pre>{logs}</pre></p>
    """.format(time=the_time, version=version, logs=logs)

def startFlask():
  port = int(os.environ.get("PORT", 8000))
  print(port)
  app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port)

if __name__ == '__main__':
    flaskThread = threading.Thread(target=startFlask)
    flaskThread.start()

    startDiscord()
