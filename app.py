from flask import Flask , jsonify , request
app = Flask(__name__)


@app.route('/v1/process' , methods=["POST"])
def process():
    """this is call back from kavenegar. will get sender and message and will check if it is valid , then answers back"""

    data = request.form
    sender = data[}from]
    message = data["message"]
    print(f"received (message) from (sender)")
    ret = {"message" : "processed"}
    return jsonify(ret) , 200
def send_sms():
    pass

def check_serial():
    pass

if __name__ == "__main__":
    app.run("0.0.0.0" , 5000 , debug=True)

