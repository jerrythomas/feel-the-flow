from multiprocessing import Pool

def calculate_square(num):
    return num * num

def calculate_square_mp(data):
    pool = Pool()
    results = pool.map(calculate_square, data)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    result = calculate_square_mp(data)
    print(result)
