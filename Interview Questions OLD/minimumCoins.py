import sys

def minimumCoinBottomUp(total, coins):
    T = [0] * (total + 1)
    R = [0] * (total + 1)
    T[0] = 0
    for i in range(1, total + 1): 
        T[i] = sys.maxsize
        R[i] = -1

    solution = [[]] * (total + 1)
    for j in range(0, len(coins)):
        for i in range(1, total + 1):
            if i >= coins[j]:
                if T[i - coins[j]] + 1 < T[i]:
                    T[i] = 1 + T[i - coins[j]]
                    R[i] = j
                    solution[i].append(coins[j])
    return solution[i]


# print(minimumCoinBottomUp(50, [1,5,10,25]))


def minCoins(coins, m, V, solution):
 
    # base case
    if (V == 0):
        return 0
 
    # Initialize result
    res = sys.maxsize
     
    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res, sol = minCoins(coins, m, V-coins[i], solution)
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
                sol.append(coins[i])
 
    return res, sol


# res, sol = minCoins([1,5,10,25], 4, 11, [])
# for i in sol:
#     print(i)


def _get_change_making_matrix(set_of_coins, r: int):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r + 1):
        m[0][i] = float('inf')  # By default there is no way of making change
    return m

def change_making(coins, n: int):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations.
    """
    m = _get_change_making_matrix(coins, n)
    for c, coin in enumerate(coins, 1):
        for r in range(1, n + 1):
            # Just use the coin
            if coin == r:
                m[c][r] = 1
            # coin cannot be included.
            # Use the previous solution for making r,
            # excluding coin
            elif coin > r:
                m[c][r] = m[c - 1][r]
            # coin can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coin).
            # 2. Using the previous solution for making r - coin (without
            #      using coin) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coin])
    return m[-1][-1]


print(change_making([1,5,10,25], 50))