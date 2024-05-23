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
