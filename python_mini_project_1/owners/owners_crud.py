import cx_Oracle


def insert(conn):
    cursor = conn.cursor()
    try:
        name = input("이름: ")
        age = int(input("나이: "))
        address = input("주소: ")
        experience_in_raise = input("양육 경력: ")
        did_pre_training = input("사전교육 이수 여부: ")
        monthly_income = input("월 수입(단위: 천): ")
        report_date = input("신고일: ")
        sql = """insert into owners
               (owner_id, name, age, address,
                     experience_in_raise, did_pre_training,
                     monthly_income, report_date)
               values
               (owners_seq.nextval, :name, :age, :address,
                :experience_in_raise, :did_pre_training,
                 :monthly_income, to_date(:report_date, 'rr/MM/DD'))"""

        cursor.execute(sql,
                       (name, age, address,
                        experience_in_raise, did_pre_training,
                        monthly_income, report_date))
        print("정보가 입력되었습니다")
    except cx_Oracle.Error as e:
        errorObj, = e.args
        print(errorObj.message)
        return
    except Exception as e:
        print(e.args)
        return


def update():
    pass


def get_player_by_name():
    pass


def get_player_by_team():
    pass


def get_players():
    pass


def delete():
    pass