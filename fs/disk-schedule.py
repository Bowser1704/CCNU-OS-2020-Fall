def sstf(seq, cur):
    ans = []
    all_len = 0
    while seq:
        ans.append(cur)
        n = min(seq, key=lambda x : abs(x-cur))
        all_len += abs(n-cur)
        cur = n
        seq.remove(cur)
    return ans, all_len

def scan(seq, cur):
    ans = []
    all_len = 0
    while seq:
        ans.append(cur)
        n = min(seq, key=lambda x : abs(x-cur))
        all_len += abs(n-cur)
        cur = n
        seq.remove(cur)
    return ans, all_len


seq = [86, 147, 91, 177, 94, 150, 102, 175, 130]
ans, n = sstf(seq, 143)
print(ans)
print(n)
