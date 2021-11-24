import random


class Soldier:
    hp = 100

    def __init__(self, name):
        self.name = name

    def kick(self, enemy):
        enemy.hp -= 20
        print(f"{self.name} бьет {enemy.name}")


class Battle:
    def __init__(self, u1, u2):
        while u1.hp > 0 and u2.hp > 0:
            if random.randint(1, 2) == 1:
                u1.kick(u2)
            else:
                u2.kick(u1)
        if u1.hp > u2.hp:
            print(f"Победил {u1.name}")
        else:
            print(f"Победил {u2.name}")


first = Soldier("Ivan")
second = Soldier("Petr")

round_1 = Battle(first, second)

print(first.hp, second.hp)
print(Soldier.hp)
