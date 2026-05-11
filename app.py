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
    try:
        with open('sol.txt', 'r') as file:
            content = file.read()
        return content, 200
    except FileNotFoundError:
        return "sol.txt not found.", 404
    except Exception as e:
        return f"Error reading file: {str(e)}", 500

if __name__ == "__main__":
    app.run()
