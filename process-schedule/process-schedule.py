import copy
from collections import deque

Timeslice = 1

class Process:
    num = 0
    # status = 1  # 1 ready, 2 waiting, 3 running. it's no need to use this state
    priority = 0
    need_time = 0
    enter_time = 0
    start_time = -1
    complete_time = 0
    execed_time = 0
    def __init__(self, argv):
        self.num = argv[0]
        self.enter_time = argv[1]
        self.need_time = argv[2]
        self.priority = argv[3]



def print_processes(processes):
    print('Here is the process list, with the infomation of each process: \n')
    for p in processes:
        print('Process: {}, enter_time: {:2d}, need_time: {:2d}, priority: {}'.format(p.num, p.enter_time, p.need_time, p.priority))

def print_statistics(processes):
    print('Final statistics:')
    count = 0
    turnaroundSum = 0
    waitSum       = 0
    responseSum   = 0
    for p in processes:
        # print(p.enter_time, p.need_time, p.start_time, p.complete_time)
        num  = p.num
        runtime = p.need_time

        response   = p.start_time - p.enter_time
        turnaround = p.complete_time - p.enter_time
        wait       = turnaround - p.need_time
        print('  Process {} -- Response:{:3d}   Turnaround: {:3d}  Wait: {:3d}'.format(num, response, turnaround, wait))
        responseSum   += response
        turnaroundSum += turnaround
        waitSum       += wait

        count = count + 1
    print('\n  Average -- Response:{:.3f}   Turnaround: {:.3f}  Wait: {:.3f}\n'.format(responseSum/count, turnaroundSum/count, waitSum/count))

def fifo(processes):
    print("FIFO:")
    print('Execution trace:')
    fifo_processes = copy.deepcopy(processes)
    cur = 0
    for p in fifo_processes:
        print('  time {:3d}: Run process {} for {:2d} secs ( DONE at {:3d} ) Priority: {}'.format(cur, p.num, p.need_time, cur + p.need_time, p.priority) )
        p.start_time = cur
        cur += p.need_time
        p.complete_time = cur
    fifo_processes.sort(key=lambda x: x.num)
    print_statistics(fifo_processes)

# highest priority first
def hpf(processes):
    print("Highest Priority First:")
    tsr(processes, key=lambda x: x.priority)

# shortest time-to-complete first
def stcf(processes):
    print("Shortest Time-to-Complete First:")
    tsr(processes, key=lambda x: x.need_time - x.execed_time)

# Round-Robin
def rr(processes):
    print("Round Robin:")
    tsr(processes)

# Time Slice Rotation.
def tsr(processes, key=None):
    print('Execution trace:')
    tsr_processes = copy.deepcopy(processes)
    cur, size = 0, len(tsr_processes)
    start, done = set(), [] #start record process that has entered the queue, prevent repeated entry.
    circular_queue = deque()
    while len(done) < size:
        # if using depue.extend, we can't make the start set clearly.
        pes = list(filter(lambda x: x.num not in start and x.enter_time <= cur, tsr_processes))
        for p in pes:
            circular_queue.append(p)
            start.add(p.num)
        if key == None:
            p = circular_queue[0]
        else:
            # Because the smaller the number, the higher the priority, we can use the min function all the time.
            p = min(circular_queue, key=key)
        if p.num not in start:
            start.append(p.num)
        if p.start_time == -1:
            p.start_time = cur
        p.execed_time += Timeslice
        if p.execed_time >= p.need_time:
            circular_queue.remove(p)
            p.complete_time = cur + Timeslice
            done.append(p.num)
            print('  time {:3d}: Run process {} for {:2d} secs Priority: {} (!!! Process {} DONE at {:3d})'.format(cur, p.num, Timeslice, p.priority, p.num, cur + Timeslice) )
        else:
            print('  time {:3d}: Run process {} for {:2d} secs Priority: {}'.format(cur, p.num, Timeslice, p.priority) )
            circular_queue.rotate(-1)
        cur += Timeslice
    tsr_processes.sort(key=lambda x: x.num)
    print_statistics(tsr_processes)


processes = []
num = int(input())
for i in range(num):
    process_s = input().split()
    process_a = list(map(int, process_s))
    processes.append(Process(process_a))

processes.sort(key=lambda x: x.enter_time, reverse=False)
print_processes(processes)
print("\nSolution:\n")
fifo(processes)
rr(processes)
hpf(processes)
stcf(processes)
