def print_menu():
    print("------------------------------------------------------------")
    print("                   반려동물 관리 시스템")
    print("------------------------------------------------------------")
    print("1. 반려동물 정보 관리", "2. 양육자 정보 관리", "0: 종료", sep=" | ")
    menu = int(input("메뉴 선택: "))
    return menu


def print_menu_pet():
    print()
    print()
    print("------------------------------------------------------------")
    print("                   반려동물 관리 시스템")
    print("                    반려동물 정보 관리")
    print("------------------------------------------------------------")
    print("1. 반려동물 정보 등록", "2. 반려동물 정보 수정", "3. 반려동물 정보 삭제"
          , sep=" | ")
    print("4. 반려동물 전체 목록 조회", "5. 반려동물 개별 조회", "6. 양육자의 반려동물 찾기",
          sep=" | ")
    print("7. 내보내기(CSV)")
    print("0: 종료")
    menu = int(input("메뉴 선택: "))
    return menu


def print_menu_owner():
    print()
    print()
    print("------------------------------------------------------------")
    print("                   반려동물 관리 시스템")
    print("                     양육자 정보 관리")
    print("------------------------------------------------------------")
    print("1. 양육자 정보 등록", "2. 양육자 정보 수정", "3. 양육자 정보 삭제"
          , sep=" | ")
    print("4. 양육자 전체 목록 조회", "5. 양육자 개별 조회", "6. 반려동물의 양육자 찾기",
          sep=" | ")
    print("7. 내보내기(CSV)")
    print("0: 종료")
    menu = int(input("메뉴 선택: "))
    return menu
