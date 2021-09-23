def average(array):
    array = set(array)
    sum = 0.0
    for i in array:
        sum = sum + i

    return sum / len(array)

