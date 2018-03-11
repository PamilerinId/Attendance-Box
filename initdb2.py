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

from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'attendance'

TABLES = {}
TABLES['admin'] = (
    "CREATE TABLE `admin` ("
    "  `admin_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `admin_class` varchar(14) NOT NULL,"
    "  `cardid` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`admin_id`)"
    ") ENGINE=InnoDB")

TABLES['instructor'] = (
    "CREATE TABLE `instructor` ("
    "  `instructor_id` char(4) NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `cardid` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`instructor_id`)"
    ") ENGINE=InnoDB")

TABLES['course'] = (
    "CREATE TABLE `course` ("
    "  `course_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `course_title` varchar(16) NOT NULL,"
    "  `course_code` varchar(14)  NOT NULL,"
    "  `instructor_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`course_id`,`instructor_id`),"
    "  KEY `instructor_id` (`instructor_id`),"
    "  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`instructor_id`) "
    "     REFERENCES `instructor` (`instructor_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['student'] = (
    "CREATE TABLE `student` ("
    "  `student_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `matric_no` varchar(16) NOT NULL,"
    "  `cardid` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`student_id`),"
    ") ENGINE=InnoDB")

TABLES['attendance'] = (
    "  CREATE TABLE `attendance` ("
    "  `course_id` int(11) NOT NULL,"
    "  `date` date NOT NULL,"
    "  `time_in` date NOT NULL,"
    "  `student_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`course_id`,`student_id`),"
    "  KEY `course_id` (`course_id`),"
    "  KEY `student_id` (`student_id`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`course_id`) "
    "     REFERENCES `course` (`course_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`student_id`) "
    "     REFERENCES `student` (`student_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='pi')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

##for name, ddl in TABLES.iteritems():
##    try:
##        print("Creating table {}: ".format(name), end='')
##        cursor.execute(ddl)
##    except mysql.connector.Error as err:
##        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
##            print("already exists.")
##        else:
##            print(err.msg)
##    else:
##        print("OK")

cursor.close()
cnx.close()
