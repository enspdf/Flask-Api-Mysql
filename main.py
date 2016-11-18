from flask import Flask
from flask import jsonify
from flask import g

from models import initialize
from models import Course
from models import DATABASE

app = Flask(__name__)
PORT = 8000
DEBUG = True
@app.before_request
def before_request():
    g.db = DATABASE
    g.db.connect()

@app.after_request
def after_request(request):
    g.db.close()
    return request

@app.route('/codigo/api/v1.0/courses', methods=['GET'])
def get_courses():
    courses = Course.select()
    courses = [ course.to_json() for course in courses  ]
    return jsonify(courses)

if __name__ == '__main__':
    initialize()
    app.run(port = PORT, debug = DEBUG)