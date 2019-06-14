from flask import Flask, redirect, request, url_for
from jinja2 import Template
import time, schedule

app = Flask(__name__)

with open('./static/html/index.html', 'r') as index:
    defaultPage = index.read()

renderPage = Template(defaultPage)
chatText, chatTextBuffer = " ",""
@app.route("/", methods=['GET'])
def hello():
    return renderPage.render(chatText=chatText)

@app.route("/sendmessage", methods=['POST'])
def receiveText ():
	global chatTextBuffer
	newTime = time.strftime("%A, %d. %B %Y %I:%M:%S %p")
	newUser = request.form.get('username')
	newMessage = request.form.get('message') #if key doesn't exist, returns None
	newChatText = "<div class='chatMessage'><span class='chatDate'>" + str(newTime) + "</span> <span class=chatText>" + newUser + ": " + newMessage + "</span></div>"
	chatTextBuffer = chatTextBuffer + newChatText
	print ("New message added to chatTextBuffer:\n ", newChatText)
	updateChatText()
	return redirect(url_for('hello'))

def updateChatWindow():
	return renderPage.render(chatText=chatText)

def updateChatText ():
	global chatText, chatTextBuffer
	chatText = chatText + chatTextBuffer
	chatTextBuffer = ""
	print ("Updated chatText")

schedule.every().second.do(updateChatWindow)
schedule.run_pending()
