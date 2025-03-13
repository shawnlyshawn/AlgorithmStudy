import sys

def b_check(board):
    cnt = 0
    for i in range(5):
        check_a = 0
        if board[5*i : 5*i+5] == ['0', '0', '0', '0', '0']:
            cnt += 1
            if cnt >= 3:
                return True
            
        for j in range(5):
            if board[i+5*j] != '0':
                break
            else:
                check_a += 1
        if check_a == 5:
            cnt += 1
            if cnt >= 3:
                return True

    check_b = 0
    for i in range(5):
        if board[4*(i+1)] != '0':
            break
        else:
            check_b += 1
    if check_b == 5:
        cnt += 1
        if cnt >= 3:
            return True

    check_c = 0
    for i in range(5):
        if board[6*i] != '0':
            break
        else:
            check_c += 1
    if check_c == 5:
        cnt += 1
        if cnt >= 3:
           return True

    return False

board = []
for i in range(5):
    board.extend(sys.stdin.readline().split())

mc = []
for i in range(5):
    mc.extend(sys.stdin.readline().split())

bingo = False
for i in range(25):
    board[board.index(mc[i])] = '0'
    bingo = b_check(board)
    if bingo:
        print(i+1)
        break