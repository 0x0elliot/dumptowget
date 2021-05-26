import requests
from flask import Flask, request
from flask_ngrok import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def hello():
    #discord_webhook_link="https://google.com"
    #data={'content':'all the shit you need. thoda bahut docs dekh le hojayga.'}
    #requests.post(discord_webhook_link, data=data)
    return "5 rupai ki pepsi elliot bhai sexy."

if __name__=="__main__":
    app.run()
