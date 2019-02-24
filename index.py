#!/usr/bin/env python3

import smtplib
import os
import grilly
import print_character
import credentials
import random, threading, webbrowser
import string
from random import *

from flask import Flask, render_template, Blueprint, request, session, abort, redirect

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__, '/templates')
app.secret_key = credentials.getSecret()

def generate_random_string():
    min_char = 8
    max_char = 12
    allchar = string.ascii_letters + string.punctuation + string.digits
    random_string = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return random_string

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = generate_random_string()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

@app.route("/", methods=['GET'])
def index():
    return render_template('form.html')

@app.route("/send", methods=['POST'])
def main():
    if request.form["email"] != None:
        if request.form["email"] != "" and isinstance(request.form["email"], str):
            email = request.form["email"]
            test_character = grilly.getCharacter()
            img = print_character.main(test_character)
            file_name = save_character_sheet(img)
            error = send_email(email, file_name)
            if error:
                return render_template('error.html', error=error), 400
            return render_template('success.html', email=email)
    return render_template('form.html', error="Email address is missing or not valid"), 400

def attach_file(msg, file_path, file_name):
    fp = open(file_path, 'rb')
    pdfAttach = MIMEApplication(fp.read(), _subtype = "pdf")
    fp.close()
    pdfAttach.add_header('content-disposition', 'attachment', filename = ('utf-8', '', file_name))
    msg.attach(pdfAttach)

def send_email(recipient, file_name):
    creds = credentials.getCredentials()
    from_email = creds["email"]
    to_email = recipient

    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'ICONS Character sheet'
        msg['To'] = recipient
        msg['From'] = creds['email']
        body = MIMEText('Hello\n\nThank you for taking an interest in my ICONS character. I was never really good at imagingin my characters in great detail so I just made him Billy Maze if he carried the products he was trying to sell in a trench coat with infinite storage space.\n\nDrew')
        msg.attach(body)
        attach_file(msg, file_name, 'character.pdf')
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.verify(recipient)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(creds["email"], creds["password"])
        smtpObj.sendmail(from_email, to_email, msg.as_string())
        smtpObj.close()
        print("Successfully sent email")
        return None
    except Exception as exception:
        print(exception)
        print("Error: unable to send email")
        return "Unable to send email at this time please try again later."

def save_character_sheet(img):
    dir_name = "characters/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    file_name = "character.pdf"
    file_dir = "%s%s" % (dir_name, file_name)
    img.save(file_dir, "PDF")
    return file_dir

@app.errorhandler(403)
def page_restricted(error):
    return render_template('form.html', error='Please submit your email again'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('form.html', error='Page not found'), 404

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    port = 5000
    url = "http://localhost:{0}".format(port)
    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run()