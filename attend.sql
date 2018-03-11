--School Attendance System database script 
-- Wtitten by Pamilerin 'PI' Idowu

DROP SCHEMA IF EXISTS school_attendance;
CREATE SCHEMA school_attendance;
USE school_attendance;

DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
SET AUTOCOMMIT=0;

CREATE TABLE IF NOT EXISTS 'admin' (
    'adminid' int(11) unsigned NOT NULL,
    'adminclass' bigint(18) unsigned NOT NULL,
    'cardid' int(11) unsigned NOT NULL,
    PRIMARY KEY ('adminid')
)   ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `admin` VALUES (1,'Super',127800);

CREATE TABLE IF NOT EXISTS 'instructor' (
    'instructorid' int(11) unsigned NOT NULL AUTO_INCREMENT,
    'firstname' varchar(255) COLLATE utf8_czech_ci NOT NULL,
    'lastname' varchar(255) COLLATE utf8_czech_ci NOT NULL,
    'cardid' bigint(18) unsigned NOT NULL,
    PRIMARY KEY ('instructorid')
)   ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `instructor` VALUES (1,'Gbolahan','Idowu',1780000);

CREATE TABLE IF NOT EXISTS 'course' (
    'courseid' int(11) unsigned NOT NULL AUTO_INCREMENT,
    'courseTitle' varchar(255) NOT NULL,
    'coursecode' varchar(255) NOT NULL,
    'instructorid' int(11) unsigned NOT NULL,
    PRIMARY KEY ('courseid')
)   ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `course` VALUES (1,'Anatomy I','PHY205',1);
INSERT INTO `course` VALUES (2,'Programming Languages','CPS409',1);

CREATE TABLE IF NOT EXISTS 'student' (
    'studentid' int(11) unsigned NOT NULL AUTO_INCREMENT,
    'firstname' varchar(255) NOT NULL,
    'lastname' varchar(255) NOT NULL,
    'matricno' int(11) unsigned NOT NULL,    
    'cardid' bigint(18) unsigned NOT NULL,
    PRIMARY KEY ('studentid')
)   ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `student` VALUES (1,'Idowu','Pamilerin','NAS/12042',237500);
INSERT INTO `student` VALUES (2,'Lasisi','Femi','NAS/12047',186800);

CREATE TABLE IF NOT EXISTS 'attendance' (
    'courseid' int(11) unsigned NOT NULL,
    'date' varchar(50) NOT NULL,
    'timein' varchar(50) NOT NULL,
    'studentid' int(11) unsigned NOT NULL,
    PRIMARY KEY ('courseid')
)   ENGINE=InnoDB DEFAULT CHARSET=utf8;





