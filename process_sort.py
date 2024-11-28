
import multiprocessing
import os

def shared_memory_process_test(collection: list[int]) -> list[int]:
    """method to pass shared memory array to processes"""
    processor_count: int = os.cpu_count()
    collection_length = len(collection)
    chunk_size: int = collection_length // processor_count
    shared_collection = multiprocessing.Array('i', collection, lock=True)

    processes = []
    for core in range(processor_count):
        p = multiprocessing.Process(target=do_process, args=(shared_collection, core * chunk_size, chunk_size,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    sorted_collection = []
    for i in shared_collection:
        sorted_collection.append(i)
    return sorted_collection

def do_process(shared_collection, process_index, chunk_size):
    """do stuff with shared memory collection"""
    print(f"chunk size: {chunk_size}")
    first_str = ""
    for i in shared_collection:
        first_str += str(i)
        first_str += " "
    print(first_str)
    shared_collection[process_index : process_index + chunk_size] = sorted(shared_collection[process_index : process_index + chunk_size])
    second_str = ""
    for i in shared_collection:
        second_str += str(i)
        second_str += " "
    print(second_str)



