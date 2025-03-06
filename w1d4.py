import sys

def kkeut(n):
    cnt = 0

    for key, value in kkeuts.items():
        if key >= n:
            break
        else:
            for pair in value:
                if a in pair:
                    cnt += 2
                elif b in pair:
                    cnt += 2
                else:
                    cnt += 4

    print("{:.3f}".format(cnt / 153))

kkeuts = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

for j in range(1, 11):
    for k in range(j, 11):
        if j != k:
            kkeuts[int(str(j + k)[-1])].append([j, k])

a, b = map(int, sys.stdin.readline().split())

if a == b:
    if a == 10:
        print("{:.3f}".format(1.000))
    elif a == 9: # 9, 9
        print("{:.3f}".format(152 / 153))
    elif a == 8:
        print("{:.3f}".format(151 / 153))
    elif a == 7:
        print("{:.3f}".format(150 / 153))
    elif a == 6:
        print("{:.3f}".format(149 / 153))
    elif a == 5:
        print("{:.3f}".format(148 / 153))
    elif a == 4:
        print("{:.3f}".format(147 / 153))
    elif a == 3:
        print("{:.3f}".format(146 / 153))
    elif a == 2:
        print("{:.3f}".format(145 / 153))
    elif a == 1:
        print("{:.3f}".format(144 / 153))

else:
    if (str(a+b)[-1]) == '9':
        kkeut(9)
    elif (str(a+b)[-1]) == '8':
        kkeut(8)
    elif (str(a+b)[-1]) == '7':
        kkeut(7)
    elif (str(a+b)[-1]) == '6':
        kkeut(6)
    elif (str(a+b)[-1]) == '5':
        kkeut(5)
    elif (str(a+b)[-1]) == '4':
        kkeut(4)
    elif (str(a+b)[-1]) == '3':
        kkeut(3)
    elif (str(a+b)[-1]) == '2':
        kkeut(2)
    elif (str(a+b)[-1]) == '1':
        kkeut(1)
    else:
        print("{:.3f}".format(0.000))