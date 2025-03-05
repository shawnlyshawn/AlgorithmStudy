# 1000 이하 삼각수
tri = 0
tri_lst = []
for i in range(1, 45):
    tri += i
    tri_lst.append(tri)

# print(tri_lst) # 굿~

# k보다 작은 삼각수만 봐, 하나하나 맞춰가면 되지 않을까? 최소 1+1+(본인)
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

print(len(sum_lst))

# input 처리
t = int(input())

for i in range(0, t):
    k = int(input())
    if k in sum_lst:
        print(1)
    else:
        print(0)