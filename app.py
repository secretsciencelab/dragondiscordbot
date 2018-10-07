from flask import Flask
from bot import *
from handlers import *
import os, threading

app = Flask(__name__)
app.register_blueprint(handlers)

def startFlask():
  port = int(os.environ.get("PORT", 8000))
  print(port)
  app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port)

if __name__ == '__main__':
    flaskThread = threading.Thread(target=startFlask)
    flaskThread.start()

    startDiscord()
