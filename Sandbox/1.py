class Human:
    age: int
    firstname: str
    lastname: str
    weight: float

    counter: int = 0

    def __init__(self, firstname, lastname, age, weight=0):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.weight = weight

        Human.counter += 1

    def info(self):
        print(f"I am {self.firstname}")


john = Human("John", "Due", 30)
arthur = Human("Arthur", "Due", 30)

print(Human.counter)
