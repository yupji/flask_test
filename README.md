# 파이썬 기반 웹 프로그래밍

# 목표
    - 웹 환경 이해 및 웹 프로그램 구성 이해
    - flask 기반 웹기반 백엔드(서버)프로그래밍
    - blueprint를 이용한 기능별 분할 구성
    - 데이터베이스 연동 (sql,ORM)
    - 배포 및 운영

# 발전적 목표
    - 머신러닝(딥러닝 포함) 모델 서빙및 서비스를 구현
    - 구축된 서비스를 도커 및 쿠버네티스 기반하에서 운영
    - MLOps에 연동사용

# 가상환경 구축
    - 순수 파이썬
        - 가상환경을 모아두는 폴더 생성
            - mkdir venvs
        - 해당폴더 이동
            - cd venvs
        - 가상환경 생성
            - python -m venv 가상환경이름
            - python -m venv web
        - 가상환경 활성화 하는 명령어 위치까지 이동
            - cd ./web/Scripts
        - 가상환경 활성화
            - 윈도우
                - activate
        - 최종 프럼프트 형태
            - (web) >
    - 아나콘다(미니콘다, ...)

# 필요한 패키지 설치
    - requirements.txt 생성
    - 작성
        - 수동
            - 직접 기업
            - 패키지==버전
            - 패키지
        - 자동 
            - 패키지가 이미 일부 설치가, 혹은 전부 설치가 되어 있다.
            - 내가 설치하지 않은 패키지도 추가된다.
            - pip freeze > requirements.txt
    - 설치
        - pip install -r requirements.txt