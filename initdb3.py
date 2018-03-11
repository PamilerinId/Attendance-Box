#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        MySQL Schema
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

DB_NAME = 'attendance_db'

TABLES = {}
TABLES['admin'] = (
    "CREATE TABLE IF NOT EXISTS `attendance_db`.`admin` ("
    "  `admin_id` INT NOT NULL AUTO_INCREMENT,"
    "  `admin_class` VARCHAR(14) NOT NULL,"
    "  `card_id` VARCHAR(16) NOT NULL,"
    "  PRIMARY KEY (`admin_id`)"
    ") ENGINE=InnoDB")

TABLES['instructor'] = (
    "CREATE TABLE IF NOT EXISTS `attendance_db`.`instructor`("
    "  `instructor_id` INT NOT NULL AUTO_INCREMENT,"
    "  `first_name` VARCHAR(45) NOT NULL,"
    "  `last_name` VARCHAR(45) NOT NULL,"
    "  `card_id` VARCHAR(16) NOT NULL,"
    "  PRIMARY KEY (`instructor_id`)"
    ") ENGINE=InnoDB")

TABLES['course'] = (
    "CREATE TABLE IF NOT EXISTS `attendance_db`.`course` ("
    "  `course_id` INT NOT NULL AUTO_INCREMENT,"
    "  `course_title` VARCHAR(45) NOT NULL,"
    "  `course_code` VARCHAR(45) NOT NULL,"
    "  `instructor_id` INT NOT NULL,"
    "  PRIMARY KEY (`course_id`),"
    "  INDEX `instructor_id_idx` (`instructor_id` ASC),"
    "  CONSTRAINT `instructor_id`"
    "    FOREIGN KEY (`instructor_id`)"
    "    REFERENCES `attendance_db`.`instructor` (`instructor_id`)"
    "    ON DELETE CASCADE"
    "    ON UPDATE NO ACTION)"
    ") ENGINE=InnoDB")

TABLES['student'] = (
    "CREATE TABLE IF NOT EXISTS `attendance_db`.`student`("
    "  `student_id` INT NOT NULL AUTO_INCREMENT,"
    "  `first_name` VARCHAR(45) NOT NULL,"
    "  `last_name` VARCHAR(45) NOT NULL,"
    "  `matric_no` VARCHAR(14) NOT NULL,"
    "  `card_id` VARCHAR(16) NOT NULL,"
    "  PRIMARY KEY (`student_id`),"
    ") ENGINE=InnoDB")

TABLES['attend_log'] = (
    "CREATE TABLE IF NOT EXISTS `attendance_db`.`attend_log` ("
    "  `course_id` INT NOT NULL,"
    "  `student_id` INT NOT NULL,"
    "  `date` DATE NOT NULL,"
    "  `time_in` DATE NOT NULL,"
    "  PRIMARY KEY (`course_id`, `student_id`),"
    "  INDEX `student_id_idx` (`student_id` ASC),"
    "  CONSTRAINT `course_id`"
    "    FOREIGN KEY (`course_id`)"
    "    REFERENCES `attendance_db`.`course` (`course_id`)"
    "    ON DELETE CASCADE"
    "    ON UPDATE NO ACTION,"
    "  CONSTRAINT `student_id`"
    "    FOREIGN KEY (`student_id`)"
    "    REFERENCES `attendance_db`.`student` (`student_id`)"
    "    ON DELETE CASCADE"
    "    ON UPDATE NO ACTION
    ") ENGINE = InnoDB")

cnx = mysql.connector.connect(user='root', passwd='raspberry')
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

    for name, ddl in TABLES.iteritems():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

create_database(cursor)
cursor.close()
cnx.close()
