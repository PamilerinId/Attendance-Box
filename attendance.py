#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path = sys.path + ['nfcpy']
import os
os.chdir("/home/pi/Attendance")

import nfc
import RPi.GPIO as GPIO
import mysql2
import initdb2 as initdb

initdb.runscript()

import datetime
import time
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

initdb()

def main(tag):
    GPIO.output(12,0)
    dCurrentTime = datetime.datetime.now()
    cCurrentTime = str(datetime.datetime(dCurrentTime.year,dCurrentTime.month,dCurrentTime.day,dCurrentTime.hour,dCurrentTime.minute,dCurrentTime.second,dCurrentTime.microsecond))[:23]
    s = str(tag)
    print s
    start_id = s.find('ID=') + 3
    cardid = s[start_id:start_id + 14]
    #Checking to validate card
    check = mysql.checkInstructor(cardid)
    print check
    while check[0] is True:
        courseid = check[1]
        logStudent(cardid, courseid)




print "Attempting to connect nfc reader..."	
while True:
	try:
		clf = nfc.ContactlessFrontend('tty:AMA0:pn532')
		print "Success..!"
		break
	except IOError as error:
		if error.errno != 19:
			raise error
		print "Attempting to connect nfc reader (retrying)..."
		time.sleep(1.0)
		continue
       	
#clf = nfc.ContactlessFrontend('tty:AMA0:pn53x')
while True:
    print "Swipe Your Card!!"
    clf.connect(rdwr={'on-connect':main})
GPIO.cleanup()
