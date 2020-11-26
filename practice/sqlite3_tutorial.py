#1. sqlite를 import
import pandas as pd
import sqlite3, numpy

#2. DB에 연결
conn = sqlite3.connect("C:\\Users\\Taemin\\Documents\\GitHub\\DB-project\\myDB.db")

#3. Cursor 객체 생성
#Cursor = conn.cursor()

#4. 테이블 생성
#query = "CREATE TABLE Student \
#(num int(4), major varchar(50), name varchar(50), \
# grade double(8), toeic double(8), intern double(8), corp varchar(50))"
#Cursor.execute(query)

#5. execute에 DB 적용
#conn.commit()

#6. 접속한 DB 종료
#conn.close()

#CONTENTS = pd.read_sql("SELECT * FROM student", Cursor)
#print(dict(CONTENTS))

cs = conn.cursor()

CONTENTS = pd.read_sql_query("SELECT * FROM student", conn)
print(dict(CONTENTS))
