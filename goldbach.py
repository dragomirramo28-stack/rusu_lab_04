def este_prim(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def citeste_numar_par():
    while True:
        text = input("Introduceți un număr par mai mare decât 2: ")
        try:
            n = int(text)
        except ValueError:
            print("Valoare invalidă: introduceți un număr întreg.")
            continue
        if n <= 2:
            print("Valoare invalidă: numărul trebuie să fie mai mare decât 2.")
        elif n % 2 != 0:
            print("Valoare invalidă: numărul trebuie să fie par.")
        else:
            return n

def perechi_goldbach(n):
    perechi = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            perechi.append((p, q))
    return perechi


def main():
    n = citeste_numar_par()
    perechi = perechi_goldbach(n)
    print(f"Descompuneri ale lui {n} ca sumă de două numere prime:")
    for p, q in perechi:
        print(f"{n} = {p} + {q}")


if __name__ == "__main__":
    main()    