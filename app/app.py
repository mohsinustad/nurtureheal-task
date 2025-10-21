from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return f"<h1>Hello from Dr. ViKi DevOps Pipeline!</h1><p>Time: {datetime.utcnow()} UTC</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
