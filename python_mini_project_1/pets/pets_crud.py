from pets import pets
import cx_Oracle
import csv
from time import strftime, localtime

def insert(conn):
    cursor = conn.cursor()
    try:
        name = input("이름: ")
        species = input("종: ")
        kind = input("품종: ")
        owner_id = input("양육자 id: ")
        weight = float(input("체중: "))
        age = int(input("나이: "))
        height = float(input("신장: "))
        birth = input("출생일: ")
        adopt_date = input("입양 날짜: ")
        neutered = input("중성화 수술 여부: ")
        sql = """insert into pets
           (pid, name, species, kind, owner_id, weight, age,
            height, birth, adopt_date, neutered)
           values
           (pet_seq.nextval, :name, :species, :kind, :owner_id, :weight, :age,
            :height, to_date(:birth, 'rr/MM/DD'), to_date(:adopt_date, 'rr/MM/DD'), :neutered)"""
        if owner_id == '':
            owner_id = None
        else:
            owner_id = int(owner_id)

        cursor.execute(sql,
                       (name, species, kind, owner_id, weight, age,
                        height, birth, adopt_date, neutered))
        print()
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
        pet_id = int(input("수정할 반려동물 id: "))
        sql_find_id = """
            select pid
            from pets
            where pid=:pet_id
        """
        cursor.execute(sql_find_id, (pet_id,))
        cursor.fetchall()
        if cursor.rowcount == 0:
            raise Exception("id is not exist")
        print()
        print("<---------------------------------------------------->")
        print("이름->name, 종->species, 품종->kind, 양육자->owner_id")
        print("체중->weight, 나이->age, 신장->height, 출생일->birth")
        print("입양날짜->adopt_date, 중성화 수술 여부->neutered")
        print("<---------------------------------------------------->")
        print()
        update_title = input("수정할 항목을 입력하세요: ")
        update_data = input("수정할 내용을 입력하세요: ")
        if (update_title == 'adopt_date') | (update_title == 'birth'):
            sql = f"""
                update pets
                set {update_title} = to_date(:update_data, 'rr/MM/DD')
                where pid = :pid
            """
            cursor.execute(sql, (update_data, pet_id))
            print()
            print("정보가 수정되었습니다")
        else:
            sql = f"""
                update pets
                set {update_title} = :update_data
                where pid = :pid
            """
            cursor.execute(sql, (update_data, pet_id))
            print()
            print("정보가 수정되었습니다")

    # TODO: 디버깅용이니 꼭 시연 전에 삭제할 것
    # cx_Oracle.Error / print(e.args)
    except cx_Oracle.Error as e:
        errorObj, = e.args
        print(errorObj.message)
        return
    except Exception as e:
        print(e.args)
        print("올바르지 않은 입력값입니다")
        return


def get_pet_by_name(conn):
    print()
    name = input("이름: ")
    cursor = conn.cursor()
    sql = f"""
        select pid, name, species, kind, weight, age,
               height, to_char(birth, 'yyyy-MM-DD'), to_char(adopt_date, 'yyyy-MM-DD'), neutered,
               owner_id
        from pets
        where name like '%{name}%'
    """
    cursor.execute(sql)
    for data in cursor:
        pet = pets.Pet(*data)
        print()
        print(f"| {data[0]} |")
        print(pet)


def get_pets(conn):
    cursor = conn.cursor()
    sql = """
        select pid, name, species, kind, weight, age,
               height, to_char(birth, 'yyyy-MM-DD'), to_char(adopt_date, 'yyyy-MM-DD'), neutered,
               owner_id
        from pets
    """
    cursor.execute(sql)
    for data in cursor:
        pet = pets.Pet(*data)
        print()
        print(f"| {data[0]} |")
        print(pet)


def get_pets_by_owner(conn):
    cursor = conn.cursor()
    owner_id = int(input("양육자 id: "))
    sql = """
        select pid, name, species, kind, weight, age,
               height, to_char(birth, 'yyyy-MM-DD'), to_char(adopt_date, 'yyyy-MM-DD'), neutered,
               owner_id
        from pets
        where owner_id = :owner_id
    """
    cursor.execute(sql, (owner_id,))
    for data in cursor:
        pet = pets.Pet(*data)
        print()
        print(f"| {data[0]} |")
        print(pet)


def delete(conn):
    cursor = conn.cursor()
    try:
        pid = int(input("반려동물 id: "))
        sql_find_id = """
                    select pid
                    from pets
                    where pid=:pid
                """
        cursor.execute(sql_find_id, (pid,))
        cursor.fetchall()
        if cursor.rowcount == 0:
            raise Exception("id is not exist")

        sql = """
            delete from pets
            where pid = :pid
        """
        cursor.execute(sql, (pid,))
        print()
        print("정보가 삭제되었습니다")
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


def make_csv(conn):
    cursor = conn.cursor()
    sql = """
        select pid, p.name, species, kind, weight, p.age,
               height, to_char(birth, 'yyyy-MM-DD') as birth,
               to_char(adopt_date, 'yyyy-MM-DD') as adopt_date, neutered,
               p.owner_id, o.name, o.phone_number
        from pets p
        left outer join owners o
        on o.owner_id = p.owner_id
    """
    cursor.execute(sql)
    now = localtime()
    str_ = 'pets_' + strftime('%Y-%m-%d_%H%M', now) + '.csv'
    with open(str_, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['pid', 'pet_name', 'species', 'kind',
                      'weight', 'age', 'height', 'birth', 'adopt_date',
                      'neutered', 'owner_id', 'owner_name',
                      'owner_phone_number']
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_writer.writeheader()
        for data in cursor:
            pet = pets.Pet(*data)
            dict_writer.writerow(pet.to_dict())
    print()
    print("csv 파일이 생성되었습니다")