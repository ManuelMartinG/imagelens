import flask
import json
import matplotlib.pyplot as plt

app = flask.Flask(__name__)


@app.route('/raw', methods=["POST"])
def process():
    print(dir(flask.request))
    request = flask.request
    image = request.files["media"].read()
    print(image)
    with open("results-from-post.jpg", "wb") as f:
        f.write(image)
    return json.dumps({"status": "OK"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
