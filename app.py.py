from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def receive_message():
    # Get the message from the "msg" parameter in the request
    msg = request.form.get('msg')
    if msg:
        print(f"\n[NEW MESSAGE]: {msg}")
        return "Message received!", 200
    return "No message found.", 400

if __name__ == "__main__":
    app.run()