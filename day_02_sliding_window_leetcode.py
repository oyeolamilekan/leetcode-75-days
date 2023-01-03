from typing import List


def max_profit(prices: List[int], ):
    """
    using pointers to solve this problem
    """

    left = 0 # left is buying
    right = 1 # right is selling
    max_p = 0

    while right < len(prices):
        print(f"buying price {prices[left]}")
        print(f"selling price {prices[right]}")
        print("\n")
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_p = max(max_p, profit)
        else:
            print("shifting")
            print(prices[left])
            print(prices[right])
            print("\n")
            left = right
        right += 1

    return max_p

print(max_profit([7, 1, 9, 3, 6, 10, 4]))
