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
        self.Mmax_hp = 50
        self.Mcurrent_hp = 50
        self.Mherattack = 10

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
        self.pmax_hp = 50
        self.pcurrent_hp = 50
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
#---------------------------------
animate_text("Promienie słońca wpadły przez odsłonięte okno prosto na twoją twarz. \n")
animate_text("Powoli otworzyłeś oczy i przeciągnąłeś się.\n ")
animate_text("Twoją uwagę zwrócił fakt, iż było aż zbyt cicho. \n")
animate_text("Co było dziwne biorąc pod uwagę, że zazwyczaj w sobotę dziaciaki sąsiadów już jeździły po osiedlu\n ")
animate_text("*Która jest godzina?*\n ")
animate_text("Sięgnąłeś po telefon. Wyświetlacz pokazywał godzinę 9:30. \n")
animate_text("*Dziwne... Zazwyczaj już by ktoś mnie siłą zrzucił z łóżka* \n")
#------------------------------------
def wybierz_odp1():
    animate_text("a/A - Zawołaj ")
    animate_text("b/B - Wstań z łóżka ")
    odp1 = input().upper()
    if odp1 == "A":
        animate_text("*Mamo?*\n ")
        animate_text("Brak jakiej kolwiek odpowiedzi na twoje wołanie. \n")
        animate_text("*Hm... Może wyszła na zakupy.* \n")
    if odp1 == "B":
        return 0
    else:
        return 0
odp1 = wybierz_odp1()
animate_text("Wstałeś z łóżka i podeszłeś do drzwi. Wyjrzałeś na korytarz. \n")
animate_text("Jest cicho i pusto ")
#_----------------------------------------------------
def wybierz_odp2():
    animate_text("a/A - Wyjdź z pokoju\n ")
    animate_text("b/B - Przebierz się zanim wyjdziesz\n ")
    odp2 = input().upper()
    if odp2 == "A":
        return 0
    if odp2 == "B":
        animate_text("przebrałeś się w wygodnie ubrania, +5 do staminy\n ")
        animate_text("Zauważyłeś że w szafie są ubrania które wczoraj wieczorem rzuciłeś do prania,\n")
        animate_text("NIemożliwe że przez noc ktokolwiek zrobił pranie,\n")
        player.gain_stamina(5)
    else:
        return 0
odp2 = wybierz_odp2()
#-------------------------------------------------------------
animate_text("wyszedłeś z pokoju by rozejrzec się czy ktoś jest jeszcze w domu \n")
animate_text("*huh? Mamy rzeczy dalej są. Ale gdzie ona jest?*\n ")
animate_text("Zszedłeś myśląc, że spotkasz tam swoją mame\n ")
animate_text("Jednak to co zobaczyłeś to niewyglądało zupełnie jak twoja mama \n")
#----------------------------------------------------------
def choose_attack():
    animate_text('a/A - Rzuć w nią krzesło \n')
    animate_text('b/B - Przyglądaj się dalej\n ')
    co = input().upper()
    if co == 'A':
        animate_text("Ten potwór się cofnął, co daje ci więcej czasu,\n ")
        def wybierz_odp2():
            animate_text("a/A - Uciekaj\n ")
            animate_text("b/B - *może jest cośco by pozbyłoby się tego na stałe?\n")
            odp2 = input().upper()
            if odp2 == "A":
                return 0
            elif odp2 =='B':
                animate_text("NAwet nie wiem co jest z tobą nie tak, \n")
                animate_text("'mama' nie daje ci jakoś wiecej czasu ale jednak wystarczająco by jakoś si wymigać,\n")
                animate_text("Jednakże  udało się jej zadrapać jakoś noge, (-2hp)\n")
                player.take_damage(2)
            else:
                animate_text("Co tak stoisz? (-10hp) \n")
                player.take_damage(mother.Mherattack)
            odp2 = wybierz_odp2()
    elif co == 'B':
        animate_text("To coś co miało być twoją mamą zadaje ci obrażenia (-10hp)\n ")
        player.take_damage(mother.Mherattack)
    else:
        animate_text("You lose a turn ")
        return 0
attack = choose_attack()
animate_text("Udało ci się jakimś cudem uciec do garażu, tylko co teraz?\n ")
#_----------------------------------------------------------------------
def wybierz_odp5():
    animate_text("a/A - Rozglądaj się po przydatne rzeczy ")
    animate_text("b/B - Przemyśl sytuacje ")
    odp5 = input().upper()
    if odp5 == "A":
        animate_text(" W garażu znajdujesz wiele dobrych rzeczy, ale z wszystkimi trudno się zabrać.\n ")
        def wybierz_bron():
            animate_text("a - Grabie, wyglądają na ciężkie ale są ostre.\n ")
            animate_text("b - Stare buty ojca. Twój rozmiar oraz są świetne do biegania, aż przypominając ci się stare czasy.\n ")
            animate_text("c - Młotek, trochę cieżki ale poręczny. \n")
            animate_text("d - Piła mechaniczna. Działa ale jest bardzo ciężka. \n")
            animate_text("e - Nic nie bierzesz.")
            odp7 = input().upper()
            if odp7 == 'A':
                animate_text("Bierzesz grabie, są cieżkie więc tylko je. (+5 attack, -2 stamina)\n")
                player.do_attack(5)
                player.no_stamina(2)
            elif odp7 == 'B':
                animate_text("Pasują idealnie i są wygodne (+5 stamina),\n")
                player.gain_stamina(5)
            elif odp7 == "C":
                animate_text("Młotek to dobra sprawa.(+2 attacku)\n")
                player.do_attack(2)
            elif odp7 == 'D':
                animate_text("Bardzo ciężka, trudno się z nią chodzi. (-10staminy, +10 attaku)\n")
                player.do_attack(10)
                player.no_stamina(10)
            else:
                animate_text("Nic nie wybrałeś, to teraz powodzenia\n")
                return 0
        odp7 = wybierz_bron()
    if odp5 == "B":
        animate_text("*Co się do diabła dzieje?! Co to było? Czy to naprawdę była moja Mama?* \n")
        animate_text("Rozmyślasz całą sytuację, ale czy coś ci to daje?\n ")
    else:
        animate_text("szkoda że skipnołeś, A te opcje akurat miały znaczenie..\n ")
        return 0
