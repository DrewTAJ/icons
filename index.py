#!/usr/bin/env python3

import smtplib
import os
import grilly
import print_character

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def send_email(file_name):
    from_email = "drew.t.a.johnson@gmail.com"
    to_email = "drew.t.a.johnson@gmail.com"
    message = "This is a message"

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(from_email, to_email, message)         
        print("Successfully sent email")
    except Exception as exception:
        print(exception)
        print("Error: unable to send email")

def main():
    test_character = grilly.getCharacter()
    img = print_character.main(test_character)
    send_email("test.pdf")

# def save_character_sheet():
#     dir_name = "characters/"
#     if not os.path.exists(dir_name):
#         os.makedirs(dir_name)

#     file_name = "character.pdf"

#     merger = PdfFileMerger()
    
main()