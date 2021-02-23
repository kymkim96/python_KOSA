class Pet:
    def __init__(self, pid, name, species, kind,
                 weight, age, height, birth,
                 adopt_date, neutered, owner_id, oname=None, opnumber=None):
        self.pid = pid
        self.name = name
        self.species = species  # 종
        self.kind = kind    # 품종
        self.owner_id = owner_id
        self.weight = weight
        self.age = age
        self.height = height
        self.birth = birth  # 출생연도
        self.adopt_date = adopt_date    # 입양 날짜
        self.neutered = neutered    # 중성화 수술 여부
        self.oname = oname
        self.opnumber = opnumber

    def __str__(self):
        return "이름: {}, 종: {}, 품종: {}, 체중: {}, 나이: {},\n신장: {}, 출생일: {}, " \
               "입양날짜: {}, 중성화 수술 여부: {}"\
            .format(self.name, self.species, self.kind, self.weight, self.age,
                    self.height, self.birth, self.adopt_date, self.neutered)

    def to_dict(self):
        return {"pid": self.pid, "pet_name": self.name, "species": self.species, "kind": self.kind,
                "weight": self.weight, "age": self.age, "height": self.height, "birth": self.birth,
                "adopt_date": self.adopt_date, "neutered": self.neutered, "owner_id": self.owner_id,
                "owner_name": self.oname, "owner_phone_number": self.opnumber}