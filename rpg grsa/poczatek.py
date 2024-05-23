animate_text("Promienie słońca wpadły przez odsłonięte okno prosto na twoją twarz. \n")
animate_text("Powoli otworzyłeś oczy i przeciągnąłeś się.\n ")
animate_text("Twoją uwagę zwrócił fakt, iż było aż zbyt cicho. \n")
animate_text("Co było dziwne biorąc pod uwagę, że zazwyczaj w sobotę dziaciaki sąsiadów już jeździły po osiedlu\n ")
animate_text("*Która jest godzina?*\n ")
animate_text("Sięgnąłeś po telefon. Wyświetlacz pokazywał godzinę 9:30. \n")
animate_text("*Dziwne... Zazwyczaj już by ktoś mnie siłą zrzucił z łóżka* \n")
#------------------------------------
def wybierz_odp1():
    animate_text("a/A - Zawołaj \n")
    animate_text("b/B - Wstań z łóżka \n")
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
animate_text("Jest cicho i pusto \n")
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
