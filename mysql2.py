#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        SQLite reader/writer
# Purpose:     Database script for school attendance system
#
# Author:      Pamilerin 'PI' Idowu
#
# Created:     27.7.2016
# 
#-------------------------------------------------------------------------------
#from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

from time import strftime,localtime
import datetime

cnx = mysql.connector.connect(user='pi', database ='attendance')
cur = cnx.cursor()
   
    

'''Checks for courses taught by instructor and returns'''
def checkInstructor(cardid):
    #check database for instructor card
    #cur.execute("INSERT INTO instructor (instructorid,firstname,lastname,cardid) VALUES (1,'Gbolahan','Idowu','0487E6B2DE3680')")
    cur.execute("SELECT cardid FROM instructor")
    rows = cur.fetchall()
    for row in rows:
        if row[0] == cardid:
            print row[0]
            #print instructor details to screen
            cur.execute("SELECT firstname,lastname FROM instructor WHERE cardid= ?",(cardid,))
            drow = cur.fetchone()
            print "Welcome ", drow[1]+"\t"+drow[0] 
            courseid = logInstructor(cardid)
            return (True,)
        else:
            print "Not an Instructor !!!!!"
            return False
    cursor.close()
    cnx.close()
    
        
        
def logInstructor(cardid):
    cur.execute("SELECT instructorid FROM instructor WHERE cardid = ?", (cardid,))
    row = cur.fetchone()
    print row[0]
    cur.execute("SELECT * FROM course WHERE instructorid = ? ", (row,))
    rows = cur.fetchall()
    print rows
    for i in rows:
        print i[1]+"\t"+i[2]
    #must print to screen
    print "select course"
    selected_course = 1
    print "Attendance for %s begins..."
    #return course info to be printed to screen then save id in variable
    #to be used later
    dCurrentTime = datetime.datetime.now()
    currentdate = str(datetime.datetime(dCurrentTime.year,dCurrentTime.month,dCurrentTime.day))
    cur.execute("""INSERT INTO attendance (courseid,date) VALUES (?, ?)""", (selected_course,currentdate))
    cnx.commit()
    cursor.close()
    cnx.close()
    return selected_course

def logStudent(cardid, courseid):
    cur.execute("SELECT cardid FROM student")
    rows = cur.fetchall()    
    for row in rows:
        if row == cardid:
            cur.execute("SELECT firstname,lastname FROM student WHERE cardid= ?", (cardid,))
            row = cur.fetchone()
            dCurrentTime = datetime.datetime.now()
            currenttime = str(datetime.datetime(ss.year,ss.month,ss.day,ss.hour,ss.minute,ss.second,ss.microsecond))[11:23]
            cur.execute("""INSERT INTO attendance (cardid,time) VALUES (?, ?)""", (courseid,currentime))
            print row[1]+" "+row[0]+" has logged in at "+currenttime
            cnx.commit()
        else:
            print "Not Registered"
    cursor.close()
    cnx.close()
    
    











