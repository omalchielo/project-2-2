def main():
    print("Welcome to Tic Tac Toe")
    print(carky())
    pravidla()


    f = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    pocitani = 0
    seznam = []
    vyhry = (0, 1, 2), (3, 4, 5), (6, 7, 8),\
            (0, 3, 6), (0, 4, 8), (2, 5, 8),\
            (1, 4, 7), (2, 4, 6)
    tabulka(f)
    print(carky())
    print('{:^50}'.format("Let's start the game"))
    while True:
        if pocitani % 2 == 0:
            hrac = "x"
        else:
            hrac = "o"

        print(carky())
        x = input(f"Player {hrac} | Please enter your move number: ")
        print(carky())
        if x in seznam:
             print("pole je obsazene")
             continue
        seznam.append(x)
        if not x.isdigit():
            print("musis zadat cislo")
            continue
        if spravne_cislo(x):
            continue
        pocitani += 1
        f[int(x)] = hrac
        vysledny_hrac = hrac


        first = list(f.values())
        tabulka(f)
        for a, b, c in vyhry:
            if vysledny_hrac == first[a] == first[b] == first[c]:
                print(carky())
                print(f"Vyhrál hráč {vysledny_hrac} ")
                quit()


        if pocitani == 9 :
            print("Remíza!")
            quit()



def radek():
    return "+---+---+---+"

def carky():
    return("="*50)


def spravne_cislo(x):
    spravnost = False
    if 0 < int(x) < 10:
        spravnost = False
    else:
        spravnost = True
    return spravnost


def tabulka(f):
    first = list(f.values())
    print(radek())
    print(f"| {first[0]} | {first[1]} | {first[2]} |")
    print(radek())
    print(f"| {first[3]} | {first[4]} | {first[5]} |")
    print(radek())
    print(f"| {first[6]} | {first[7]} | {first[8]} |")
    print(radek())


def pravidla():
    print("""                GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
          """)

if __name__ == "__main__":
    main()
