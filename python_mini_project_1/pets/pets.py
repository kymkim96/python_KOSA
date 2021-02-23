class Pet:
    def __init__(self, pid, name, species, kind,
                 owner_id, weight, age, height, birth,
                 adopt_date, neutered):
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

    def __str__(self):
        return "name: {}, species: {}, kind: {}, owner_id: {}, weight: {}, age: {}, height: {}, birth: {}" \
               "adopt_date: {}"\
            .format(self.name, self.species, self.kind, self.owner_id,
                    self.weight, self.age, self.height, self.birth, self.adopt_date)

    def to_dict(self):
        return {"name": self.name, "species": self.species, "kind": self.kind, "owner_id": self.owner_id,
                "weight": self.weight, "age": self.age, "height": self.height, "birth": self.birth,
                "adopt_date": self.adopt_date}