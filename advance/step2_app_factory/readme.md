# 어플리케이션 팩토리
    - 엔트리 위치 조정, 코드 조정
    - app = Flask(__name__)
        - 현재 이 코드는 전역변수로 존재
        - 프로젝트 규모가 커지면, 순환참조를 할 확률이 크다
        - flask 구현시 어플리케이션 팩토리라는 형태로 사용하라 => 권장

# 방법
    - 플라스크 객체를 생성하는 코드를
        - 특정 패키지 밑에 위치 => ex) service
        - __init__.py 로 이름변경
        - 구조
            service
            L __init__.py
        - 최종 실행 명령
            - flask --app service --debug run