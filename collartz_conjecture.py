def conjecture(list_, num):
    list_.append(num)
    if num == 1:
        return True
    elif num % 2 == 0:  # 짝수
        return conjecture(list_, num // 2)
    elif num % 2 == 1:  # 홀수
        return conjecture(list_, num * 3 + 1)
    return False


if __name__ == '__main__':
    index = 2
    while True:
        temp_list = list()
        if conjecture(temp_list, index):
            print(f'{index}: TRUE, {temp_list}')
        else:
            break
        index += 1
