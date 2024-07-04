import json


class Database:
    def __init__(self, name, keys: list[str]):
        self.name = f"{name}.json"
        self.keys = keys
        try:
            with open(self.name, "r") as json_file:
                self.dict = json.load(json_file)
        except FileNotFoundError:
            self.new_file()
            with open(self.name, "r") as json_file:
                self.dict = json.load(json_file)

    def check(self, pk):
        return pk in self.dict

    def new_file(self):
        with open(self.name, "w") as json_file:
            json.dump({}, json_file)

    def create(self, inf):
        if not self.check(inf[0]):
            self.dict[inf[0]] = dict(self.connect_keys(inf))
            self.save()
        else:
            raise ValueError("Record exists")

    def update(self, inf):
        if self.check(inf[0]):
            self.dict[inf[0]] = dict(self.connect_keys(inf))
            self.save()
        else:
            raise ValueError("Record not found")

    def read(self, pk):
        if self.check(pk):
            return self.dict[pk]
        raise ValueError("Record not found")

    def connect_keys(self, values):
        connected_list = []
        for i in range(1, len(self.keys)):
            connected_list.append((self.keys[i], values[i]))
        return connected_list

    def save(self):
        with open(self.name, "w") as json_file:
            json.dump(self.dict, json_file, indent=3)


cars_db = Database("cars", ["number-plate", "car-make", "model", "release-date"])
# cars_db.create(["kz-374vaz-01", "BMW", "M5 Competition", "2017"])
# cars_db.create(["kz-001AAA-02", "Mercedes", "GT 63 S", "2018"])
# cars_db.create(["kz-577ASA-14", "Range Rover", "Sport L494", "2022"])
# cars_db.save()
# print(cars_db.dict)
# cars_db.json_file()
# print(cars_db.read("kz-577ASA-14"))


player_db = Database("players", ["PlayerID", "satiety", "money", "happiness", "health"])
# player_db.create(["User1", 100, 10000, 100, 100])
player_db.update(["User1", 60, 10000, 100, 100])
# player_db.save()
# print(player_db.read("User1"))
# print(player_db.make_dict())
