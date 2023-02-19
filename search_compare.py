import time
import random


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False
    start = time.time()
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    time_spent = time.time() - start
    return found, time_spent


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    start = time.time()
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    time_spent = time.time() - start
    return found, time_spent


def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False
    start = time.time()
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    time_spent = time.time() - start
    return found, time_spent
    
    
def binary_search_recursive(a_list,item):
    start = time.time()
    if len(a_list) == 0:
        return False, (time.time() - start)
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True, (time.time() - start)
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

def run_searches(the_size):
    sequential_total_time = 0
    ordered_sequential_total_time = 0
    binary_iterative_total_time = 0
    binary_recursive_total_time = 0
    for i in range(100):
        mylist = get_me_random_list(the_size)
        sequential_result = sequential_search(mylist, 99999)
        sequential_total_time += sequential_result[1]
        mylist_sorted = sorted(mylist)
        ordered_sequential_result = ordered_sequential_search(mylist_sorted, 99999)
        ordered_sequential_total_time += ordered_sequential_result[1]
        binary_iterative_result = binary_search_iterative(mylist_sorted, 99999)
        binary_iterative_total_time += binary_iterative_result[1]
        binary_recursive_result = binary_search_recursive(mylist_sorted, 99999)
        binary_recursive_total_time += binary_recursive_result[1]
    print(f"Sequential Search took {(sequential_total_time/100):10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Ordered Sequential Search took {(ordered_sequential_total_time/100):10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Iterative Binary Search took {(binary_iterative_total_time/100):10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Recursive Binary Search took {(binary_recursive_total_time/100):10.7f} seconds to run, on average for a list of {the_size} elements")



if __name__ == "__main__":
    """Main entry point"""
    run_searches(500)
    run_searches(1000)
    run_searches(10000)

