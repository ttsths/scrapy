# coding:utf8
import time
class Funnel(object):
    def __init__(self,capacity,leaking_rate):
        """
        :param capacity: 漏斗容量
        :param leaking_rate: 滤嘴流水速率
        """
        self.capacity = capacity
        self.leaking_rate = leaking_rate
        # 剩余漏斗空间
        self.left_quota = capacity
        # 上一次漏水时间
        self.leaking_ts = time.time()



    """
    更新当前漏斗属性
    """
    def make_space(self):
        now_ts = time.time()
        # 当前时间与上一次漏水的时间差
        delta_ts = now_ts - self.leaking_ts
        # 这段时间内流失的容量
        delta_quota = delta_ts * self.leaking_rate
        if delta_quota < 1:
            return
        self.left_quota += delta_quota
        self.leaking_ts = now_ts
        if self.left_quota > self.capacity:
            self.left_quota = self.capacity


    """
    当前是否允许 quota个漏斗
    """
    def watering(self,quota):
        """
        :param quota:
        :return:
        """
        self.make_space()
        if self.left_quota >= quota:
            self.left_quota -= quota
            return True
        return False

# 所有的漏斗
funnels = {}
def is_action_allowed(user_id, action_key, capacity,leaking_rate):
    """
    :param user_id:
    :param action_key:
    :param capacity:
    :param leaking_rate:
    :return:
    """
    key = '%s:%s'%(user_id, action_key)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity,leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)

for i in range(20):
    print is_action_allowed('laoqian','reply',15,0.5)