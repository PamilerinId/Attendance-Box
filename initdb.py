#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        SQLite Schema
# Purpose:     Database schema definition script for school attendance system
#
# Author:      Pamilerin 'PI' Idowu
#
# Created:     27.7.2016
# 
#-------------------------------------------------------------------------------

import sqlite3

con = sqlite3.connect("attendance.db")
cur = con.cursor()
#print "con created"
def runscript():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS admin
        (
            adminid INT PRIMARY KEY NOT NULL,
            adminclass TEXT NOT NULL,
            cardid INT NOT NULL
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS instructor
        (
            instructorid INT PRIMARY KEY NOT NULL,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            cardid CHAR(50) NOT NULL
            
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course
        (
            courseid INT PRIMARY KEY NOT NULL,
            courseTitle TEXT NOT NULL,
            coursecode CHAR(50) NOT NULL,
            instructorid INT NOT NULL
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student
        (
            studentid INT PRIMARY KEY NOT NULL,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            matricno CHAR(50) NOT NULL,    
            cardid CHAR(50)NOT NULL
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance
        (
            courseid INT PRIMARY KEY NOT NULL,
            date CHAR(50) NOT NULL,
            timein CHAR(50) NOT NULL,
            studentid INT NOT NULL
        );
        """)
    print "DD done"
    #################
    ##test data insert
    cur.execute("INSERT INTO admin (adminid,adminclass,cardid) VALUES (1,'Super',127800)")
    cur.execute("INSERT INTO instructor (instructorid,firstname,lastname,cardid) VALUES (1,'Gbolahan','Idowu','0487E6B2DE3680')")
    cur.execute("INSERT INTO course (courseid,courseTitle,coursecode,instructorid) VALUES (1,'Anatomy I','PHY205',1)")
    cur.execute("INSERT INTO course (courseid,courseTitle,coursecode,instructorid) VALUES (2,'Programming Languages','CPS409',1)")
    cur.execute("INSERT INTO student (studentid,firstname,lastname,matricno,cardid) VALUES (1,'Idowu','Pamilerin','NAS/12042','5AD58BA2')")
    cur.execute("INSERT INTO student (studentid,firstname,lastname,matricno,cardid) VALUES (2,'Lasisi','Femi','NAS/12047','04338BA2173C81')")
    print "DM done"

