from operator import index


A = [310,315,275,295,260,270,230,255,250]
# A = [7,1,5,3,6,4]

def calculateProfitWhenBuyingNow(A,index):
    buyingPrice = A[index]
    maxProfit = 0
    sellAt = index
    for i in range(index+1, len(A)):
        sellingPrice = A[i]
        # if sellingPrice > buyingPrice:
        #     profit = sellingPrice - buyingPrice
        #     maxProfit = profit
        #     sellAt += i
        profit = sellingPrice - buyingPrice
        if profit > maxProfit:
            maxProfit = profit
            sellAt = i
    return maxProfit, sellAt

def stockBuy(A):
    max_profit = None
    buy = None
    sell = None
    result =[]
    for i, v in enumerate(A):
        profit, sellAt = calculateProfitWhenBuyingNow(A, i)
        result.append(profit)
        if max_profit is None or profit > max_profit:
            max_profit = profit
            buy = i
            sell = sellAt
    print(result)
    return max_profit, buy, sell

def stock_price_2(A):
    l, r = 0, 1
    max_profit = 0
    while r < len(A):
        if A[l] < A[r]:
            profit = A[r] - A[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    print(max_profit)

def buy_and_sell(A):
    max_profit, min_price_so_far = 0.0, float('inf')
    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
        print(f"max profit: {max_profit} max sell today: {max_profit_sell_today}  min price so far {min_price_so_far}")
    return max_profit

ans = buy_and_sell(A)
print(ans)