from prefect import flow, task

@task
def print_result(nums):
    print('Result: ',nums)

@task
def calculate_square(num):
    return num*num

@flow
def map_flow(nums):
    squared_nums = calculate_square.map(nums)
    print_result(squared_nums)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    map_flow(data)
