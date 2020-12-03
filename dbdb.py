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
def insert_data(num, major, name, grade, toeic, intern, corp, salary):
    try:
        db = dbcon()
        Cursor = db.cursor()
        setdata = (num, major, name, grade, toeic, intern, corp, salary)
        Cursor.execute("INSERT INTO student VALUES(?, ?, ?, ?, ?, ?, ?, ?)", setdata)
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


def select_corp(_corp):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT * FROM student WHERE 회사 = '{}'".format(_corp))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_grade(_major):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(학점), 2), MAX(학점), MIN(학점) FROM student WHERE 전공 = '{}' GROUP BY 전공".format(_major))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_grade_c(_corp):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(학점), 2), MAX(학점), MIN(학점) FROM student WHERE 회사 = '{}' GROUP BY 회사".format(_corp))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_toeic(_major):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(토익), 2), MAX(토익), MIN(토익) FROM student WHERE 전공 = '{}' GROUP BY 전공".format(_major))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_toeic_c(_corp):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(토익), 2), MAX(토익), MIN(토익) FROM student WHERE 회사 = '{}' GROUP BY 회사".format(_corp))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_intern(_major):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(인턴), 2), MAX(인턴), MIN(인턴) FROM student WHERE 전공 = '{}' GROUP BY 전공".format(_major))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_intern_c(_corp):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(인턴), 2), MAX(인턴), MIN(인턴) FROM student WHERE 회사 = '{}' GROUP BY 회사".format(_corp))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_salary(_major):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(s.개인연봉), 2), MAX(s.개인연봉), MIN(s.개인연봉) FROM student s LEFT JOIN corp c ON s.회사 == c.회사 WHERE 전공 = '{}' GROUP BY 전공".format(_major))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_salary_c(_corp):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT ROUND(AVG(s.개인연봉), 2), MAX(s.개인연봉), MIN(s.개인연봉) FROM student s LEFT JOIN corp c ON s.회사 == c.회사 WHERE s.회사 = '{}' GROUP BY s.회사".format(_corp))
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret


def select_corporation(_major):
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT c.회사, c.위치, (COUNT(c.회사)) FROM student s LEFT JOIN corp c ON s.회사 == c.회사 WHERE 전공 = '{}' GROUP BY c.회사".format(_major))
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


def select_all_corp():
    ret = list()
    try:
        db = dbcon()
        Cursor = db.cursor()
        Cursor.execute("SELECT c.회사 AS 소속회사, c.위치, c.평균연봉, (COUNT(c.회사)) AS 소속수 FROM student s LEFT JOIN corp c ON s.회사 == c.회사 GROUP BY c.회사")
        ret = Cursor.fetchall()
    except Exception as e:
        print('db select all error', e)
    finally:
        db.close()
        return ret
