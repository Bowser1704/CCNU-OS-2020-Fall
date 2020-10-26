## 进程调度算法

- FIFO
- SJF (Shortest Job First)
- STCF (Shortest Time-to-Completion First)
- RR (Round-Robin)
- MLFQ (Multi-level Feedback Queue)

SJF/STCF for average turnaround time, RR for response time.

考虑到我们的新假设，STCF 可证明 是最优的。考虑到如果所有工作同时到达，SJF 是 最优的，那么你应该能够看到 STCF 的最优性是符合直觉的。

响应时间，分时系统的引进，需要我们考虑响应时间。
$$
周转时间 = 完成时间 - 到达时间
$$

$$
响应时间 = 首次运行 - 到达时间
$$

$$
等待时间 = 周转时间 - 运行时间
$$

当你坐在计算机面前，你需要计算机对你的一些操作马上作出响应，也就必须要是抢占式的。

