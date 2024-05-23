from mc import MainCharacter
print("Promienie słońca wpadły przez odsłonięte okno prosto na twoją twarz.")
print("Powoli otworzyłeś oczy i przeciągnąłeś się.")
print("Twoją uwagę zwrócił fakt, iż było aż zbyt cicho.")
print("Co było dziwne biorąc pod uwagę, że zazwyczaj w sobotę dziaciaki sąsiadów już jeździły po osiedlu")
print("*Która jest godzina?*")
print("Sięgnąłeś po telefon. Wyświetlacz pokazywał godzinę 9:30.")
print("*Dziwne... Zazwyczaj już by ktoś mnie siłą zrzucił z łóżka*")
#decyzja: zawołaj lub wstań
def wybierz_odp1():
    print("a/A - Zawołaj")
    print("b/B - Wstań")
    odp1 = input().upper()
    if odp1 == "A":
        print("*Mamo?*")
        print("Brak jakiej kolwiek odpowiedzi na twoje wołanie.")
        print("*Hm... Może wyszła na zakupy.*")
    if odp1 == "B":
        return 0
    else:
        return 0
odp1 = wybierz_odp1()
print("Wstałeś z łóżka i podeszłeś do drzwi. Wyjrzałeś na korytarz.")
print("Jest cicho i pusto")
#decyzja: wyjdź z pokoju lub ubierz się zanim wyjdziesz

def wybierz_odp2():
    print("a/A - Wyjdź z pokoju")
    print("b/B - Przebierz się zanim wyjdziesz")
    odp2 = input().upper()
    if odp2 == "A":
        return 0
    if odp2 == "B":
        print("przebrałeś się w wygodnie ubrania, +5 do staminy")
        #:c
        def gain_stamina(self, stamina):
            self.stamina += 5
            if self.stamina > self.max_stamina:
                self.stamina = self.max_stamina
    else:
        return 0
odp2 = wybierz_odp2()

print("wyszedłeś z pokoju by rozejrzec się czy ktoś jest jeszcze w domu")
print("*huh? mamy rzeczy dalej są. Ale gdzie ona jest?*")

