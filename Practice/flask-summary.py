from flask import Flask, url_for, request
app = Flask(__name__)

#라우팅
#------------------------------------------------------------------------------
@app.route("/")
def index(): pass
    #return "<h1>Index page</h1>"
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# HTTP method
# GET: Client request information to Server, Server send infromation
# POST: Clinet send information to Server
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
                       return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    #Activate if the request is 'GET' or verifying information is wrong
    return render_template('login.html', error = error)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('practice-template/hello.html', name = name)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
@app.route('/user/<username>')
def profile(username): pass
    # show the user profile for that user
    #return 'User %s' % username
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username = 'Taemin'))
    print(url_for('static', filename = 'style.css'))  #정적 파일 경로 찾기 'static'
#------------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(debug = True)
    # debug = True를 이용하여 코드 변경 감지, 자동 리로드, 오류 체크
    # app.run(host = '0.0.0.0') 네트워크 상 모든 사용자 신뢰
