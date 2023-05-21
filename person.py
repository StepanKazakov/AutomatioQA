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

    def update_weight(self, kg):
        self.weight = kg

class Warrior(Person):
    
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.rage = 100

    def description_person(self):
        description = self.name + ', age: ' + str(self.age) + ', rage: ' + str(self.rage)
        return description

warrior = Warrior('Konan', 32, 200)
print('Warrior name: ' + warrior.description_person())

man = Person('Mad Max', 33, 190)
man.update_weight(75)
man.description_person()