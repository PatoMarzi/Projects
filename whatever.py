import random


class Player:
    #
    def __init__(self, hp, atk, deff):
        self.hp = hp
        self.atk = atk
        self.deff = deff

    # Special power increases atk by 10
    def powerUp(self):
        self.atk += 10

    # Attacks the enemy causing them damage
    def attack(self, Enemy):
        return Enemy.hp - self.atk

    # Absorbs dmg as a percentage
    def defense(self, dmg):
        self.hp = self.hp - dmg * (self.deff / 100)

    def __str__(self):
        return f"Patrick"


class Enemy(Player):
    def __init__(self, hp, atk, deff):
        super().__init__(hp, atk, deff)

    def __str__(self):
        return f"Creep, {self.hp}"


jugador = Player(100, 30, 20)
creeps = []

for i in range(10):
    creeps.append(Enemy(10, 10, 10))


def fight(pos):
    while (creeps[pos].hp > 0) and (jugador.hp > 0):
        print(
            f"{jugador.__str__()} is attacking a wild creature with {creeps[pos].hp} max health"
        )
        creeps[pos].hp = creeps[pos].hp - jugador.atk * creeps[pos].deff / 100
        if creeps[pos].hp > 0:
            print(f"{creeps[pos]} is retaliating!")
            jugador.hp = jugador.hp - creeps[pos].atk * jugador.deff / 100
            print(f"{jugador.__str__()}'s HP is now {jugador.hp}")

    if jugador.hp > 0:
        print("Jugador defeated the creep!")
        del creeps[pos]
    elif jugador.hp < 0 and creeps[pos].hp < 0:
        print("Jugador and creep died")
        del creeps[pos]
    else:
        print("Jugador died")


while (jugador.hp > 0) and (len(creeps) >= 1):
    fight(random.randint(0, len(creeps) - 1))
    print(f"\nRemaining creeps: {len(creeps)}\n")

    if len(creeps) == 0:
        print(f"{jugador.__str__()} has defeated all the creeps. YOU WIN!")
