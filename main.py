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
    info2 = dbdb.select_all_corp()

    title = '취업 현황'
    colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500"
    ]
    labels = [info2[0][0], info2[1][0], info2[2][0], info2[3][0], info2[4][0], info2[5][0], info2[6][0], info2[7][0], info2[8][0], info2[9][0]]
    values = [info2[0][3], info2[1][3], info2[2][3], info2[3][3], info2[4][3], info2[5][3], info2[6][3], info2[7][3], info2[8][3], info2[9][3]]
    return render_template("search.html", DBdata = info, DBdata2 = info2, max = 17000, title = title, set = zip(values, labels, colors))
    #return "{} {} {} {}".format(values[0], values[1], values[2], values[3])
    #return "{} {} {} {}".format(labels[0], labels[1], labels[2], labels[3])

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

        bar_grade = ["평균", "최고", "최저"]
        bar_grade_score = [info_grade[0][0], info_grade[0][1], info_grade[0][2]]
        bar_toeic = ["평균", "최고", "최저"]
        bar_toeic_score = [info_toeic[0][0], info_toeic[0][1], info_toeic[0][2]]
        bar_intern = ["평균", "최고", "최저"]
        bar_intern_score = [info_intern[0][0], info_intern[0][1], info_intern[0][2]]
        bar_salary = ["평균", "최고", "최저"]
        bar_salary_score = [info_salary[0][0], info_salary[0][1], info_salary[0][2]]


        #return "{} {} {}".format(bar_grade_score[0], bar_grade_score[1], bar_grade_score[2])
        #return "{} {} {}".format(bar_grade[0], bar_grade[1], bar_grade[2])
        #return "{}".format(input_major)
        return render_template("input-major.html", DBdata = info, majorName = input_major, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary, DBdata_corporation = info_corporation,
        max = 4.3, grade = bar_grade_score, bgrade = bar_grade, toeic = bar_toeic_score, btoeic = bar_toeic, intern = bar_intern_score, bintern = bar_toeic, salary = bar_salary_score, bsalary = bar_salary)
    else:
        input_major = request.args['input_major']
        #return "출력: {}".format(input_major)
        info = dbdb.select_major(input_major)
        info_grade = dbdb.select_grade(input_major)
        info_toeic = dbdb.select_toeic(input_major)
        info_intern = dbdb.select_intern(input_major)
        info_salary = dbdb.select_salary(input_major)
        info_corporation = dbdb.select_corporation(input_major)

        bar_grade = ["평균", "최고", "최저"]
        bar_grade_score = [info_grade[0][0], info_grade[0][1], info_grade[0][2]]
        bar_toeic = ["평균", "최고", "최저"]
        bar_toeic_score = [info_toeic[0][0], info_toeic[0][1], info_toeic[0][2]]
        bar_intern = ["평균", "최고", "최저"]
        bar_intern_score = [info_intern[0][0], info_intern[0][1], info_intern[0][2]]
        bar_salary = ["평균", "최고", "최저"]
        bar_salary_score = [info_salary[0][0], info_salary[0][1], info_salary[0][2]]

        #return render_template("input-major.html", DBdata = info, majorName = input_major, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary, DBdata_corporation = info_corporation)
        return render_template("input-major.html", DBdata = info, majorName = input_major, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary, DBdata_corporation = info_corporation,
        grade = bar_grade_score, bgrade = bar_grade, toeic = bar_toeic_score, btoeic = bar_toeic, intern = bar_intern_score, bintern = bar_toeic, salary = bar_salary_score, bsalary = bar_salary)

@app.route('/inputCorp', methods = ['GET', 'POST'])
def inputCorp():
    if request.method == 'POST':
        input_Corp = request.form['input_Corp']
        #info = dbdb.select_all_corp()
        #return "{}".format(input_major)
        info = dbdb.select_corp(input_Corp)
        info_grade = dbdb.select_grade_c(input_Corp)
        info_toeic = dbdb.select_toeic_c(input_Corp)
        info_intern = dbdb.select_intern_c(input_Corp)
        info_salary = dbdb.select_salary_c(input_Corp)

        bar_grade = ["평균", "최고", "최저"]
        bar_grade_score = [info_grade[0][0], info_grade[0][1], info_grade[0][2]]
        bar_toeic = ["평균", "최고", "최저"]
        bar_toeic_score = [info_toeic[0][0], info_toeic[0][1], info_toeic[0][2]]
        bar_intern = ["평균", "최고", "최저"]
        bar_intern_score = [info_intern[0][0], info_intern[0][1], info_intern[0][2]]
        bar_salary = ["평균", "최고", "최저"]
        bar_salary_score = [info_salary[0][0], info_salary[0][1], info_salary[0][2]]

        #return "{} {} {}".format(bar_grade_score[0], bar_grade_score[1], bar_grade_score[2])
        return render_template("input-corp.html", DBdata = info, corpName = input_Corp, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary,
        grade = bar_grade_score, bgrade = bar_grade, toeic = bar_toeic_score, btoeic = bar_toeic, intern = bar_intern_score, bintern = bar_toeic, salary = bar_salary_score, bsalary = bar_salary)

    else:
        input_major = request.args['input_Corp']
        #info = dbdb.select_all_corp()
        #return "출력: {}".format(input_major)
        info = dbdb.select_corp(input_Corp)
        info_grade = dbdb.select_grade_c(input_Corp)
        info_toeic = dbdb.select_toeic_c(input_Corp)
        info_intern = dbdb.select_intern_c(input_Corp)
        info_salary = dbdb.select_salary_c(input_Corp)

        bar_grade = ["평균", "최고", "최저"]
        bar_grade_score = [info_grade[0][0], info_grade[0][1], info_grade[0][2]]
        bar_toeic = ["평균", "최고", "최저"]
        bar_toeic_score = [info_toeic[0][0], info_toeic[0][1], info_toeic[0][2]]
        bar_intern = ["평균", "최고", "최저"]
        bar_intern_score = [info_intern[0][0], info_intern[0][1], info_intern[0][2]]
        bar_salary = ["평균", "최고", "최저"]
        bar_salary_score = [info_salary[0][0], info_salary[0][1], info_salary[0][2]]

        return render_template("input-corp.html", DBdata = info, corpName = input_Corp, DBdata_grade = info_grade, DBdata_toeic = info_toeic, DBdata_intern = info_intern, DBdata_salary = info_salary,
        grade = bar_grade_score, bgrade = bar_grade, toeic = bar_toeic_score, btoeic = bar_toeic, intern = bar_intern_score, bintern = bar_toeic, salary = bar_salary_score, bsalary = bar_salary)



if __name__ == '__main__':
    app.run(debug = True, port = 7000)
