def coin_sum_r(total, coins):
    if len(coins) == 1:
        return 1
    elif total < coins[-1]:
        return coin_sum_r(total, coins[:-1])
    else:
        return (coin_sum_r(total-coins[-1], coins) + 
                coin_sum_r(total, coins[:-1]))

#coins_a = (1, 5, 10, 25)   
#print(coin_sum(100, coins_a))# 242

coins_b = (1, 5, 10, 25, 50, 100)  
print(coin_sum(100000, coins_b))# 13398445413854501

#coins_england = (1, 2, 5, 10, 20, 50, 100, 200)
#print(coin_sum(600, coins_england))   # 73682
