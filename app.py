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

@app.route('/get', methods=['GET'])
def send_message():
    url = "https://raw.githubusercontent.com/kzarre/help2/main/sol.txt"

    try:
        response = requests.get(url, timeout=10)

        return (
            response.text,
            response.status_code,
            {"Content-Type": "text/plain"}
        )

    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run()