odp5 = wybierz_odp5()
#_----------------------------------------------------------------
animate_text("Wyglądasz przez okno, ale nie ma ani jedenj żywej duszy.\n ")
animate_text("Słyszysz walenie w drzwi od garażu, odwracasz się. \n")
animate_text("W tym samym momencie drzwi od garażu odpadają i wchodzi 'mama' \n")
animate_text("Rozgladasz sie szybko czy jest jak uciec , no tak mozesz przez okno. \n")
animate_text("Jednakże nie masz czasu, bo 'mama' już na ciebie biegnie\n")
animate_text("Pozostało ci się z nią walczyć. \n")
animate_text("Niepowinno to być trudne, prawda? \n")
#-----------------------------------------
def attack_mother():
    if player.yourattack >= mother.Mcurrent_hp:
        animate_text(f"Zadałeś matce {mother.Mcurrent_hp} obrażeń i pokonałeś ją!\n")
        mother.take_damage(mother.Mcurrent_hp)  
    else:
        animate_text(f"Zadałeś matce {player.yourattack} obrażeń!\n")
        mother.take_damage(player.yourattack) 

#--Symulacja walki
while player.current_hp > 0 and mother.Mcurrent_hp > 0:
    attack_mother()
    if mother.Mcurrent_hp <= 0:
        break 

    player.take_damage(mother.Mherattack)
    if player.current_hp <= 0:
        break  

if player.current_hp <= 0:
    animate_text(f"{player.name}, przegrałeś!")
    sys.exit(0)
elif mother.Mcurrent_hp <= 0:
    animate_text(f"{player.name}, wygrałeś. Pokonałeś matkę!\n")

animate_text("Jesteś teraz sam w domu. Możesz się rozejrzeć po domu, może coś jeszcze znajdziesz przydatnego. \n")
animate_text(" to gdzie najpierw idziesz? \n")
#------------------------------
def wybierz_miejsce():
    animate_text("a - kuchnia")
    animate_text("b - salon")
    animate_text("c - łazienka")
    odp10 = input().upper()
    if odp10 == 'A':
        animate_text("udałeś się najpierw do kuchni,co robisz? \n")
        def co_robisz1():
            animate_text("a - poszukaj czegoś")
            animate_text("b - wyjdz.")
            odp11 = input().upper()
            if odp11 == 'A':
                animate_text("znalazłeś jedzenie, a ze jestes głodny zjadłeś troche (+5hp) \n")
                animate_text("znalazłes również nożyk poręczny, (+2 attaku)\n")
                player.do_attack(2)
                player.heal(5)
                animate_text("w innych pokojach nic nie znalazłeś opróch skrzynki z narzędziami \n")
            if odp11 == "B":
                animate_text("wyszedłeś z kuchni. idz: ")
                def wybierz_miejsce2():
                    animate_text("a - salon")
                    animate_text("b - łazienka")
                    odp12 = input().upper()
                    if odp12 == 'A':
                        animate_text("udałeś się do salonu,co robisz?\n")
                        def co_robisz2():
                            animate_text("a - poszukaj czegoś")
                            animate_text("b - wyjdz.")
                            odp13 = input().upper()
                            if odp13 == 'A':
                                animate_text("znalazłeś starą krzynke z nażedziami w szawce, troche dziwne nie?\n")
                                animate_text("wziołeś ją ze sobą, może się przyta\n")
                                animate_text("została ci tylko łazienka w której nic nie znalazłeś\n")
                            if odp13 == "B":
                                animate_text("wyszedłeś z salonu\n")
                                animate_text("została ci tylko łazienka, w której nic nie znalazłeś\n")
                            else: 
                                return 0
                        odp13 = co_robisz2()
                    if odp12 == "B":
                        animate_text("w łazience nic nie znalazłeś\n")
                        animate_text("został ci tylko salon, w którym\n")
                        animate_text("znalazłeś starą krzynke z nażedziami w szawce, troche dziwne nie?\n")
                        animate_text("wziołeś ją ze sobą, może się przyta\n")
                    else:
                        return 0
                odp12 = wybierz_miejsce2()
            else:
                return 0
        odp11 = co_robisz1()
    if odp10 == 'B':
        animate_text(" udałeś się napierw do salonu, co robisz?\n")
        def co_robisz3():
            animate_text("a - poszukaj czegoś\n")
            animate_text("b - wyjdz.")
            odp14 = input().upper()
            if odp14 == 'A':
                animate_text("znalazłeś starą krzynke z nażedziami w szawce, troche dziwne nie?\n")
                animate_text("wziałeś ją ze sobą, może się przyta\n")
                def miejsce20():
                    animate_text("a- kuchnia")
                    animate_text("b- salon")
                    odp20 = input().upper()
                    if odp20 == 'A':
                        animate_text("znalazłeś jedzenie, a ze jestes głodny zjadłeś troche (+5hp)\n")
                        animate_text("znalazłes również nożyk poręczny, (+2 attaku)\n")
                        player.do_attack(2)
                        player.heal(5)
                    if odp20 == "B":
                        ("poszedłeś do salonu gdzie tam znalazłeś skrzynkę z narzędziami\n")
                    else:
                        return 0
                odp20 = miejsce20()
            if odp14 == "B":
                animate_text("wyszedłeś z salonu\n")
                def wybierz_miejsce5():
                    animate_text("a - kuchnia")
                    animate_text("b - łazienka")
                    odp15 = input().upper()
                    if odp15 == 'A':
                        animate_text("udałeś się do kuchni,\n")
                        animate_text("znalazłeś jedzenie, a ze jestes głodny zjadłeś troche (+5hp)\n")
                        animate_text("znalazłes również nożyk poręczny, (+2 attaku)\n")
                        player.do_attack(2)
                        player.heal(5)
                        animate_text("została ci tylko łązienka w której nic nie znalazłeś\n")
                    if odp15 == "B":
                        animate_text("w łazience nic nie znalazłeś\n")
                        animate_text("została ci kuchnia w której znalazłes\n")
                        animate_text("jedzenie, a ze jestes głodny zjadłeś troche (+5hp)\n")
                        animate_text("znalazłes również nożyk poręczny, (+2 attaku)\n")
                        player.do_attack(2)
                        player.heal(5)
                    else:
                        return 0
                odp15 = wybierz_miejsce5()
        odp14 = co_robisz3()
    if odp10 == "C":
        animate_text("udałes się najperw do łazienki\n")
        def co_robisz9():
            animate_text("a - poszukaj czegoś")
            animate_text("b - wyjdz.")
            odp19 = input().upper()
            if odp19 == 'A':
                animate_text("w łazience nic nie znalazłes,\n")
                animate_text("w innych pokojach znalazłeś skrzynke z narzędziami, jedzenie, które zjadłeś oraz nozyk podreczny(+5hp +2attack)\n")
                player.do_attack(2)
                player.heal(5)
            if odp19 == "B":
                animate_text("w innych pokojach znalazłeś skrzynke z narzędziami, jedzenie, które zjadłeś oraz nozyk podreczny(+5hp +2attack)\n")
                player.do_attack(2)
                player.heal(5)
            else: 
                return 0
        odp19 = co_robisz9()
