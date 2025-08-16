from .analyser import analyser


def main():
    chemin = input("Entrez le chemin vers votre code : ")
    resultats = analyser(chemin)
    for resultat in resultats:
        print(resultat)


if __name__ == '__main__':
    main()
