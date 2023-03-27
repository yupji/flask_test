# 애플리케이션 구동
    - flask 명령상 기본으로 찾는 파일
        - wsgi.py
        - app.py
        - 환경변수에 지정된 파일을(FLASK_APP=xxx) 찾는다
    - 커스텀 설정
        1. 환경변수를 지정하고 실행 -> OS에 설정하거나 혹은 shell(맥/리눅스) or cmd(윈도우) 작성해서 구동
            - set FLASK_APP=stat_app
            - flask run
        2. 환경변수 파일을 읽어서 처리
            - conda install python-dotenv -y
            - pip install python-dotenv
            - 파일 생성
                - env.config
                - start_app.py
            - 실행
                - flask -e ./env.config run
        3. 명령 수행시 옵션 제공
            - flask --app start_app run
            - flask --app start_app --debug run

# 실습
    - wsgi.py 파일 생성
        - flask run