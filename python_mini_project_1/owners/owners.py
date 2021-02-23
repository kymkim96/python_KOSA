class Owner:
    def __init__(self, owner_id, name, age, address,
                 experience_in_raise, did_pre_training,
                 monthly_income, report_date):
        self.owner_id = owner_id
        self.name = name
        self.age = age
        self.address = address
        self.experience_in_raise = experience_in_raise  # 양육 경력 varchar2(30)
        self.did_pre_training = did_pre_training    # 사전교육 이수 여부 char(1)
        self.monthly_income = monthly_income    # 월 수입(단위: 천) number(7)
        # 현재 양육 중인지 정기적으로 신고하고 날짜를 기록
        # 주기는 1년
        self.report_date = report_date

    def __str__(self):
        return "name: {}, age: {}, address: {}, experience_in_raise: {}, did_pre_training: {}," \
               " monthly_income: {}, report_date: {}"\
            .format(self.name, self.age, self.address, self.experience_in_raise,
                    self.did_pre_training, self.monthly_income, self.report_date, self.birth, self.adopt_date)

    def to_dict(self):
        return {"name": self.name, "monthly_income": self.monthly_income, "address": self.address, "experience_in_raise": self.experience_in_raise,
                "did_pre_training": self.did_pre_training, "monthly_income": self.monthly_income, "report_date": self.report_date}