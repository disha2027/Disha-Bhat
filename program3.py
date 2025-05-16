def generate_odd_series_conditionally(a):
    result = []
    if a % 2 != 0:  # Only for odd inputs
        for i in range(a):
            result.append(2 * i + 1)
    else:
        for i in range(a - 1):
            if i % 2 == 0:
                result.append(2 * i + 1)
    return result
