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
    animate_text("a/A - Rozglądaj się po przydatne rzeczy \n")
    animate_text("b/B - Przemyśl sytuacje \n")
    odp5 = input().upper()
    if odp5 == "A":
        animate_text(" W garażu znajdujesz wiele dobrych rzeczy, ale z wszystkimi trudno się zabrać.\n ")
        def wybierz_bron():
            animate_text("a - Grabie, wyglądają na ciężkie ale są ostre.\n ")
            animate_text("b - Stare buty ojca. Twój rozmiar oraz są świetne do biegania, aż przypominając ci się stare czasy.\n ")
            animate_text("c - Młotek, trochę cieżki ale poręczny. \n")
            animate_text("d - Piła mechaniczna. Działa ale jest bardzo ciężka. \n")
            animate_text("e - Nic nie bierzesz.\n")
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
