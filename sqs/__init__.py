from flask_api import FlaskAPI, exceptions
app = FlaskAPI(__name__)


@app.route('/', methods=['GET'])
def simple_q():
    return {'q': 'q'}