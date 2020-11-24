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
    info = dbdb.select_all()
    return render_template("update.html", DBdata = info)


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
    return render_template("search.html")





if __name__ == '__main__':
    app.run(debug = True, port = 7000)
