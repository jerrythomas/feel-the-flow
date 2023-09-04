def calculate_square(num):
    return num * num

def calculate_square_sq(numbers):
    results = []
    for num in numbers:
        results.append(calculate_square(num))
    return results

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    result = calculate_square_sq(data)
    print(result)
