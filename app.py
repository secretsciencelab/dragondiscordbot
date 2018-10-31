from flask import Flask
import bot
import handlers
import os, threading

app = Flask(__name__)
app.register_blueprint(handlers.handlers)

app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))

def startFlask():
  port = int(os.environ.get("PORT", 8000))
  print(port)
  app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port)

if __name__ == '__main__':
    flaskThread = threading.Thread(target=startFlask)
    flaskThread.start()

    bot.startDiscord()
