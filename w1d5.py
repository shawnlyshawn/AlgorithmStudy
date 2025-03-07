import sys

n, m = map(int, sys.stdin.readline().split())

nm_board = []
for i in range(0, n):
    row = input()
    nm_board.append(row)
 
truncated_boards = []
for i in range(n-7):
    for j in range(m-7):
        truncated_board = [row[j:j+8] for row in nm_board[i:i+8]]
        truncated_boards.append(truncated_board)

ans_list = []
for truncated_board in truncated_boards:
    cnt_w = 0
    cnt_b = 0

    for i in range(0, 8):
        if not (i%2):
            for j in range(0, 8): # WBWB

                if not (j%2) and (truncated_board[i][j] != 'W'):
                    cnt_w += 1
                elif (j%2) and (truncated_board[i][j] != 'B'):
                    cnt_w += 1

            for j in range(0, 8): # BWBW

                if not (j%2) and (truncated_board[i][j] != 'B'):
                    cnt_b += 1
                elif (j%2) and (truncated_board[i][j] != 'W'):
                    cnt_b += 1

        else:
            for j in range(0, 8): # WBWB

                if not (j%2) and (truncated_board[i][j] != 'W'):
                    cnt_b += 1
                elif (j%2) and (truncated_board[i][j] != 'B'):
                    cnt_b += 1

            for j in range(0, 8): # BWBW

                if not (j%2) and (truncated_board[i][j] != 'B'):
                    cnt_w += 1
                elif (j%2) and (truncated_board[i][j] != 'W'):
                    cnt_w += 1

    ans_list.append(min(cnt_w, cnt_b))

print(min(ans_list))