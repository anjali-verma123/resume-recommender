# main.py
from flask import Flask
from hr_1 import app1
from hr_2 import app2

app = Flask(__name__)

app.register_blueprint(hr_1, url_prefix='/app1')
app.register_blueprint(hr_2, url_prefix='/app2')

if __name__ == '__main__':
    app.run(port=5000)