odp10 = wybierz_miejsce()
# -------------------------------------------
print("-=-=-=-=-=-=-="*7)
animate_text("W drodze do sklepu nikogo nie było,\n")
#--------------------------------------------
animate_text("-=-=-=-=-=-=-=-="*7)
animate_text("Szłeś dobre 10 minut,\n")
animate_text("nikogo nie spotkałeś, jedyne co widziałeś to przewalone śmieci, puste auta a niektóre nawet rozbitei stojące w płomieniach\n")
animate_text("Znalazłeś pierwszy sklep, sklep spożywczy\n")
animate_text("patrząc przez okna nie było nic widzać, a drzwi wyglądają na otwarte wchodzisz?\n")
# -------------------------------------------------------------------------------------
def sklep():
    animate_text("a/A - wejdz\n")
    animate_text("b/B - poszukaj innego sklepu\n")
    odpsklep = input().upper()
    if odpsklep == 'A':
        return 0
    if odpsklep == "B":
        animate_text("proszę, bądz miły i wejdz do sklepu.\n")
        def sklep2():
            animate_text("a/A - wejdz,\n")
            animate_text("b/B - poszukaj innego sklepu\n")
            odpsklep2 = input().upper()
            if odpsklep2 == 'A':
                animate_text("Jednak wchodzisz?\n")
                def wchodzisz():
                    animate_text("a/A - Tak\n")
                    animate_text("b/B - Żartuje, nie wchodze\n")
                    odpW = input().upper()
                    if odpW == 'A':
                        animate_text("Dziękuje i zaprszam serdecznie\n")
                    elif odpW == 'B':
                            animate_text("słuchaj, i tak wejdziesz do slepu czy tego chcesz czy nie.\n")
                    def Wchodzisz2():
                        animate_text("a/A - wejdz,\n")
                        animate_text("b/B - poszukaj innego sklepu\n")
                        odpW2 = input().upper()
                        if odpW2 == 'a':
                            return 0 
                        if odpW2 == "B":
                            animate_text("sam tego chciałeś, jak nie po miłemu to na siłe (-5hp)\n")
                            player.take_damage(5)
                        else:
                            return 0
                    odpW2 = Wchodzisz2()
                odpW = wchodzisz()
            if odpsklep2 == "B":
                animate_text("słuchaj, i tak wejdziesz do slepu czy tego chcesz czy nie.\n")
                def sklep3():
                    animate_text("a/A - wejdz,\n")
                    animate_text("b/B - poszukaj innego sklepu\n")
                    odpsklep3 = input().upper()
                    if odpsklep3 == 'a':
                        return 0 
                    if odpsklep3 == "B":
                        animate_text("sam tego chciałeś, jak nie po miłemu to na siłe (-5hp)\n")
                        player.take_damage(5)
                    else:
                        return 0
                odpsklep3 = sklep3()
            else:
                return 0
        odpsklep2 = sklep2()
    else:
        return 0
