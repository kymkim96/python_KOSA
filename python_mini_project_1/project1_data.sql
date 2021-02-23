-- 반려동물 데이터
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '동물1', '개', '진돗개', 3, 12.1, 2,
       100.1, '19/02/22', '19/02/30', '0');
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '동물2', '개', '시바', 3, 8.2, 5,
       50.0, '14/07/01', '15/02/10', '1');
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '동물3', '고양이', '먼치킨', 4, 5.2, 12,
       30.2, '08/04/19', '10/08/12', '1');
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '동물4', '햄스터', '펄', 5, 0.2, 0,
       7.3, '21/02/01', '21/02/01', '0');
       
-- 양육자 데이터       
insert into owners
       (owner_id, name, age, address,
             experience_in_raise, did_pre_training,
             monthly_income, report_date, phone_number)
       values
       (owners_seq.nextval, '주인1', 20, '인천',
        '1년 6개월', 1, 200, '20/06/02', '010-1111-1111');
insert into owners
       (owner_id, name, age, address,
             experience_in_raise, did_pre_training,
             monthly_income, report_date, phone_number)
       values
       (owners_seq.nextval, '주인2', 25, '서울',
        '18년 1개월', 0, 300, '19/06/07', '010-2222-2222');
insert into owners
       (owner_id, name, age, address,
             experience_in_raise, did_pre_training,
             monthly_income, report_date, phone_number)
       values
       (owners_seq.nextval, '주인3', 43, '부산',
        '30년 3개월', 0, 700, '21/01/01', '010-3333-3333');
        
commit;