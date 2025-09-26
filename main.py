"""Module Syracuse : Calcul et analyse de la suite de Syracuse."""
import matplotlib.pyplot as plt

def syracuse(n):
    """Calcule la suite de Syracuse pour un entier positif n."""
    if n <= 0:
        raise ValueError("n doit être un entier strictement positif.")
    suite = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        suite.append(n)
    return suite


def temps_de_vol(suite):
    """Retourne le temps de vol de la suite de Syracuse (nombre d'étapes pour atteindre 1)."""
    return len(suite) - 1


def temps_de_vol_en_altitude(suite):
    """Retourne le temps de vol en altitude (nombre de termes consécutifs strictement supérieurs à l'altitude de départ)."""
    altitude_depart = suite[0]
    tva = 0
    for valeur in suite[1:]:
        if valeur > altitude_depart:
            tva += 1
        else:
            break
    return tva


def altitude_maximale(suite):
    """Retourne l'altitude maximale atteinte dans la suite de Syracuse."""
    return max(suite)


def main():
    """Fonction principale : interaction utilisateur et affichage du graphique."""
    n = int(input("Entrez un entier strictement positif : "))
    suite = syracuse(n)
    print("Suite de Syracuse :", suite)
    print("Temps de vol :", temps_de_vol(suite))
    print("Temps de vol en altitude :", temps_de_vol_en_altitude(suite))
    print("Altitude maximale :", altitude_maximale(suite))

    x_vals = list(range(len(suite)))
    plt.plot(x_vals, suite, marker="o", linestyle="-", color="b")
    plt.title(f"Suite de Syracuse pour n = {n}")
    plt.xlabel("Étape")
    plt.ylabel("Valeur")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
