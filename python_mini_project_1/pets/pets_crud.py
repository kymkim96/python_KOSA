from pets import pets
import cx_Oracle


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
        birth = input("출생연도: ")
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
