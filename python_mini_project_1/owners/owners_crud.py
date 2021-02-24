import cx_Oracle
from owners import owners
import csv
from time import strftime, localtime


def insert(conn):
    cursor = conn.cursor()
    try:
        name = input("이름: ")
        age = int(input("나이: "))
        address = input("주소: ")
        experience_in_raise = input("양육 경력: ")
        did_pre_training = input("사전교육 이수 여부: ")
        monthly_income = input("월 수입(단위: 만): ")
        report_date = input("신고일: ")
        phone_number = input("전화번호: ")
        sql = """insert into owners
               (owner_id, name, age, address,
                     experience_in_raise, did_pre_training,
                     monthly_income, report_date, phone_number)
               values
               (owners_seq.nextval, :name, :age, :address,
                :experience_in_raise, :did_pre_training,
                :monthly_income, to_date(:report_date, 'rr/MM/DD'),
                :phone_number)"""

        cursor.execute(sql,
                       (name, age, address,
                        experience_in_raise, did_pre_training,
                        monthly_income, report_date, phone_number))
        print("정보가 입력되었습니다")

    # TODO: 디버깅용이니 꼭 시연 전에 삭제할 것
    # cx_Oracle.Error / print(e.args)
    except cx_Oracle.Error as e:
        errorObj, = e.args
        print()
        print(errorObj.message)
        return
    except Exception as e:
        print()
        print(e.args)
        print("올바르지 않은 입력값입니다")
        return


def update(conn):
    cursor = conn.cursor()
    try:
        owner_id = int(input("수정할 양육자 id: "))
        sql_find_id = """
            select owner_id
            from owners
            where owner_id=:owner_id
        """
        cursor.execute(sql_find_id, (owner_id,))
        cursor.fetchall()
        if cursor.rowcount == 0:
            print(cursor.rowcount)
            raise Exception("id is not exist")

        print("<", "-"*105, ">", sep="")
        print("성명->name, 나이->age, 주소지->address, 양육 경력->experience_in_raise,",
              " 사전교육 이수 여부->did_pre_training\n",
              "월 수입(단위: 만)->monthly_income, 정기신고일->report_date\n",
              "전화번호->phone_number", sep="")
        print("<", "-"*105, ">", sep="")
        update_title = input("수정할 항목을 입력하세요: ")
        update_data = input("수정할 내용을 입력하세요: ")
        if update_title == 'report_date':
            sql = f"""
                update owners
                set {update_title} = to_date(:update_data, 'rr/MM/DD')
                where owner_id = :owner_id
            """
            cursor.execute(sql, (update_data, owner_id))
            print("정보가 수정되었습니다")
        else:
            sql = f"""
                update owners
                set {update_title} = :update_data
                where owner_id = :owner_id
            """
            cursor.execute(sql, (update_data, owner_id))
            print("정보가 수정되었습니다")

    # TODO: 디버깅용이니 꼭 시연 전에 삭제할 것
    # cx_Oracle.Error / print(e.args)
    except cx_Oracle.Error as e:
        errorObj, = e.args
        print()
        print(errorObj.message)
        return
    except Exception as e:
        print()
        print(e.args)
        print("올바르지 않은 입력값입니다")
        return


def get_owner_by_name(conn):
    name = input("이름: ")
    cursor = conn.cursor()
    sql = f"""
        select owner_id, name, age, address,
               experience_in_raise, did_pre_training,
               monthly_income, to_char(report_date, 'yyyy-MM-DD'),
               phone_number
        from owners
        where name like '%{name}%'
    """
    cursor.execute(sql)

    for data in cursor:
        owner = owners.Owner(*data)
        print()
        print(f"| {data[0]} |")
        print(owner)

def get_owners(conn):
    cursor = conn.cursor()
    sql = """
        select owner_id, name, age, address,
               experience_in_raise, did_pre_training,
               monthly_income, to_char(report_date, 'yyyy-MM-DD'),
               phone_number
        from owners
    """
    cursor.execute(sql)
    for data in cursor:
        owner = owners.Owner(*data)
        print()
        print(f"| {data[0]} |")
        print(owner)


def get_owner_by_pet(conn):
    cursor = conn.cursor()
    pid = int(input("반려동물 id: "))
    if pid == 0:
        return
    sql = """
        select o.owner_id, o.name, o.age, address,
               experience_in_raise, did_pre_training,
               monthly_income, to_char(report_date, 'yyyy-MM-DD'),
               phone_number, p.pid
        from owners o
        join pets p
        on o.owner_id = p.owner_id
        where p.pid = :pid
        """
    cursor.execute(sql, (pid,))
    for data in cursor:
        owner = owners.Owner(*data)
        print()
        print(f"| {data[0]} |")
        print(owner)


def delete(conn):
    cursor = conn.cursor()
    try:
        owner_id = int(input("양육자 id: "))
        sql = """
            delete from owners
            where owner_id = :owner_id
        """
        cursor.execute(sql, (owner_id,))
        print("정보가 삭제되었습니다")
    except cx_Oracle.Error as e:
        errorObj, = e.args
        print(errorObj.message)
        return
    except Exception as e:
        print(e.args)
        return


def make_csv(conn):
    cursor = conn.cursor()
    sql = """
        select o.owner_id, o.name, o.age, address,
               experience_in_raise, did_pre_training,
               monthly_income, to_char(report_date, 'yyyy-MM-DD') as report_date,
               phone_number, p.pid, p.name
        from owners o
        left outer join pets p
        on o.owner_id = p.owner_id
    """
    cursor.execute(sql)
    now = localtime()
    str_ = 'owners_' + strftime('%Y-%m-%d_%H-%M', now) + '.csv'
    with open(str_, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['owner_id', 'owner_name', 'age', 'address',
                      'experience_in_raise', 'did_pre_training',
                      'monthly_income', 'report_date', 'phone_number', 'pid', 'pet_name']
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_writer.writeheader()
        for data in cursor:
            owner = owners.Owner(*data)
            dict_writer.writerow(owner.to_dict())
    print("csv 파일이 생성되었습니다")
