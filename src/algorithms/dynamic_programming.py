from __future__ import annotations


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def matrix_sum(matrix: list[list[int]]) -> list[int]:
    result = []
    for row in matrix:
        row_sum = sum(row)
        if row_sum > 0:
            result.append(row_sum)
    return result


def matrix_chain_order(matrices: list[tuple[int, int]]) -> int:
    """
    Find the minimum number of operations needed to multiply a chain of matrices.

    Args:
        matrices: A list of matrix dimensions as tuples (rows, cols)

    Returns:
        Minimum number of operations
    """
    n = len(matrices)

    def dp(i: int, j: int) -> int:
        if i == j:
            return 0

        min_ops = float("inf")

        for k in range(i, j):
            cost = (
                dp(i, k)
                + dp(k + 1, j)
                + matrices[i][0] * matrices[k][1] * matrices[j][1]
            )
            min_ops = min(min_ops, cost)

        return min_ops

    return dp(0, n - 1)


def coin_change(coins: list[int], amount: int, index: int) -> int:
    memo: dict[tuple[int, int], int] = {}

    def dp(amount: int, index: int) -> int:
        if amount == 0:
            return 1
        if amount < 0 or index >= len(coins):
            return 0
        key = (amount, index)
        if key in memo:
            return memo[key]
        res = dp(amount - coins[index], index) + dp(amount, index + 1)
        memo[key] = res
        return res

    return dp(amount, index)


def knapsack(weights: list[int], values: list[int], capacity: int, n: int) -> int:
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)

    return max(
        values[n - 1] + knapsack(weights, values, capacity - weights[n - 1], n - 1),
        knapsack(weights, values, capacity, n - 1),
    )
