from flask import Flask, request
import requests

hero = ""
princess = ""
app = Flask(__name__)


@app.route('/', methods=['GET'])
def send_code():
    msg = """@echo off
setlocal enabledelayedexpansion

:: Ask for username
set /p username=Enter username: 

:loop
set /p msg=Enter message (/ to check if recieved): 

:: If empty → GET request
if "!msg!"=="/" (
    curl "https://help-wk9i.onrender.com/get?user=%username%"
    echo.
    goto loop
)

:: Otherwise → POST request
curl -d "msg=%username% !msg!" https://help-wk9i.onrender.com/send

echo.
goto loop"""

    return msg, 200

@app.route('/send', methods=['POST'])
def receive_message():
    global hero, princess
    msg = request.form.get('msg')
    if msg:
        user, mess = msg.split(" ")[0], " ".join(msg.split(" ")[1:])
        print(f"\n[NEW MESSAGE]: {msg}")
        if user=="kzar":
            hero = mess
            # return "Message Saved", 200
        elif user=="vedika":
            princess = mess
        return f"{user} {mess} Recieved", 200
    return "No message found.", 400

@app.route('/get', methods=['GET'])
def send_message():
    global hero, princess
    
    user = request.args.get('user')

    if user=='vedika':
        print(hero)
        return hero, 200
    elif user=='kzar':
        print(princess)
        return princess, 200
    return "", 200

if __name__ == "__main__":
    app.run()
