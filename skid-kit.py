import time
import smtplib
import re
import json
from urllib2 import urlopen
import requests
import os
import sys
img = """"

  /$$$$$$  /$$       /$$       /$$       /$$   /$$ /$$   /$$
 /$$__  $$| $$      |__/      | $$      | $$  /$$/|__/  | $$
| $$  \__/| $$   /$$ /$$  /$$$$$$$      | $$ /$$/  /$$ /$$$$$$
|  $$$$$$ | $$  /$$/| $$ /$$__  $$      | $$$$$/  | $$|_  $$_/
 \____  $$| $$$$$$/ | $$| $$  | $$      | $$  $$  | $$  | $$
 /$$  \ $$| $$_  $$ | $$| $$  | $$      | $$\  $$ | $$  | $$ /$$
|  $$$$$$/| $$ \  $$| $$|  $$$$$$$      | $$ \  $$| $$  |  $$$$/
 \______/ |__/  \__/|__/ \_______/      |__/  \__/|__/   \___/



"""
print img

def ipLookUp():
    x = raw_input("Please insert the IP to trace")
    url = 'http://ipinfo.io/' + x + '/json'
    response = urlopen(url)
    data = json.load(response)
    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']

    print 'Your IP detail\n '
    print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org, region, country, city, IP)

def SMSBomber():

    # CONFIG. You can change any of the values on the right.
    #
    email_provider = 'smtp.gmail.com'  # server for your email- see ReadMe on github
    email_address = "*******@gmail.com"  # your email
    email_port = 587  # port for email server- see ReadMe on github

    email_provider1 = 'smtp.gmail.com'  # server for your email- see ReadMe on github
    email_address1 = "******@gmail.com"  # your email
    email_port1 = 587  # port for email server- see ReadMe on github

    email_provider2 = 'smtp.gmail.com'  # server for your email- see ReadMe on github
    email_address2 = "*******@gmail.com"  # your email
    email_port2 = 587  # port for email server- see ReadMe on github

    email_provider3 = 'smtp.gmail.com'  # server for your email- see ReadMe on github
    email_address3 = "******@gmail.com"  # your email
    email_port3 = 587  # port for email server- see ReadMe on github

    password = "********"  # your email password
    #
    # This starts the actaul user input phase of the code
    #
    #
    textMessage = raw_input("Please insert your desired text message: ")
    text_amount_input = raw_input("Please insert the amount of text messages")
    target = raw_input("Please insert the target number in email form ('http://freecarrierlookup.com'): ")
    wait_limit = raw_input("Please insert the time between messages in seconds: ")
    msg = textMessage  # your txt message
    text_amount = int(text_amount_input)  # amount sent
    target_email = target  # target number. must be in email form- see ReadMe on github
    wait = int(wait_limit)  # seconds in between messages

    #
    # This sends the text messages
    #
    server = smtplib.SMTP(email_provider, email_port)
    server.starttls()
    server.login(email_address, password)
    for _ in range(0, text_amount):
        server.sendmail(email_address, target_email, msg)
        print("Text sent from account #1")
        time.sleep(wait)

    server = smtplib.SMTP(email_provider1, email_port1)
    server.starttls()
    server.login(email_address1, password)
    for _ in range(0, text_amount):
        server.sendmail(email_address1, target_email, msg)
        print("Text Sent From Account#2")
        time.sleep(wait)

    server = smtplib.SMTP(email_provider2, email_port2)
    server.starttls()
    server.login(email_address2, password)
    for _ in range(0, text_amount):
        server.sendmail(email_address2, target_email, msg)
        print("Text Sent From Account#3")
        time.sleep(wait)

    server = smtplib.SMTP(email_provider3, email_port3)
    server.starttls()
    server.login(email_address3, password)
    for _ in range(0, text_amount):
        server.sendmail(email_address3, target_email, msg)
        print("Text Sent From Account#4")
        time.sleep(wait)

    print("All texts were sent to the target")
    server.quit()

def instaChecker():
    # prompts user for the list name
    user_list = raw_input("Please enter the name of the list: ")

    # imports usernames as list
    with open(user_list, "r") as f:
        usernames = f.read().split("\n")

    # checks each username
    for user in usernames:
        r = requests.get("https://www.instagram.com/" + user)
        if r.status_code == 404:  # if page returns a 404 the username is available
            print("{} is available".format(user))
    # stops program from quitting
    input("")

def folderSpam():
    amount0 = 0
    amount = raw_input("Please insert how many folders you want to create: ")
    amount = int(amount)
    path = raw_input("Please insert the directory to create the folders in: ")
    msg = raw_input("Please insert the spam name of the folders")
    for i in range(0, amount):
        os.chdir(path)
        os.mkdir(msg + str(amount0))
        amount0 +=1
    print "All folders have been created"

def spooky():
    def list_files(startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    list_files("C:\\")

def start():
    start_input = raw_input("Please enter a command or type !help for a list of command: ")
    if start_input == "!help":
        print "!ipLookUp - Starts the IP Look up script \n !SMSbomber - Starts the SMS bomber \n !instaCheck - Starts the Instagram Username Checker \n !folderSpam - Spam creates folders! \n !spooky - be a hacker"
        start()
    elif start_input == "!ipLookUp":
        ipLookUp()
        start()
    elif start_input == "!SMSbomber":
        SMSBomber()
        start()
    elif start_input == "!intaCheck":
        instaChecker()
        start()
    elif start_input == "!folderSpam":
        folderSpam()
        start()
    elif start_input == "!spooky":
        spooky()
        start()
print "Welcome to The Skid Tool Kit Version 1.0"
start()
