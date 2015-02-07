import flask
from flask import request, render_template, redirect
import uuid
import os
import json
import pickle
import time

import localConfig



# Test Flask initialization with main module.
app = flask.Flask('__main__')
app.debug = True


@app.route('/',methods=['GET','POST'])
def index():

	# get all messages in cargo
	messages = [ (msg,pickle.load(open('cargo/'+msg,'r')).encode('utf-8')) for msg in os.walk('cargo').next()[2] ]
	messages.sort(reverse=True)
	print messages

	return render_template("main.html",messages=messages)


@app.route('/store',methods=["POST"])
def store():

	msg = request.form['msg']
	print msg

	filename = "cargo/"+str(int(time.time()))+".msg"
	fhand = open(filename,'w')
	pickle.dump(msg,fhand)
	fhand.close()

	return redirect('/')
    

@app.route('/delete/<msg_filename>',methods=["GET"])
def delete(msg_filename):

	filename = "cargo/"+msg_filename
	os.remove(filename)

	return redirect('/')



if __name__ == "__main__":
	app.run(host=localConfig.HOST, port=localConfig.PORT)
