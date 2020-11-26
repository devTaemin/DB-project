import sqlite3
import numpy
import pandas as pd

def dbcon():
    return sqlite3.connect('myDB.db')

'''
def create_table():
    try:
        db = dbcon()
        Cursor = db.cursor()
        query = "CREATE TABLE Student \
        (num int(4), major varchar(50), name varchar(50), \
         grade double(8), toeic double(8), intern double(8), corp varchar(50))"
        Cursor.execute(query)
        db.commit()
    except Exception as e:
        print('db create table error', e)
    finally:
        db.close()
'''
def insert_data(num, major, name, grade, toeic, intern, corp):
    try:
        db = dbcon()
        Cursor = db.cursor()
        setdata = (num, major, name, grade, toeic, intern, corp)
        Cursor.execute("INSERT INTO student VALUES(?, ?, ?, ?, ?, ?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db insert data error', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT * FROM student")
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_major(_major):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT * FROM student WHERE 전공 = '{}'".format(_major))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_num(num):
    ret = ()
    try:
        db = dbcon()
        Cursor = db.cursor()
        setdata = (num, )
        Cursor.execute('SELECT * FROM student WHERE num = ?', setdata)
    except Exception as e:
        print('db select num error', e)
    finally:
        db.close()
        return ret
