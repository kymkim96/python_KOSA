import cx_Oracle
from view import ui
from owners import owners_crud
from pets import pets_crud


def main():
    while True:
        menu = ui.print_menu()
        # 반려동물 정보 관리
        if menu == 1:
            while True:
                menu_pet = ui.print_menu_pet()
                if menu_pet == 1:
                    pets_crud.insert(conn)
                    conn.commit()
                elif menu_pet == 2:
                    pets_crud.update(conn)
                    conn.commit()
                elif menu_pet == 3:
                    pets_crud.delete(conn)
                    conn.commit()
                elif menu_pet == 4:
                    pets_crud.get_pets(conn)
                elif menu_pet == 5:
                    pets_crud.get_pet_by_name(conn)
                elif menu_pet == 6:
                    pets_crud.get_pets_by_owner(conn)
                elif menu_pet == 7:
                    pets_crud.make_csv(conn)
                elif menu_pet == 0:
                    break
        # 양육자 정보 관리
        elif menu == 2:
            while True:
                menu_owner = ui.print_menu_owner()
                if menu_owner == 1:
                    owners_crud.insert(conn)
                    conn.commit()
                elif menu_owner == 2:
                    owners_crud.update(conn)
                    conn.commit()
                elif menu_owner == 3:
                    owners_crud.delete(conn)
                    conn.commit()
                elif menu_owner == 4:
                    owners_crud.get_owners(conn)
                elif menu_owner == 5:
                    owners_crud.get_owner_by_name(conn)
                elif menu_owner == 6:
                    owners_crud.get_owner_by_pet(conn)
                elif menu_owner == 7:
                    owners_crud.make_csv(conn)
                elif menu_owner == 0:
                    break
        elif menu == 0:
            break


oracle_dsn = cx_Oracle.makedsn("localhost", 1521, sid="xe")
# cx_Oracle.init_oracle_client(lib_dir=r"C:/oracle/instantclient_19_9")

if __name__ == '__main__':
    global conn
    conn = cx_Oracle.connect(dsn=oracle_dsn, user="hr", password="123456")
    main()
