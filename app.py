from flask import Flask
from datetime import datetime
from bot import *
import os, threading

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    version = os.environ.get("HEROKU_RELEASE_VERSION")

    return """
    <h1>Dragon's Blessings!</h1>
    <p>I am alive at {time}.</p>
    <p>{version}</p>
    """.format(time=the_time, version=version)

def startFlask():
  port = int(os.environ.get("PORT", 8000))
  print(port)
  app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port)

if __name__ == '__main__':
    flaskThread = threading.Thread(target=startFlask)
    flaskThread.start()

    startDiscord()
