"""
@author: devTaemin
"""
from flask import Flask, render_template, request
import dbdb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/update')
def Update():
    return render_template("update.html", )


@app.route('/method', methods = ['GET', 'POST'])
def method():
    if request.method == 'GET':
        num = request.args["student_num"]
        major = request.args["student_major"]
        name = request.args["student_name"]
        grade = request.args["grade"]
        toeic = request.args["toeic"]
        intern = request.args["intern"]
        corp = request.args["corp"]
        return "GET으로 전달된 데이터({}, {}, {}, {}, {}, {}, {})".format(
        num, major, name, grade, toeic, intern, corp)
    else:
        num = request.form["student_num"]
        major = request.form["student_major"]
        name = request.form["student_name"]
        grade = request.form["grade"]
        toeic = request.form["toeic"]
        intern = request.form["intern"]
        corp = request.form["corp"]
        dbdb.insert_data(num, major, name, grade, toeic, intern, corp)
        return "POST으로 전달된 데이터({}, {}, {}, {}, {}, {}, {})".format(
        num, major, name, grade, toeic, intern, corp)



@app.route('/search')
def Search():
    info = dbdb.select_all()
    return render_template("search.html", DBdata = info)


@app.route('/inputMajor', methods = ['GET', 'POST'])
def inputMajor():
    if request.method == 'POST':
        input_major = request.form['input_major']
        #return "출력: {}".format(input_major)
        info = dbdb.select_major(input_major)
        info_grade = dbdb.select_grade(input_major)
        info_toeic = dbdb.select_toeic(input_major)
        info_intern = dbdb.select_intern(input_major)
        info_salary = dbdb.select_salary(input_major)
        info_corporation = dbdb.select_corporation(input_major)
        #return "{}".format(input_major)
        return render_template("input-major.html", DBdata = info, majorName = input_major, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary, DBdata_corporation = info_corporation)
    else:
        input_major = request.args['input_major']
        #return "출력: {}".format(input_major)
        info = dbdb.select_major(input_major)
        info_grade = dbdb.select_grade(input_major)
        info_toeic = dbdb.select_toeic(input_major)
        info_intern = dbdb.select_intern(input_major)
        info_salary = dbdb.select_salary(input_major)
        info_corporation = dbdb.select_corporation(input_major)
        return render_template("input-major.html", DBdata = info, majorName = input_major, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary, DBdata_corporation = info_corporation)



if __name__ == '__main__':
    app.run(debug = True, port = 7000)
