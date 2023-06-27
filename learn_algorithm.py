import datetime
import time


def main():

    binary_search(12354)


def time_checker(func):
    def wrapper(*args):
        print(f'{func.__name__} 시작')
        start_time = time.time()
        func(*args)
        end_time = time.time()
        required_second_time = (end_time - start_time)
        print(f'함수종료 | 소요시간 : {required_second_time:.6f}s')

    return wrapper


# 속도 테스트
@time_checker
def function_1():
    list_ = list(range(100000))


@time_checker
def function_2():
    list_ = [x for x in range(100000)]


@time_checker
def function_3():
    list_ = list()
    for i in range(100000):
        list_.append(i)


@time_checker
def find_algorithm_with_for(value):
    list_ = list(range(100000))
    for i in list_:
        if i == value:
            print(i)
            break


@time_checker
def binary_search(target_value):
    list_ = range(100000)
    low = 0
    high = len(list_)
    while low <= high:
        mid = low + (high - low) // 2
        if list_[mid] == target_value:
            print(mid)
            return
        elif list_[mid] < target_value:
            low = mid + 1
        else:
            high = mid - 1
    raise "No match Element!"



if __name__ == '__main__':
    main()