odpsklep = sklep()
#-----------------------------------------------------------------------
animate_text("Wchodizsz do sklepu, który wydaje się pusty, idealna okazja.\n")
animate_text("Rozglądasz się po sklepie, jednak jedną rzecz zauważasz odrazu, wszystkie produkty co mają krótki termin ważnosci (typu owoce) są zepsute, bardzo zepsute..\n")
animate_text("Ten sklep jest w stanie jakby nikogo tu od dawna nie było.\n")
animate_text("*Ile mineło dni?, czemu to wszystko jest w takim stanie?*\n")
animate_text('jedyne co znalazłeś jeszcze w dobrym stanie to makarony i produkty w puszkach,\n')
animate_text("*nic ciekawego ani przydetnago tu nie ma* powiedziałeś kierując się w strone wyjścia\n")
animate_text("Jeydny problem jest taki, że to coś stoi przy drzwiach,")
animate_text("rozmyślając sytuacje: ")
animate_text("wiesz, że znajduję się wyjscie ewakuacyjne po drugiej stronie sklepu, jak i okna które można łatwo wybić\n")
#_---------------------------------------------------------------------------------------------------------------
def droga_ucieczki():
    animate_text("a/A - wyjście ewakacyjne\n")
    animate_text("b/B - przez okno\n ")
    animate_text("c/C - może przejdziesz obok tego czegoś?\n")
    animate_text("nie może być źle prawda?\n")
    odp_ucieczka = input().upper()
    if odp_ucieczka == 'A':
        animate_text("Zawrócłeś się, wolnym, cichym krokiem w strone drzwi ewakuacyjnych.\n")
        animate_text("udeżyłeś przypadkiem metalową puszkę na ziemi, słyszysz jak dzwięk uderzeń metalu o podłoge rozprzeszenia sie po całym budynku,\n")
        animate_text("zwróciło to uwage potwora który w tym momencie na ciebie biegnie,\n")
        def attack_potwor():
            if player.yourattack >= potwor.pcurrent_hp:
                animate_text(f"Zadałeś mu {potwor.pcurrent_hp} obrażeń i pokonałeś ją!")
                potwor.take_damage(potwor.pcurrent_hp)  
            else:
                animate_text(f"Zadałeś mu {player.yourattack} obrażeń!")
                potwor.take_damage(player.yourattack) 
            #--Symulacja walki
        while player.current_hp > 0 and potwor.pcurrent_hp > 0:
            attack_potwor()
            if potwor.pcurrent_hp <= 0:
                break 

            player.take_damage(potwor.pherattack)
            if player.current_hp <= 0:
                sys.exit(0)  
        if player.current_hp <= 0:
            animate_text(f"{player.name}, przegrałeś!")
        elif potwor.pcurrent_hp <= 0:
            animate_text(f"{player.name}, wygrałeś.")
            #---
        animate_text("Wyszło na jedno i tak musiałeś się z tym bić.\n")

    elif odp_ucieczka == 'B':
        animate_text("ruszyłeś w strone okna, cicho i bezpośpiechu")
        animate_text("na twoje szczęście okno jest już wybite, jedyny problem to duża ilość szkła, która możę  cię skaleczyc,\n")
        animate_text("napewno chcesz isć?\n")
        def uceiczka_okno():
            animate_text("a/A - Tak")
            animate_text("b\B Nie, idę dalej do drzwi awaryjnych\n")
            odpucieczka = input().upper()
            if odpucieczka == 'A':
                animate_text("wyszedłeś przez okno, jednak się troche skaleczyłeś (-1hp)\n")
                player.take_damage(1)
            elif odpucieczka == 'B':
                animate_text("Zawrócłeś się, wolnym, cichym krokiem w strone drzwi ewakuacyjnych.\n")
                animate_text("udeżyłeś przypadkiem metalową puszkę na ziemi, słyszysz jak dzwiek uderzeń metalu o podłoge rozprzeszenia sie po całym budynku,\n")
                animate_text("zwróciło to uwage potwora który w tym momencie na ciebie biegnie,\n")
                def attack_potwor():
                    if player.yourattack >= potwor.pcurrent_hp:
                        animate_text(f"Zadałeś mu {potwor.pcurrent_hp} obrażeń i pokonałeś ją!\n")
                        potwor.take_damage(potwor.pcurrent_hp)  
                    else:
                        animate_text(f"Zadałeś mu {player.yourattack} obrażeń!\n")
                        potwor.take_damage(player.yourattack) 
                    #--Symulacja walki
                while player.current_hp > 0 and potwor.pcurrent_hp > 0:
                    attack_potwor()
                    if potwor.pcurrent_hp <= 0:
                        break 

                    player.take_damage(potwor.pherattack)
                    if player.current_hp <= 0:
                        sys.exit(0)

                if player.current_hp <= 0:
                    animate_text(f"{player.name}, przegrałeś!\n")
                elif potwor.pcurrent_hp <= 0:
                    animate_text(f"{player.name}, wygrałeś.\n")
                animate_text("Wyszło na jedno i tak musiałeś się z tym bić.\n")
        odpucieczka = uceiczka_okno()
    elif odp_ucieczka == 'C':
        animate_text("próbowałes przejść jakoś przejśc, może cie nie zobaczy?\n")
        animate_text("cofam słowa, zobaczyło cię odrazu jak postawiłeś pierwszy krok.\n")
        def Pierwszykrok():
            animate_text("a/A - uciekaj\n")
            animate_text("b/B - Walcz\n")
            odpPK = input().upper()
            if odpPK == 'A':
                def UciekajPK():
                    animate_text("a/A - Prez okno,\n")
                    animate_text("b/B - drzwi awaryjne\n")
                    odpUPK = input().upper()
                    if odpUPK == 'A':
                        animate_text("ruszyłeś w strone okna, biegiem, ")
                        animate_text("na twoje szczęście okno jest już wybite, jedyny problem to duża ilość szkła, która możę  cię skaleczyc,\n")
                        animate_text("napewno chcesz isć?\n")
                        def uceiczka_okno2():
                            animate_text("a/A - Tak\n")
                            animate_text("b\B Nie, idę dalej do drzwi awaryjnych\n")
                            odpucieczka2 = input().upper()
                            if odpucieczka2 == 'A':
                                animate_text("wyszedłeś przez okno, jednak się troche skaleczyłeś (-1hp)\n")
                                animate_text("prznajmniej potwór nie wyszedł za tobą, ")
                                player.take_damage(1)
                            elif odpucieczka2 == 'B':
                                animate_text("Pobiegłeś w strone drzwi ewakuacyjnych.\n")
                                animate_text("potknołeś się po drodze o puszke,\n")
                                animate_text("Potwór dogania,\n")
                                def attack_potwor():
                                    if player.yourattack >= potwor.pcurrent_hp:
                                        animate_text(f"Zadałeś mu {potwor.pcurrent_hp} obrażeń i pokonałeś ją!\n")
                                        potwor.take_damage(potwor.pcurrent_hp)  
                                    else:
                                        animate_text(f"Zadałeś mu {player.yourattack} obrażeń!\n")
                                        potwor.take_damage(player.yourattack) 
                                    #--Symulacja walki
                                while player.current_hp > 0 and potwor.pcurrent_hp > 0:
                                    attack_potwor()
                                    if potwor.pcurrent_hp <= 0:
                                        break 

                                    player.take_damage(potwor.pherattack)
                                    if player.current_hp <= 0:
                                        sys.exit(0)

                                    if player.current_hp <= 0:
                                        animate_text(f"{player.name}, przegrałeś!\n")
                                    elif potwor.pcurrent_hp <= 0:
                                        animate_text(f"{player.name}, wygrałeś.\n")
                                    animate_text("Wyszło na jedno i tak musiałeś się z tym bić.\n")
                        odpucieczka2 = uceiczka_okno2()
                    elif odpUPK == 'b':
                        animate_text("pobiegłes w strone drzwi ewakuacyjnych.\n")
                        animate_text("udeżyłeś przypadkiem metalową puszkę na ziemi i się wywruciłeś\n")
                        animate_text(" w tym momencie potwór cie dogania,\n")
                        def attack_potwor():
                            if player.yourattack >= potwor.pcurrent_hp:
                                animate_text(f"Zadałeś mu {potwor.pcurrent_hp} obrażeń i pokonałeś ją!")
                                potwor.take_damage(potwor.pcurrent_hp)  
                            else:
                                animate_text(f"Zadałeś mu {player.yourattack} obrażeń!")
                                potwor.take_damage(player.yourattack) 
                                #--Symulacja walki
                        while player.current_hp > 0 and potwor.pcurrent_hp > 0:
                            attack_potwor()
                            if potwor.pcurrent_hp <= 0:
                                break 

                            player.take_damage(potwor.pherattack)
                            if player.current_hp <= 0:
                                sys.exit(0)  
                            if player.current_hp <= 0:
                                animate_text(f"{player.name}, przegrałeś!")
                            elif potwor.pcurrent_hp <= 0:
                                animate_text(f"{player.name}, wygrałeś.")
                            #---
                        animate_text("Wyszło na jedno i tak musiałeś się z tym bić.\n")
                    else:
                        return 0
                odpUPK = UciekajPK()
            elif odpPK == 'B':
                animate_text("Postanowiłęś się z tym bić,\n")
                def attack_potwor():
                    if player.yourattack >= potwor.pcurrent_hp:
                        animate_text(f"Zadałeś mu {potwor.pcurrent_hp} obrażeń i pokonałeś ją!")
                        potwor.take_damage(potwor.pcurrent_hp)  
                    else:
                        animate_text(f"Zadałeś mu {player.yourattack} obrażeń!")
                        potwor.take_damage(player.yourattack) 
                        #--Symulacja walki
                while player.current_hp > 0 and potwor.pcurrent_hp > 0:
                    attack_potwor()
                    if potwor.pcurrent_hp <= 0:
                        break 

                    player.take_damage(potwor.pherattack)
                    if player.current_hp <= 0:
                        sys.exit(0)  
                    if player.current_hp <= 0:
                        animate_text(f"{player.name}, przegrałeś!")
                    elif potwor.pcurrent_hp <= 0:
                        animate_text(f"{player.name}, wygrałeś.")
                animate_text("możesz teraz bezpiecznie wyjść ze sklepu")
            else:
                animate_text("stoisz w miejscu, nic nie zrobiłeś\n")
                def attack_potwor():
                    if player.yourattack >= potwor.pcurrent_hp:
                        animate_text(f"Zadałeś mu {potwor.pcurrent_hp} obrażeń i pokonałeś ją!")
                        potwor.take_damage(potwor.pcurrent_hp)  
                    else:
                        animate_text(f"Zadałeś mu {player.yourattack} obrażeń!")
                        potwor.take_damage(player.yourattack) 
                        #--Symulacja walki
                while player.current_hp > 0 and potwor.pcurrent_hp > 0:
                    attack_potwor()
                    if potwor.pcurrent_hp <= 0:
                        break 

                    player.take_damage(potwor.pherattack)
                    if player.current_hp <= 0:
                        sys.exit(0)  
                    if player.current_hp <= 0:
                        animate_text(f"{player.name}, przegrałeś!")
                    elif potwor.pcurrent_hp <= 0:
                        animate_text(f"{player.name}, wygrałeś.")
                animate_text("możesz teraz bezpiecznie wyjśc ze sklepu.")
        odpPK = Pierwszykrok()
