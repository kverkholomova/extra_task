numer_przedmiotu = [1, 2, 3, 4, 5, 6]
wartosc = [6, 4, 5, 7, 10, 2]
waga = [6, 2, 3, 2, 3, 1]

result = []
for i in range(1, 24):
    if waga[0] > i:
        result.append(0)
    elif waga[0] <= i and waga[0] * 2 > i:
        result.append(wartosc[0])
    elif waga[0] * 2 <= i and waga[0] * 3 > i:
        result.append(wartosc[0] * 2)
    elif waga[0] * 3 <= i and waga[0] * 4 > i:
        result.append(wartosc[0] * 3)
print("We have only one object:", result)

result_1 = []
for i in range(1, 24):
    if waga[0] > i and waga[1] > i:
        result_1.append(0)
    elif waga[0] <= i or waga[1] <= i:
        if waga[0] > waga[1]:
            if waga[1] * 2 > i:
                result_1.append(wartosc[1])
            elif waga[1] * 2 <= i and waga[1] * 3 > i:
                result_1.append(wartosc[1] * 2)
            elif waga[1] * 3 <= i and waga[1] * 4 > i:
                result_1.append(wartosc[1] * 3)
            elif waga[1] * 4 <= i and waga[1] * 5 > i:
                result_1.append(wartosc[1] * 4)
            elif waga[1] * 5 <= i and waga[1] * 6 > i:
                result_1.append(wartosc[1] * 5)
            elif waga[1] * 6 <= i and waga[1] * 7 > i:
                result_1.append(wartosc[1] * 6)
            elif waga[1] * 7 <= i and waga[1] * 8 > i:
                result_1.append(wartosc[1] * 7)
            elif waga[1] * 8 <= i and waga[1] * 9 > i:
                result_1.append(wartosc[1] * 8)
            elif waga[1] * 9 <= i and waga[1] * 10 > i:
                result_1.append(wartosc[1] * 9)
            elif waga[1] * 10 <= i and waga[1] * 11 > i:
                result_1.append(wartosc[1] * 10)
            elif waga[1] * 11 <= i and waga[1] * 12 > i:
                result_1.append(wartosc[1] * 11)
print("We have two objects:", result_1)


