-- �ݷ����� ������
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '����1', '��', '������', 3, 12.1, 2,
       100.1, '19/02/22', '19/02/30', '0');
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '����2', '��', '�ù�', 3, 8.2, 5,
       50.0, '14/07/01', '15/02/10', '1');
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '����3', '�����', '��ġŲ', 4, 5.2, 12,
       30.2, '08/04/19', '10/08/12', '1');
insert into pets
       (pid, name, species, kind, owner_id, weight, age,
       height, birth, adopt_date, neutered)
       values
       (pet_seq.nextval, '����4', '�ܽ���', '��', 5, 0.2, 0,
       7.3, '21/02/01', '21/02/01', '0');
       
-- ������ ������       
insert into owners
       (owner_id, name, age, address,
             experience_in_raise, did_pre_training,
             monthly_income, report_date, phone_number)
       values
       (owners_seq.nextval, '����1', 20, '��õ',
        '1�� 6����', 1, 200, '20/06/02', '010-1111-1111');
insert into owners
       (owner_id, name, age, address,
             experience_in_raise, did_pre_training,
             monthly_income, report_date, phone_number)
       values
       (owners_seq.nextval, '����2', 25, '����',
        '18�� 1����', 0, 300, '19/06/07', '010-2222-2222');
insert into owners
       (owner_id, name, age, address,
             experience_in_raise, did_pre_training,
             monthly_income, report_date, phone_number)
       values
       (owners_seq.nextval, '����3', 43, '�λ�',
        '30�� 3����', 0, 700, '21/01/01', '010-3333-3333');
        
commit;