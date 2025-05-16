def count_multiples(data):
    counts = {i: 0 for i in range(1, 10)}
    for num in data:
        for i in range(1, 10):
            if num % i == 0:
                counts[i] += 1
    return counts
