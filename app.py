from flask import Flask, url_for
import bot
import logging
import handlers
import os, threading

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.register_blueprint(handlers.handlers)

def startFlask():
  port = int(os.environ.get("PORT", 8000))
  print(port)
  app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port)

if __name__ == '__main__':
    flaskThread = threading.Thread(target=startFlask)
    flaskThread.start()

    bot.startDiscord()
