from flask import Flask
from datetime import datetime
from bot import *
import threading

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Dragon's Blessings!</h1>
    <p>I am alive at {time}.</p>
    <p>{token}.</p>
    """.format(time=the_time)

def startFlask():
  app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    flaskThread = threading.Thread(target=startFlask)
    flaskThread.start()

    startDiscord()