def find_number():
    result_2 = []
    numer = 0
    wart = 0
    for j in range(1, 24):
        for r in range(1, 12):
            if j % (waga[0] * r) == 0:
                numer = waga[0] * r
                wart = wartosc[0] * r
                # continue
            if j % (waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r
                    wart1 = wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r
                    wart = wartosc[1] * r
                # continue
            if j % (waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[2] * r
                    wart1 = wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[2] * r
                    wart = wartosc[2] * r
                # numer = waga[2]
                # wart = wartosc[2]
                # continue
            if j % (waga[0] + waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[1] * r
                    wart1 = wartosc[0] + wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[1] * r
                    wart = wartosc[0] + wartosc[1] * r
                # continue
            if j % (waga[1] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] + waga[2] * r
                    wart1 = wartosc[1] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] + waga[2] * r
                    wart = wartosc[1] + wartosc[2] * r
                # continue
            if j % (waga[0] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[2] * r
                    wart1 = wartosc[0] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[2] * r
                    wart = wartosc[0] + wartosc[2] * r
                # continue
            if j % (waga[1] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r + waga[2]
                    wart1 = wartosc[1] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r + waga[2]
                    wart = wartosc[1] * r + wartosc[2]
                # continue
        result_2.append(wart)

    return result_2


print("We have three objects:", find_number())


def find_number_4():
    result_2 = []
    numer = 0
    wart = 0
    for j in range(1, 24):
        for r in range(1, 12):
            if j % (waga[0] * r) == 0:
                numer = waga[0] * r
                wart = wartosc[0] * r
                # continue
            if j % (waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r
                    wart1 = wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r
                    wart = wartosc[1] * r
                # continue
            if j % (waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[2] * r
                    wart1 = wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[2] * r
                    wart = wartosc[2] * r
            if j % (waga[3] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r
                    wart1 = wartosc[3] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r
                    wart = wartosc[3] * r
            if j % (waga[0] + waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[1] * r
                    wart1 = wartosc[0] + wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[1] * r
                    wart = wartosc[0] + wartosc[1] * r
            if j % (waga[0] + waga[3] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[3] * r
                    wart1 = wartosc[0] + wartosc[3] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[3] * r
                    wart = wartosc[0] + wartosc[3] * r
            if j % (waga[1] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] + waga[2] * r
                    wart1 = wartosc[1] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] + waga[2] * r
                    wart = wartosc[1] + wartosc[2] * r
            if j % (waga[3] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] + waga[2] * r
                    wart1 = wartosc[3] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] + waga[2] * r
                    wart = wartosc[3] + wartosc[2] * r
                # continue
            if j % (waga[0] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[2] * r
                    wart1 = wartosc[0] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[2] * r
                    wart = wartosc[0] + wartosc[2] * r
                # continue
            if j % (waga[1] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r + waga[2]
                    wart1 = wartosc[1] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r + waga[2]
                    wart = wartosc[1] * r + wartosc[2]
            if j % (waga[3] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r + waga[2]
                    wart1 = wartosc[3] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r + waga[2]
                    wart = wartosc[3] * r + wartosc[2]
                # continue
        result_2.append(wart)

    return result_2


print("We have four objects:", find_number_4())


def find_number_5():
    result_2 = []
    numer = 0
    wart = 0
    for j in range(1, 24):
        for r in range(1, 12):
            if j % (waga[0] * r) == 0:
                numer = waga[0] * r
                wart = wartosc[0] * r
                # continue
            if j % (waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r
                    wart1 = wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r
                    wart = wartosc[1] * r
                # continue
            if j % (waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[2] * r
                    wart1 = wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[2] * r
                    wart = wartosc[2] * r
            if j % (waga[3] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r
                    wart1 = wartosc[3] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r
                    wart = wartosc[3] * r
            if j % (waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[4] * r
                    wart1 = wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[4] * r
                    wart = wartosc[4] * r
            if j % (waga[0] + waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[1] * r
                    wart1 = wartosc[0] + wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[1] * r
                    wart = wartosc[0] + wartosc[1] * r
            if j % (waga[0] + waga[3] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[3] * r
                    wart1 = wartosc[0] + wartosc[3] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[3] * r
                    wart = wartosc[0] + wartosc[3] * r
            if j % (waga[1] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] + waga[2] * r
                    wart1 = wartosc[1] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] + waga[2] * r
                    wart = wartosc[1] + wartosc[2] * r
            if j % (waga[1] + waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] + waga[4] * r
                    wart1 = wartosc[1] + wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] + waga[4] * r
                    wart = wartosc[1] + wartosc[4] * r
            if j % (waga[3] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] + waga[2] * r
                    wart1 = wartosc[3] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] + waga[2] * r
                    wart = wartosc[3] + wartosc[2] * r

            if j % (waga[3] + waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] + waga[4] * r
                    wart1 = wartosc[3] + wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] + waga[4] * r
                    wart = wartosc[3] + wartosc[4] * r
            if j % (waga[0] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[2] * r
                    wart1 = wartosc[0] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[2] * r
                    wart = wartosc[0] + wartosc[2] * r
                # continue
            if j % (waga[0] + waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[4] * r
                    wart1 = wartosc[0] + wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[4] * r
                    wart = wartosc[0] + wartosc[4] * r
            if j % (waga[1] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r + waga[2]
                    wart1 = wartosc[1] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r + waga[2]
                    wart = wartosc[1] * r + wartosc[2]
            if j % (waga[1] * r + waga[4]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r + waga[4]
                    wart1 = wartosc[1] * r + wartosc[4]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r + waga[4]
                    wart = wartosc[1] * r + wartosc[4]
            if j % (waga[3] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r + waga[2]
                    wart1 = wartosc[3] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r + waga[2]
                    wart = wartosc[3] * r + wartosc[2]
            if j % (waga[3] * r + waga[4]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r + waga[4]
                    wart1 = wartosc[3] * r + wartosc[4]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r + waga[4]
                    wart = wartosc[3] * r + wartosc[4]
                # continue
        result_2.append(wart)

    return result_2


print("We have five objects:", find_number_5())


def find_number_6():
    result_2 = []
    numer = 0
    wart = 0
    for j in range(1, 24):
        for r in range(1, 12):
            if j % (waga[0] * r) == 0:
                numer = waga[0] * r
                wart = wartosc[0] * r
                # continue
            if j % (waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r
                    wart1 = wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r
                    wart = wartosc[1] * r
                # continue
            if j % (waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[2] * r
                    wart1 = wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[2] * r
                    wart = wartosc[2] * r
            if j % (waga[3] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r
                    wart1 = wartosc[3] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r
                    wart = wartosc[3] * r
            if j % (waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[4] * r
                    wart1 = wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[4] * r
                    wart = wartosc[4] * r
            if j % (waga[5] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[5] * r
                    wart1 = wartosc[5] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[5] * r
                    wart = wartosc[5] * r
            if j % (waga[0] + waga[1] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[1] * r
                    wart1 = wartosc[0] + wartosc[1] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[1] * r
                    wart = wartosc[0] + wartosc[1] * r
            if j % (waga[0] + waga[3] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[3] * r
                    wart1 = wartosc[0] + wartosc[3] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[3] * r
                    wart = wartosc[0] + wartosc[3] * r
            if j % (waga[1] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] + waga[2] * r
                    wart1 = wartosc[1] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] + waga[2] * r
                    wart = wartosc[1] + wartosc[2] * r
            if j % (waga[1] + waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] + waga[4] * r
                    wart1 = wartosc[1] + wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] + waga[4] * r
                    wart = wartosc[1] + wartosc[4] * r
            if j % (waga[3] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] + waga[2] * r
                    wart1 = wartosc[3] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] + waga[2] * r
                    wart = wartosc[3] + wartosc[2] * r

            if j % (waga[3] + waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] + waga[4] * r
                    wart1 = wartosc[3] + wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] + waga[4] * r
                    wart = wartosc[3] + wartosc[4] * r
            if j % (waga[0] + waga[2] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[2] * r
                    wart1 = wartosc[0] + wartosc[2] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[2] * r
                    wart = wartosc[0] + wartosc[2] * r
                # continue
            if j % (waga[0] + waga[4] * r) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[0] + waga[4] * r
                    wart1 = wartosc[0] + wartosc[4] * r
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[0] + waga[4] * r
                    wart = wartosc[0] + wartosc[4] * r
            if j % (waga[1] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r + waga[2]
                    wart1 = wartosc[1] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r + waga[2]
                    wart = wartosc[1] * r + wartosc[2]
            if j % (waga[1] * r + waga[4]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[1] * r + waga[4]
                    wart1 = wartosc[1] * r + wartosc[4]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[1] * r + waga[4]
                    wart = wartosc[1] * r + wartosc[4]
            if j % (waga[3] * r + waga[2]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r + waga[2]
                    wart1 = wartosc[3] * r + wartosc[2]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r + waga[2]
                    wart = wartosc[3] * r + wartosc[2]
            if j % (waga[3] * r + waga[4]) == 0:
                if numer != 0 and wart != 0:
                    numer1 = waga[3] * r + waga[4]
                    wart1 = wartosc[3] * r + wartosc[4]
                    if wart1 > wart:
                        wart = wart1
                else:
                    numer = waga[3] * r + waga[4]
                    wart = wartosc[3] * r + wartosc[4]
                # continue
        result_2.append(wart)

    return result_2


print("We have six objects:", find_number_6())
