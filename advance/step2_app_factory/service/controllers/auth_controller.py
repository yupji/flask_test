from flask import render_template, request, url_for
from service.controllers import bp_auth as auth

# ~/auth
@auth.route('/')
def home():
    # 별칭, 함수명 => url_for( 앞의 내용 기입 ) => url이 리턴된다
    print( url_for('auth_bp.login') )
    return "auth 홈"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # jwt 관련 체크 => 정상(200), 오류(401)
        return 'jwt 체크 완료'

@auth.route('/logout')
def logout():
    return "auth logout"

@auth.route('/signup')
def signup():
    return "auth signup"

@auth.route('/delete')
def delete():
    return "auth delete"