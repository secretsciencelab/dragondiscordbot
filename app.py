from flask import Flask
from datetime import datetime
from bot import *

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    token = os.environ["DISCORD_TOKEN"]

    return """
    <h1>Dragon's Blessings!</h1>
    <p>I am alive at {time}.</p>
    <p>{token}.</p>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
