def primes(kmax: int) -> list:
    if kmax > 1000:
        kmax = 1000
    result = []
    for num in range(kmax):
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result.append(num)
    return result


if __name__ == '__main__':
    ret=primes(50)
    print(f'primes:{ret}')