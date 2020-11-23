import copy

free_areas = []
num = int(input())
for i in range(num):
    start, size = input().split()
    free_areas.append([int(start), int(size)])

requests = []
num = int(input())
for i in range(num):
    size = int(input())
    requests.append(size)


def free(areas, size):
    areas.sort(key=lambda x: x.start)
    start = 0
    end = max(areas, key=lambda x: x[0]+x[1])
    i, j = start, end
    for area in areas:
        if start < area[0]:
            releaseable_size = area[0] - start
            if size <= releaseable_size:
                areas.append(start, size)
            else:
                area[0] -= releaseable_size
                area[1] += releaseable_size
                size -= releaseable_size
                start = area[0] + area[1]


def adaption(areas, requests, key=None, reverse=False):
    for request in requests:
        isAllocated = False
        for area in areas:
            if area[1] >= request:
                area[0] += request
                area[1] -= request
                isAllocated = True
                print("Allocating {:3d} bytes, success!".format(request))
                if key:
                    areas.sort(key=key, reverse=reverse)
                break
        if not isAllocated:
            # print(request, areas)
            print("There is not enough free space to allocate {} bytes!".format(request))
    print_res(areas)

def print_res(areas):
    print("Free space:")
    for area in areas:
        print("start: {} end: {} size: {}".format(area[0], area[0]+area[1], area[1]))

def ff(free_areas, requests):
    print("\nFirst Fit")
    areas = copy.deepcopy(free_areas)
    adaption(areas, requests)


def bf(free_areas, requests):
    print("\nBest Fit")
    areas = copy.deepcopy(free_areas)
    areas.sort(key = lambda x: x[1])
    adaption(areas, requests, key=lambda x: x[1])

def wf(free_areas, requests):
    print("\nWorst Fit")
    areas = copy.deepcopy(free_areas)
    areas.sort(key = lambda x: x[1], reverse=True)
    adaption(areas, requests, key=lambda x: x[1], reverse=True)



ff(free_areas, requests)
bf(free_areas, requests)
wf(free_areas, requests)
