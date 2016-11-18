from flask import Flask

from models import initialize
from models import Course
from models import DATABASE

app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.route('/codigo/api/v1.0/courses', methods=['GET'])
def get_courses():
    return "Hello World."

if __name__ == '__main__':
    initialize()
    app.run(port = PORT, debug = DEBUG)