from flask_api import FlaskAPI, exceptions
app = FlaskAPI(__name__)

from sqs import *


if __name__ == '__main__':
    app.run(debug=True)