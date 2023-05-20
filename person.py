class Person():
    # human model

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 80

    def description_person(self):
        description = self.name + ', age: ' + str(self.age) + ', ' + str(self.weight) + ' kg, ' + str(self.height) + ' cm.'
        print(description)

    def sing(self):
        print(self.name + ' singing')

    def dance(self):
        print(self.name + ' dancing')

    def update_weight(self, kg):
        self.weight = kg


man = Person('Max', 33, 190)
man.update_weight(75)

man.description_person()