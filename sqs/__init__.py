from sqs.sqs_app import app


@app.route('/', methods=['GET'])
def simple_q():
    return {'q': 'q'}