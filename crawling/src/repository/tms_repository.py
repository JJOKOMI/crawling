import pymysql
from pymysql import cursors
from unicodedata import category
from src.service.tms import run


def findBoard():
    pass

# 딕셔너리커서 패치원 셀럭트 쓰기
def selectTms():
    try:
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='0520',
            db='naver_webtoon_db')

        try:
            cursor = connection.cursor(cursors=pymysql.cursors.DictCursor)
            sql = "select * from webtoon_tb as wt where wt.category_id = category_tb.category_id "
            cursor.execute(sql)
            categories = cursor.fetchone()

            cv = lambda \
            webtoon: f"(default, \'{webtoon['title']}\', \'{webtoon['author']}\', {selectTms().category_Id})"
            valueList = list(map(cv, findBoard()))
            values = ", ".join(valueList)
            print(values)

            return categories

        except Exception as e:
            print(e)
        finally:
            connection.close()

    except Exception as e:
        print("데이터 베이스 연결 실패")
