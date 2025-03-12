import sys

def junhyeon(money, stock_prices):
    n_cnt = 0
    for i in range(13):
        if money < stock_prices[i]:
            continue
        else:
            n = money // stock_prices[i]
            n_cnt += n
            money -= n * stock_prices[i]

    result = stock_prices[13] * n_cnt + money
    return result

def seongmin(money, stock_prices):
    n_cnt = 0
    buy = 0
    sell = 0

    for i in range(1, 13):
        if stock_prices[i-1] == stock_prices[i]:
            buy = 0
            sell = 0
        elif stock_prices[i-1] < stock_prices[i]:
            buy = 0
            sell += 1
        else:
            sell = 0
            buy += 1

        if sell >= 3:
            money += n_cnt * stock_prices[i]
            n_cnt = 0
        elif buy >= 3 and money >= stock_prices[i]:
            n = money // stock_prices[i]
            n_cnt += n
            money -= n * stock_prices[i]
        else:
            continue
        
    result = stock_prices[13] * n_cnt + money
    return result

if __name__ == "__main__":
    money = int(sys.stdin.readline().rstrip())
    stock_prices = list(map(int, sys.stdin.readline().split()))
    jun_result = junhyeon(money, stock_prices)
    seong_result = seongmin(money, stock_prices)
    if jun_result == seong_result:
        print("SAMESAME")
    elif jun_result > seong_result:
        print("BNP")
    else:
        print("TIMING")