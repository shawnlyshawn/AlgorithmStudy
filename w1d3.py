tri = 0
tri_lst = []
for i in range(1, 45):
    tri += i
    tri_lst.append(tri)

sum = 0
sum_lst = []
for tri_a in tri_lst:
    for tri_b in tri_lst:
        for tri_c in tri_lst:
            sum = tri_a + tri_b + tri_c
            if (sum not in sum_lst) and sum<=1000 :
                sum_lst.append(sum)
            else:
                continue

t = int(input())

for i in range(0, t):
    k = int(input())
    if k in sum_lst:
        print(1)
    else:
        print(0)