odp_ucieczka = droga_ucieczki()

animate_text("wyszedłeś wkońcu ze sklepu\n")
#-------------------------------------------------------
animate_text("Po drugiej stronie zauważasz apteke, Budynek w dorbrym stanie, jak i Sklep ogólny, taki co ma wszystko (Auchan?) budynek, pomijając brak okien, tez wygląda w dobrym stanie.\n")
animate_text("zauważasz też że to jedyne sklepy w okolicy.\n")
animate_text("gdzie idziesz teraz?")

def coteraz():
    animate_text("a/A - apteka - *Może zajdę coś by zaopatrzyć ranny?*\n")
    animate_text("b/B - ogólniak - *Myślę że będzie tam dużo przydatnych rzeczy*\n")
    animate_text("c/C - dalsza przygoda - *Może kogoś znajde?*\n")
    odpcotreaz = input().upper()
    if odpcotreaz == "A":
        animate_text("udałeś się do apteki\n")
        animate_text("podeszłeś do drzwi które okazały się zamknięte,\n ")
        def aptekawejscie():
            animate_text("a/A - *Mogę spróbować wywarzyć drzwi?*\n")
            animate_text("b/B - *A może przez okno?*\n")
            animate_text("c/C - znajdz tylnie drzwi - *może są tylnie drzwi?*\n")
            animate_text("d/D - cofnięcie się do ogólniaka,")
            odpcotreaz2 = input().upper()
            if odpcotreaz2 == "A":
                animate_text("drzwi nie wyglądają na mocne, za 3 uderzeniem drzwi odpadły z zawiasów \n")
                animate_text("*zawiasy wyglądaja na stare, nic dziwnego że łatwo poszło.\n")
                animate_text("Wszedłeś do środka, nic tu niezostało zniszczone, no oprócz tej Wielkiej dziury w ścianie, której w środku trudno nie zauważyć\n")
                animate_text("rozejrzałeś się po aptece, znalazłeś sporo bandarzy, plastrów i pateczke pierwszej pomocy, zaopatrzyłeś swoje rany (+20hp)\n")
                player.heal(20)
                animate_text("różne leki ci się zbytnio nie przydadzą\n")
                animate_text("wyszedłeś z budynku\n")
                return 0
            elif odpcotreaz2 == "B":
                animate_text("tych okien nie da się otworzyć, ja każde domowe okno zostało ci je tylko wybić\n")
                animate_text("po pierwszym uderzeniu zauważasz że to nie będzie takie proste, próbujesz jeszcze 2 razy lecz nic nowego\n")
                def ostrze():
                    animate_text("a/A - próbuj dalej\n")
                    animate_text("b/B - znajdz może coś ostrego\n")
                    odpO = input().upper()
                    if odpO == "A":
                        animate_text("po paru więcej mocniejszycz uderzeniach szkło wreście pękło.\n")
                        animate_text("Pamiętaj, szkło jesst ostre i się skaleczyłeś w paru miejscach (-2hp, -5stamina)\n")
                        player.no_stamina(5)
                        player.take_damage(2)
                        animate_text("Wszedłeś do środka, nic tu niezostało zniszczone, no oprócz tej Wielkiej dziury w ścianie, której w środku trudno nie zauważyć\n")
                        animate_text("rozejrzałeś się po aptece, znalazłeś sporo bandarzy, plastrów i pateczke pierwszej pomocy, zaopatrzyłeś swoje rany (+20hp)\n")
                        player.heal(20)
                        animate_text("różne leki ci się zbytnio nie przydadzą\n")
                        animate_text("wyszedłeś z budynku\n")
                        return 0
                    elif odpO == "B":
                        animate_text("przypomniałeś sobie o skrzynce z narzędziami z salonu, wyjmujesz z niej śrubokręt\n")
                        animate_text("śrubokręt definityfnie zadał troche obrażeń, teraz powinno pójść lepiej, jak i poszło.\n")
                        animate_text("Po kolejnym uderzeniu szkło się rozbiło całkowicie, poszło ładnie i gładko, (-1hp, -1stamina)\n")
                        player.no_stamina(1)
                        player.take_damage(1)
                        return 0
                    else: 
                        return 0
                odpO = ostrze()
                animate_text("Wszedłeś do środka, nic tu niezostało zniszczone, no oprócz tej Wielkiej dziury w ścianie, której w środku trudno nie zauważyć\n")
                animate_text("rozejrzałeś się po aptece, znalazłeś sporo bandarzy, plastrów i pateczke pierwszej pomocy, zaopatrzyłeś swoje rany (+20hp)\n")
                player.heal(20)
                animate_text("różne leki ci się zbytnio nie przydadzą\n")
                animate_text("wyszedłeś z budynku\n")
                return 0
            elif odpcotreaz2 == "C":
                animate_text("przeszedłeś budynek do okoła ale niewydaje się żeby były jakieś tylnie drzwi, coprawda jest spora dziura w ścianie, może kiedyś tu były drzwi?\n")
                animate_text("Wszedłeś do środka, nic tu niezostało zniszczone, no oprócz tej Wielkiej dziury w ścianie, której w środku trudno nie zauważyć\n")
                animate_text("rozejrzałeś się po aptece, znalazłeś sporo bandarzy, plastrów i pateczke pierwszej pomocy, zaopatrzyłeś swoje rany (+20hp)\n")
                player.heal(20)
                animate_text("różne leki ci się zbytnio nie przydadzą\n")
                animate_text("wyszedłeś z budynku\n")
                return 0
            elif odpcotreaz2 == "D":
                animate_text("potrzedłeś do budynku, drzwi są zamknięte\n")
                def ogolniak():
                    animate_text("a/A - spróbuj wywarzyć drzwi\n")
                    animate_text("b/B - przejść przez okno.\n")
                    odpOG = input().upper()
                    if odpOG == 'A':
                        animate_text("Drzwi wypadają z zawiasów odrazu bez rzadnego problemu.\n")
                        return 0
                    elif odpOG == 'B':
                        animate_text("wchodzisz przez okno, kalęcząc się o szkło (-1hp)\n")
                        player.take_damage(1)
                    else:
                        return 0
                odpOG = ogolniak()
                animate_text("Ten sklep jest ogromny, znajdujesz sporo rzeczy, bandarze którymi opatrujesz sobie rany jednak dużo ich niebyło (+10hp)\n")
                player.heal(10)
                animate_text("z jedzenia praktycznie wszystko było zepsute oprócz niektórych produktów, *wyglądają niby na dobre...*, jesteś głodny nie?\n")
                def jedzenie():
                    animate_text("a/A - zjedz to co się nadaje\n")
                    animate_text("b/B - nie jedz")
                    odpJ = input().upper()
                    if odpJ == 'A':
                        animate_text("Dużo tego nie było lecz nie czujesz się bardzo głodny, może i lepij (+5hp)\n")
                        player.heal(5)
                    elif odpJ == 'B':
                        animate_text("niedotknełeś nic z jedzenia, czujesz się troche głodny to prawda ale kto wie czy to wogule się jeszcze nadaje?\n")
                    else:
                        return 0
                odpJ = jedzenie
                animate_text("usłyszałeś jakieś uderzenie, jednak wybite okna nie były bez powodu\n")
                def Pogolniak():
                    animate_text("a/A - poszukaj powodu hałasu - *Może jest ze mną ktoś jeszcze?*\n")
                    animate_text("b/B - uciekaj.")
                    odpPO = input().upper()
                    if odpPO == 'A':
                        animate_text("poszedłeś w strone hałąsu myślać że to albo zwierze, albo ktoś z nas. Byłeś w błędzie\n")
                        animate_text("To cię zobaczyło.")
                        def attack_potwor():
                            if player.yourattack >= potwor2.p2current_hp:
                                animate_text(f"Zadałeś mu {potwor2.p2current_hp} obrażeń i pokonałeś ją!\n")
                                potwor2.take_damage(potwor2.p2current_hp)  
                            else:
                                animate_text(f"Zadałeś mu {player.yourattack} obrażeń!\n")
                                potwor2.take_damage(player.yourattack) 
                            #--Symulacja walki
                        while player.current_hp > 0 and potwor2.p2current_hp > 0:
                            attack_potwor()
                            if potwor2.p2current_hp <= 0:
                                break 

                            player.take_damage(potwor2.p2herattack)
                            if player.current_hp <= 0:
                                sys.exit(0)

                            if player.current_hp <= 0:
                                animate_text(f"{player.name}, przegrałeś!")
                            elif potwor.pcurrent_hp <= 0:
                                animate_text(f"{player.name}, wygrałeś.")
                        animate_text("I poco ci to było?")
                        animate_text("co prawda, ten nie wydawał się wogule na mocnego, w rozmiarze też mały, czyli są rózne ich rodzaje.\n")
                        animate_text("wyszedłeś z budynku")
                    elif odpPO == 'B':
                        animate_text("ruszyłeś w strone wyjścia szybkim krokiem\n")
                        animate_text("Tak długo jak nie wydasz żadnego dzwięku pownno być dobrze\n")
                odpPO = Pogolniak()
            else:
                return 0
        odpcoteraz2 = aptekawejscie()

    elif odpcotreaz == "B":
        animate_text("potrzedłeś do budynku, drzwi są zamknięte\n")
        def ogolniak():
            animate_text("a/A - spróbuj wywarzyć drzwi\n")
            animate_text("b/B - przejść przez okno.\n")
            odpOG = input().upper()
            if odpOG == 'A':
                animate_text("Drzwi wypadają z zawiasów odrazu bez rzadnego problemu.\n")
                return 0
            elif odpOG == 'B':
                animate_text("wchodzisz przez okno, kalęcząc się o szkło (-1hp)\n")
                player.take_damage(1)
            else:
                return 0
        odpOG = ogolniak()
        animate_text("Ten sklep jest ogromny, znajdujesz sporo rzeczy, bandarze którymi opatrujesz sobie rany jednak dużo ich niebyło (+10hp)\n")
        player.heal(10)
        animate_text("z jedzenia praktycznie wszystko było zepsute oprócz niektórych produktów, *wyglądają niby na dobre...*, jesteś głodny nie?\n")
        def jedzenie():
            animate_text("a/A - zjedz to co się nadaje\n")
            animate_text("b/B - nie jedz")
            odpJ = input().upper()
            if odpJ == 'A':
                animate_text("Dużo tego nie było lecz nie czujesz się bardzo głodny, może i lepij (+5hp)\n")
                player.heal(5)
            elif odpJ == 'B':
                animate_text("niedotknełeś nic z jedzenia, czujesz się troche głodny to prawda ale kto wie czy to wogule się jeszcze nadaje?\n")
            else:
                return 0
        odpJ = jedzenie
        animate_text("usłyszałeś jakieś uderzenie, jednak wybite okna nie były bez powodu\n")
        def Pogolniak():
            animate_text("a/A - poszukaj powodu hałasu - *Może jest ze mną ktoś jeszcze?*\n")
            animate_text("b/B - uciekaj.")
            odpPO = input().upper()
            if odpPO == 'A':
                animate_text("poszedłeś w strone hałąsu myślać że to albo zwierze, albo ktoś z nas. Byłeś w błędzie\n")
                animate_text("To cię zobaczyło.")
                def attack_potwor():
                    if player.yourattack >= potwor2.p2current_hp:
                        animate_text(f"Zadałeś mu {potwor2.p2current_hp} obrażeń i pokonałeś ją!\n")
                        potwor2.take_damage(potwor2.p2current_hp)  
                    else:
                        animate_text(f"Zadałeś mu {player.yourattack} obrażeń!\n")
                        potwor2.take_damage(player.yourattack) 
                    #--Symulacja walki
                while player.current_hp > 0 and potwor2.p2current_hp > 0:
                    attack_potwor()
                    if potwor2.p2current_hp <= 0:
                        break 

                    player.take_damage(potwor2.p2herattack)
                    if player.current_hp <= 0:
                        sys.exit(0)

                if player.current_hp <= 0:
                    animate_text(f"{player.name}, przegrałeś!")
                elif potwor.pcurrent_hp <= 0:
                    animate_text(f"{player.name}, wygrałeś.")

                animate_text("I poco ci to było?")
                animate_text("co prawda, ten nie wydawał się wogule na mocnego, w rozmiarze też mały, czyli są rózne ich rodzaje.\n")
                animate_text("wyszedłeś z budynku")
            elif odpPO == 'B':
                animate_text("ruszyłeś w strone wyjścia szybkim krokiem\n")
                animate_text("Tak długo jak nie wydasz żadnego dzwięku pownno być dobrze\n")
        odpPO = Pogolniak()
    elif odpcotreaz == "C":
        return 0
    else:
        return 0
