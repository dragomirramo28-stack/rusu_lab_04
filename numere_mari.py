import os

FISIER = "numere.txt"
MAX_CIFRE = 200


def elimina_zerouri(s):
    i = 0
    while i < len(s) - 1 and s[i] == "0":
        i += 1
    return s[i:]


def citeste_numere(nume_fisier=FISIER):
    if not os.path.isfile(nume_fisier):
        raise ValueError(f"Fișierul '{nume_fisier}' nu există.")
    with open(nume_fisier, "r", encoding="utf-8") as f:
        linii = [linie.strip() for linie in f if linie.strip() != ""]
    if len(linii) < 2:
        raise ValueError("Fișierul trebuie să conțină două numere, câte unul pe linie.")
    numere = []
    for idx, linie in enumerate(linii[:2], start=1):
        if not linie.isdigit():
            raise ValueError(f"Linia {idx} nu conține un număr natural valid: '{linie}'.")
        linie = elimina_zerouri(linie)
        if len(linie) > MAX_CIFRE:
            raise ValueError(f"Numărul de pe linia {idx} are mai mult de {MAX_CIFRE} cifre.")
        numere.append(linie)
    return numere[0], numere[1]


def aduna(a, b):
    i = len(a) - 1
    j = len(b) - 1
    transport = 0
    cifre = []
    while i >= 0 or j >= 0 or transport:
        suma = transport
        if i >= 0:
            suma += ord(a[i]) - ord("0")
            i -= 1
        if j >= 0:
            suma += ord(b[j]) - ord("0")
            j -= 1
        cifre.append(suma % 10)
        transport = suma // 10
    rezultat = ""
    for c in reversed(cifre):
        rezultat += str(c)
    return elimina_zerouri(rezultat)

def inmulteste(a, b):
    if a == "0" or b == "0":
        return "0"
    rezultat = [0] * (len(a) + len(b))
    for i in range(len(a)):
        ca = ord(a[len(a) - 1 - i]) - ord("0")
        transport = 0
        for j in range(len(b)):
            cb = ord(b[len(b) - 1 - j]) - ord("0")
            total = rezultat[i + j] + ca * cb + transport
            rezultat[i + j] = total % 10
            transport = total // 10
        poz = i + len(b)
        while transport:
            total = rezultat[poz] + transport
            rezultat[poz] = total % 10
            transport = total // 10
            poz += 1
    text = ""
    for c in reversed(rezultat):
        text += str(c)
    return elimina_zerouri(text)

def main():
    try:
        a, b = citeste_numere()
    except ValueError as e:
        print(f"Eroare: {e}")
        return
    print("Primul număr:", a)
    print("Al doilea număr:", b)
    print("Suma:", aduna(a, b))
    print("Produsul:", inmulteste(a, b))

if __name__ == "__main__":
    main()