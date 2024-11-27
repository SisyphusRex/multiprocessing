#!/usr/bin/env python
import multiprocessing


def square(x):
    return x * x


if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)
