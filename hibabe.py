from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)

with open('./html/index.html', 'r') as index:
    defaultPage = index.read()

renderPage = Template(defaultPage)
chatText = "<h2>Welcome to the Chat!</h2>"

@app.route("/")
def hello():
    return renderPage.render(chatText=chatText)
    #defaultPage

@app.route("/sendtext", methods=['POST'])
def receiveText ():
	newChatText = request.form.get('chattext') #if key doesn't exist, returns None
	global chatText
	chatText = chatText + "<p>" + newChatText + "</p>"
	print (chatText)
	return renderPage.render(chatText=chatText)


