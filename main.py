def zpracuj_usek(start, konec, body, minimum, body_minima):
    if (start == konec):
        minimum = float("inf")
        for i in range(1, len(body)):
            vzdalenost = body[i][1] - body[i-1][1]
            if (vzdalenost < minimum):
                minimum = vzdalenost
                body_minima = (body[i-1][2], body[i][2])
    else:
        stred = (start + konec) // 2
        body[]
    return minimum, body_minima
def main():
    N = int(input())
    body = []
    for i in range(N):
        x, y = [int(val) for val in input().split()]
        # x, y, poradi na vstupu
        body.append((x, y, i))
    body.sort()
    skupiny = [[]]
    posledni_x = body[0][0]
    for bod in body:
        if (bod[0] == posledni_x):
            skupiny[-1].append(bod)
        else:
            skupiny.append([bod])
            posledni_x = bod[0]
    delka = 1
    while(delka <= len(skupiny)):
        for start in range(0, len(skupiny), delka):
            konec = start + delka - 1
            if (konec >= len(skupiny)):
                break

        delka *= 2

if __name__ == '__main__':
    main()