odpcoteraz = coteraz()
#_-------------------------------
animate_text("-=-=-=-=-=-=-=-=-=--="*7)
animate_text("szedłeś dalej ulicą\n")
animate_text(" Usłyszałeś dzwięk silnika, troche dziwne gdyż myślałeś ze jesteś sam. . . \n")
animate_text("Odwracasz sięi widzisz pancernego warana, (no wiesz taki vann wojskowy), który ewidentnie jedzie w twoją strone.\n ")
def pancernywaran():
    animate_text("a/A - poczekaj, może jedak są tu inni ludzie?\n")
    animate_text("b/B - uciekaj, znajdz gdzie się schować\n")
    odpPW = input().upper()
    if odpPW == 'A':
        animate_text("Pancerny waran podjeżdża i wyskakuje z nich 3 panów w mundurach na żołnieża, \n")
        animate_text("Odrazu wsadzają cie do auta, nie miałeś czasu na reakcje,\n")
        animate_text(" 'Nie ruszaj się, nic ci nie zrobimy' - powiedział jeden z panów, \n")
        def Nieruszajsie():
            animate_text("a/A - słuchaj się tego co mówi, ten karabin na jego plecach nie wygląda zaciekawie. \n")
            animate_text("b/B - może da się jakoś uciec?\n")
            odpNR = input().upper()
            if odpNR == 'A':
                return 0 
            elif odpNR == 'B':
                animate_text("'co kolwiek teraz myślisz nie rób tego, sytuacja jak dobrze wiesz nie jest zaciekawa,' - powiedział, ale dobrze o tym wiesz, w końcu ile razy się z tym biłeś?\n")
                animate_text("'nie utrudniaj nam bardziej pracy niż już jest' - pora się posłuchać.\n")
                return 0
            else:
                return 0
        odpNR = Nieruszajsie()
        animate_text("'Dobra, dzięki, chociaż tyle, to co widziałeś wcześniej, to co chcaiło cie zabić nazywamy Sorami.' - Sorami? ciekawe dlaczego taka nazwa, \n")
        animate_text("'Sory znajdują się wszedzie, nie ma państwa gdzie ich nie ma, Państwa które zostały połączył się i próbujemy znaleśc przyczyne tego wszystkiego, a jeżeli możliwe  to i lekarstwo' \n")
        animate_text(" 'napewno masz dużo pytań, zrobimy deal, bedziemy się wymieniać pytaniami ok? ty jedno, ja jednodo momentu jak skączą się pytania.' - więc Jakie masz pytanie?\n")
        def Pytanie():
            animate_text("a/A - Jakie dokładnie państwa?\n")
            animate_text("b/B - Jak mnie znaleźliście?\n")
            odpP = input().upper()
            if odpP == 'A':
                animate_text("'Naprawde cię to interesuje?' - zdziwionny, gdyż kogo interesuje polityka?\n")
                animate_text("'W takiej sytuacji, Polska, bo my tu dalej jesteśmy, USA, Rosja, Chiny, Japonia, Niemcy, czyli te duże w sumie państwa, ale również Estonia jakoś się utrzymała\n")
                return 0 
            elif odpP == 'B':
                animate_text("'Stałeś na środku ulicy. ale przed tym zauważyliśmy że pare Soren było marte, widać ze tuż po walce'\n")
                animate_text("'A z czego zauważyliśmy, one nie zabijają się siebie nawzajem, one wsółpracują\n")
                return 0 
            else:
                return 0
        odpP = Pytanie()
        animate_text("'Moja kolej na pytanie, Jak długo tu byłeś a co najważniejsze jak ty wogule przeżyłeś??? nie wygląasz na kogoś kto umie walczyć'\n")
        animate_text("Pytanie z czasem to dobre faktycznie pytanie, Czas stoi w miejscu, skąd masz wiedzieć? *to czas nie stoi w miejscu?*\n")
        animate_text("'no w sumie tak, głupie pytanie ale musiałęś być tu długo skoro wiesz że czas stoi w miejscu.'\n")
        animate_text(" Usyszelicie jakieś walnięcie, któryś z panów krzyczy 'Sora!, musimy ztąd jechać!' i tak się staneło, kierowca dorazu ruszył i odjechaliście,\n")
        animate_text("'Jedziemy spowrotem do bazy, widać ze czasu na więcej pytań nie ma'.\n") 
    elif odpPW =='B':
        animate_text("BYłeś zawolny, ktobypomyślał że takie brzydke auto szybko jeżdzi?, Wysiedli z niego 3 mężczyzn i zabrali cię do środka auta.\n")
        animate_text(" 'Nie ruszaj się, nic ci nie zrobimy' - powiedział jeden z panów,\n ")
        def Nieruszajsie():
            animate_text("a/A - słuchaj się tego co mówi, ten karabin na jego plecach nie wygląda zaciekawie.\n ")
            animate_text("b/B - może da się jakoś uciec?")
            odpNR = input().upper()
            if odpNR == 'A':
                return 0 
            elif odpNR == 'B':
                animate_text("'Nieutrudniaj sprawy bardziej niż już jest!, nie jest zaciekawie, i fakt że chciałeś uciec też nie pomaga, kto normalny ucieka przed wojskiem?'\n")
                animate_text("Fakt, Potwory by auta nie prowadziły. . . \n")
                return 0
            else:
                return 0
        odpNR = Nieruszajsie()
        animate_text("'Dobra, już spokojnie? to co widziałeś wcześniej, to co chcaiło cie zabić nazywamy Sorami.' - Sorami? ciekawe dlaczego taka nazwa, \n")
        animate_text("'Sory znajdują się wszedzie, nie ma państwa gdzie ich nie ma, Państwa które zostały połączył się i próbujemy znaleśc przyczyne tego wszystkiego, a jeżeli możliwe  to i lekarstwo' \n")
        animate_text(" 'napewno masz dużo pytań, zrobimy deal, bedziemy się wymieniać pytaniami ok? ty jedno, ja jednodo momentu jak skączą się pytania.' - więc Jakie masz pytanie?\n")
        def Pytanie():
            animate_text("a/A - Jakie dokładnie państwa?")
            animate_text("b/B - Jak mnie znaleźliście?")
            odpP = input().upper()
            if odpP == 'A':
                animate_text("'Naprawde cię to interesuje?, chcesz uciekać od wojska i pytasz się o sprawy związane z wojskiem?' - zdziwionny , gdyż kogo interesuje polityka?\n")
                animate_text("'W takiej sytuacji, Polska, bo my tu dalej jesteśmy, USA, Rosja, Chiny, Japonia, Niemcy, czyli te duże w sumie państwa, ale również Estonia jakoś się utrzymała\n")
                return 0 
            elif odpP == 'B':
                animate_text("'Człowieka trudno nie odrużnić, tymbardziej ktogoś kto ucieka, ale przed tym zauważyliśmy że pare Soren było marte, widać ze tuż po walce'\n")
                animate_text("'A z czego zauważyliśmy, one nie zabijają się siebie nawzajem, one wsółpracują\n")
                return 0 
            else:
                return 0
        odpP = Pytanie()
        animate_text("'Moja kolej na pytanie, Jak długo tu byłeś a co najważniejsze jak ty wogule przeżyłeś??? nie wygląasz na kogoś kto umie walczyć'\n")
        animate_text("Pytanie z czasem to dobre faktycznie pytanie, Czas stoi w miejscu, skąd masz wiedzieć? *to czas nie stoi w miejscu?*\n")
        animate_text("'no w sumie tak, głupie pytanie ale musiałęś być tu długo skoro wiesz że czas stoi w miejscu.'\n")
        animate_text(" Usyszelicie jakieś walnięcie, któryś z panów krzyczy 'Sora!, musimy ztąd jechać!' i tak się staneło, kierowca dorazu ruszył i odjechaliście,\n")
        animate_text("'Jedziemy spowrotem do bazy, widać ze czasu na więcej pytań nie ma'.\n")
