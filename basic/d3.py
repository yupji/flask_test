'''
    데이터베이스 접속 후 쿼리 수행
'''
import pymysql as my

connection = None
try:
    connection = my.connect(host        = 'localhost',      # 127.0.0.1 서버주소
                            #port        = 3306             # 포트
                            user        = 'root',           # 사용자 계정, root 계정 외의 계정 사용 권장
                            password    = 'so970622!!',     # 비밀번호
                            database    = 'ml_db',             # 접속할 데이터베이스
                            # 조회 결과는 [ {}, {}, {}, ...  ] 이런 형태로 추출된다
                            cursorclass = my.cursors.DictCursor
                            )
    with connection.cursor() as cursor: # cursor는 with문을 벗어나면 자동으로 닫힘
        sql = '''
            SELECT
                uid, `name`, regdate
            FROM
                users
            WHERE
                uid='guest'
            AND
                upw='1234';
        '''
        cursor.execute( sql )
        row = cursor.fetchone()
        # 5. 결과확인 -> 딕셔너리 -> 이름만 추출하시오 -> '게스트'
        print( row['name'] )
        pass
except Exception as e:
    print('접속 오류', e)
else:
    print('접속시 문제 없었음')
finally:
    if connection:
        connection.close()