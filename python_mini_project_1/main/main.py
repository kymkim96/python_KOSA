import cx_Oracle
import ui
from owners import owners_crud
from pets import pets_crud


def main():
    while True:
        menu = ui.print_menu()
        if menu == 1:
            pets_crud.insert(conn)
            conn.commit()
        elif menu == 2:
            owners_crud.insert(conn)
            conn.commit()
        elif menu == 3:
            while True:
                menu_pet = ui.print_menu_pet()
                if menu_pet == 1:
                    pass
                elif menu_pet == 2:
                    pass
                elif menu_pet == 0:
                    break
        elif menu == 4:
            while True:
                menu_owner = ui.print_menu_owner()
                if menu_owner == 1:
                    pass
                elif menu_owner == 2:
                    pass
                elif menu_owner == 0:
                    break
        elif menu == 5:
            pass
        elif menu == 6:
            pass
        elif menu == 7:
            pass
        elif menu == 8:
            pass
        elif menu == 0:
            break


oracle_dsn = cx_Oracle.makedsn("localhost", 1521, sid="xe")
cx_Oracle.init_oracle_client(lib_dir=r"C:/oracle/instantclient_19_9")

if __name__ == '__main__':
    global conn
    conn = cx_Oracle.connect(dsn=oracle_dsn, user="hr", password="123456")
    main()
