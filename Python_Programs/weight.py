def weight_check():
    weight = int(input("Enter weight: "))
    unit = input("(K)g or (L)bs ")
    if unit.upper() == 'K':
        converted = weight / 0.45
        return f"weight in Lbs: {str(converted)}"
    else:
        converted = weight * 0.45
        return f"weight in Kgs: {str(converted)}"


# result = weight_check()
# print(result)