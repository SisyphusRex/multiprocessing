#!/usr/bin/env python

import multiprocessing
import os


def process_slice(data_slice):
    # Perform operations on the data slice
    print(data_slice)


if __name__ == "__main__":
    data = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
    ]
    num_processes = os.cpu_count()
    print(num_processes)
    # Split the data into slices
    chunk_size = len(data) // num_processes
    slices = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Create processes and pass slices
    processes = []
    for slice_data in slices:
        p = multiprocessing.Process(target=process_slice, args=(slice_data,))
        processes.append(p)
        p.start()

    # Wait for processes to complete
    for p in processes:
        p.join()
