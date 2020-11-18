from collections import deque
from copy import deepcopy

PHYSICAL_PAGE_NUM = 4

requests = input().split()
requests = [int(x) for x in requests]

def fifo(requests):
    print("\nFirst In First Out")
    pagefault_times = 0
    pp = deque(list(), maxlen=PHYSICAL_PAGE_NUM)
    for request in requests:
        if request not in pp:
            if len(pp) == PHYSICAL_PAGE_NUM:
                print("Miss page {} swap out page {}".format(request, pp[0]))
            else:
                print("Miss page {} swap in empty physical memory".format(request))
            pp.append(request)
            pagefault_times += 1
    print_analysis(pagefault_times)

def lru(requests):
    print("\nLeast Recently Used")
    pagefault_times = 0
    pp = deque(list(), maxlen=PHYSICAL_PAGE_NUM)
    for request in requests:
        if request not in pp:
            if len(pp) == PHYSICAL_PAGE_NUM:
                print("Miss page {} swap out page {}".format(request, pp[0]))
            else:
                print("Miss page {} swap in empty physical memory".format(request))
            pp.appendleft(request)
            pagefault_times += 1
        else:
            pp.remove(request)
            pp.appendleft(request)
    print_analysis(pagefault_times)

def print_analysis(pagefault_times):
    print("pagefault times: {}".format(pagefault_times))
    print("pagefault probabilities: {}".format(pagefault_times / len(requests)))

print("Request sequence:")
print(requests)

fifo(requests)
lru(requests)