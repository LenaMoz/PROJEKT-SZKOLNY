import sys
import time

def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

#---------------------------------------
class Character:
    def __init__(self):
        self.name = input("podaj imie: ")
        self.max_hp = 100
        self.max_stamina = 50
        self.current_hp = 100
        self.stamina = 30
        self.yourattack = 2


    def take_damage(self, damage_amount):
        self.current_hp -= damage_amount
        if self.current_hp <= 0:
            animate_text(f"{self.name}, nie żyjesz\n")
            sys.exit(0)


    def gain_stamina(self, stamina):
        self.stamina += stamina
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina

    def no_stamina(self, stamina):
        self.stamina -= stamina
        if self.stamina < 0:
            self.stamina = 0

    def heal(self, heal_amount):
        self.current_hp += heal_amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def do_attack(self, attack):
        self.yourattack += attack

player = Character()
#---------------------------------------
class Matka:
    def __init__(self):
        self.Mmax_hp = 10
        self.Mcurrent_hp = 10
        self.Mherattack = 5

    def take_damage(self, Mdamage_amount):
        self.Mcurrent_hp -= Mdamage_amount
        if self.Mcurrent_hp <= 0:
            animate_text("Pokonałeś ją!\n")
        else:
            animate_text(f"Matka jeszcze zyje.\n")

mother = Matka()
#---------------------------------
class Potwor:
    def __init__(self):
        self.pmax_hp = 20
        self.pcurrent_hp = 20
        self.pherattack = 5

    def take_damage(self, pdamage_amount):
        self.pcurrent_hp -= pdamage_amount
        if self.pcurrent_hp <= 0:
            animate_text("Pokonałeś to!\n")
        else:
            animate_text(f"to coś jeszcze zyje.\n")

potwor = Potwor()
#-------------------------------------------------
class Potwor2:
    def __init__(self):
        self.p2max_hp = 10
        self.p2current_hp = 10
        self.p2herattack = 2

    def take_damage(self, p2damage_amount):
        self.p2current_hp -= p2damage_amount
        if self.p2current_hp <= 0:
            animate_text("Pokonałeś to!\n")
        else:
            animate_text(f"to coś jeszcze zyje.\n")

potwor2 = Potwor2()
