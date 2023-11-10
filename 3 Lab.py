def remove_values(a, b):
    result = []
    for element in a:
        found = False
        for item in b:
            if element == item:
                found = True
                break
        if not found:
            result.append(element)
    return result


print(remove_values([1, 2, 3, 7, 24], [1, 7, 25, 3]))
print(remove_values([-5, 20, 3, -10], [1, 2, 3, -5, 20, -10]))
