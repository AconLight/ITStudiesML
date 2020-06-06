import time
from multiprocessing.pool import Pool


def calcNum(n,x):  # some arbitrary, time-consuming calculation on a number
    print("Calcs Started on ", n)
    print(x)
    m = n
    for i in range(5000000):
        m += i % 25
        if m > n * n:
            m /= 2
    return m


if __name__ == "__main__":
    t0 = time.time()
    p = Pool(processes=12)

    nums = [12, 25, 76, 38, 8, 2, 5]
    xs = [0, 1, 2, 3, 4, 5, 6]

    result = p.map(calcNum, nums)
    p.close()
    p.join()

    print(result)
    t1 = time.time()
    print(t1 - t0)
