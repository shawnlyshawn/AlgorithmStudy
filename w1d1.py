N = input() # 숫자 입력해도 문자열로 저장됨

ans = 0
for i in range(1, int(N)):
    check = i
    for j in str(i):
        check = check + int(j)
        # print(f"i is {i} and check is {check}")
    if check == int(N):
        ans = i
        break

print(ans)

# -----------------------------------------------

# length = len(N)
# n = int(N)
# lst = []
#
# # lst: 분해합의 각 자리별 숫자
# for i in range(length-1, 0, -1):
#     de = 10 ** i
#     quo = n // de
#     lst.append(quo)
#     n = n - de*quo
#     if (i == 1):
#         lst.append(n)
# # len(N) >= i > -1
#
# print(f"list: {lst}")