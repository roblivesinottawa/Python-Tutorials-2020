# def generate_evens():
#     _number = []
#     for number in range(1, 50):
#         if number % 2 == 0:
#             _number.append(number)
#     return _number


# print(generate_evens())


def generate_odds():
    odds = []
    for nums in range(1, 50):
        if nums % 2 != 0:
            odds.append(nums)
    return odds


print(generate_odds())
