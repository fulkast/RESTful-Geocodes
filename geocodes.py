import json
from flask import Flask, request


# Initialize flask app
app = Flask(__name__)


# Add a basic endpoint to test connection
@app.route('/geocodes/v1/', methods=["GET"])
def basicFunction():
    if request.method == "GET":
        return json.dumps({"status": "Connected",
                           "message": "Successfully connected to geocodes"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)