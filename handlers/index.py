from datetime import datetime
import urllib.request as urllib
import json
import os
from flask import render_template
from . import handlers

# https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files

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

@handlers.route('/')
def index():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    version = os.environ.get("HEROKU_RELEASE_VERSION")
    logs = "\n".join(fetchLogs())

    return render_template('index.html', 
        time=the_time, 
        version=version, 
        logs=logs)
