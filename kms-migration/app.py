from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get-key')
def get_key():  # put application's code here
    return os.getenv("AES_KEY")


if __name__ == '__main__':
    app.run()