odpPW = pancernywaran()

print("=-=-=-=-=-==--=-=-="*7)
animate_text("znaleźliście siępod murami bazy wojskowej, pierwsze na co zwróciłeś uwage to byli cywile, zwykli cywile\n")
animate_text("' tutaj powinno być bezpieczne, miejsce jest strzeżone z każdej strony, a cywili takich jak ty trenujemy by mogli jakoś się obronić, \n")
animate_text("'Najgorsze co tu jest? nie widaomo ile czasu mineło, cały czas jest dzień, śłońce się nie rusza i niewygląda jak by zamierzało.' - spojrzał się na niebo, ty też,\n")
animate_text("*hej ale przynajmniej łądna pogoda jest,* - powiedziałeś by poprawić troche humor, co go rośmieszyło, jakoś\n")
animate_text("'masz racje, przynajmniej tyle,'\n")
animate_text("rozglądałeś się po placówce oraz zapoznywałeś się z ludzmi,\n")
animate_text(" w pewnym momencie zawył alarm, żołnieże coś krzyczą a mur się rozwala, Sory Przyszły, całą gromadą to tak jaby wiedziały że tu jesteśmy,\n")
animate_text("NIebo nagle zrobiło sięciemne, słonce znikło,\n")
animate_text("Ktoś wykrzyknął twe imie, byś uważał, odwracasz sietylko po to by wiedzieć na ciebie spadający gruz\n")
print("=-=-=-=-=-=-=-=-="*7)
animate_text("Budzisz się w szpitali, a obok ciebie towja mama, cała, jakgdyby nigdy nic\n")
animate_text("Wytłumaczono że zapadłeś w śpiączce na miesiąc,\n")
animate_text("Wszytko co mówili lekarze miało sens tylko jest jedno ale czemu, tylko czemu one dalej tu są?\n")
animate_text("KONIEC, mam dość, dziękuje za granie tego czegoś ;)")