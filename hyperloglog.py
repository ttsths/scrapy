# coding: utf-8
import redis as redis
import math
import random

## 算低位0的个数
def low_zeros(value):
    for i in xrange(1,32):
        if value>>i<<i!=value:
            break
    return i-1

class BitKeeper(object):
    def __init__(self):
        self.maxbits = 0

    def random(self,m):
        bits = low_zeros(m)
        if bits > self.maxbits:
            self.maxbits = bits

class Experiment(object):
    def __init__(self,n,k = 1024):
        self.n = n
        self.k = k
        self.keepers = [BitKeeper() for i in range(k)]

    def do(self):
        for i in range(self.n):
            m = random.randint(0, 1 << 32 - 1)

            # 确保同一个整数被分配到同一个桶里面，摘取高位后取模
            keeper = self.keepers[((m & 0xfff0000) >> 16) % len(self.keepers)]
            keeper.random(m)

    def estimate(self):
        sumbits_inverse = 0  # 零位数倒数
        for keeper in self.keepers:
            sumbits_inverse += 1.0 / float(keeper.maxbits)
        avgbits = float(self.k) / sumbits_inverse  # 平均零位数
        return 2 ** avgbits * self.k  # 根据桶的数量对估计值进行放大

for i in range(100000, 1000000, 100000):
    exp = Experiment(i)
exp.do()
est = exp.estimate()
print i, '%.2f' % est, '%.2f' % (abs(est - i) / i)

client = redis.StrictRedis()
for i in range(100000):
    client.pfadd("codehole", "user%d" % i)
    total = client.pfcount("codehole")
    if total != i+1:
        print total, i+1
        break

