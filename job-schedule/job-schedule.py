import copy

class Job:
    num = 0
    enter_system_time = 0
    exec_time = 0
    enter_memory_time = 0
    def __init__(self, argv):
        self.num = argv[0]
        self.enter_system_time = argv[1]
        self.exec_time = argv[2]
    def get_done_time(self):
        return time_add(self.exec_time, self.enter_memory_time)

def time_add(t1, t2):
    t3 = (t1 // 60) * 100
    t1 %= 60
    t3 += (t1 + t2)
    if t3 % 100 >= 60:
        t3 = (t3 // 100 + 1) * 100 + (t3 % 100 - 60)
    return t3

def print_res(jobs):
    for job in jobs:
        print(job.num, job.enter_memory_time, job.get_done_time())
    
def fifo(jobs):
    fifo_jobs = copy.deepcopy(jobs)
    fifo_jobs[0].enter_memory_time = fifo_jobs[0].enter_system_time
    for i in range(1, len(fifo_jobs)):
        fifo_jobs[i].enter_memory_time = fifo_jobs[i-1].get_done_time()
    return fifo_jobs

# short_job_first
def sjf(jobs):
    sjf_jobs = copy.deepcopy(jobs)
    res = []
    length = len(sjf_jobs)
    cur_job = sjf_jobs[0]
    res.append(cur_job)
    cur_job.enter_memory_time = cur_job.enter_system_time
    while len(res) < length:
        cur_time = cur_job.get_done_time()
        sjf_jobs.remove(cur_job) # remove the cur_job from the wait_jobs
        wait_jobs = [x for x in sjf_jobs if x.enter_system_time <= cur_time] 
        if len(wait_jobs) == 0:
            cur_job = min(sjf_jobs, key=lambda x: x.enter_system_time)
        else:        
            cur_job = min(wait_jobs, key=lambda x: x.exec_time)
        cur_job.enter_memory_time = cur_time
        res.append(cur_job)
    return res

# highest response ratio next
def hrrn(jobs):
    hrrn_jobs = copy.deepcopy(jobs)
    res = []
    length = len(hrrn_jobs)
    cur_job = hrrn_jobs[0]
    res.append(cur_job)
    cur_job.enter_memory_time = cur_job.enter_system_time
    while len(res) < length:
        cur_time = cur_job.get_done_time()
        hrrn_jobs.remove(cur_job) # remove the cur_job from the wait_jobs
        wait_jobs = [x for x in hrrn_jobs if x.enter_system_time <= cur_time] 
        if len(wait_jobs) == 0:
            cur_job = min(hrrn_jobs, key=lambda x: x.enter_system_time)
        else:        
            # highest response ratio next
            cur_job = max(wait_jobs, key=lambda x: (cur_time - x.enter_system_time) / x.exec_time)
        cur_job.enter_memory_time = cur_time
        res.append(cur_job)
    return res

# initialize the jobes array
jobs = []    
num = int(input())
for i in range(num):
    job_s = input().split()
    job_a = list(map(int, job_s))
    jobs.append(Job(job_a))
jobs.sort(key=lambda x: x.enter_system_time, reverse=False)
print("--- FIFO ---")
print_res(fifo(jobs))
print("--- SJF  ---")
print_res(sjf(jobs))
print("--- HRRN ---")
print_res(hrrn(jobs))