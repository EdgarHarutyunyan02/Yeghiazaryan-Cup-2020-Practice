MAX = 10 ** 6
START = 1


def guess(start, end=MAX):
    current_guess = (start + end) // 2
    print(current_guess)
    answer = int(input())
    if answer < 0:
        return guess(start, current_guess)

    if answer > 0:
        return guess(current_guess, end)

    return current_guess


N = int(input())

guess(START, N+1)
