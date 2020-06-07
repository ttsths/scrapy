# coding: utf8
import redis
import time

client = redis.StrictRedis()

"""
redis 限流(时间窗口)
每一个行为到来 ，都维护一个窗口
将当前窗口之外的记录全部清除，只保留窗口内的行为
zset score value
"""
def is_action_allowed(user_id, action_key, period, max_count):
    key = 'hist:%s:%s'%(user_id,action_key)
    # 毫秒时间戳
    now_ts = int(time.time()*1000)
    with client.pipeline() as piple:
        # 记录行为 key value score
        mapping = {now_ts:now_ts,}
        piple.zadd(key,mapping)
        # 移除时间窗口之外的行为记录
        piple.zremrangebyscore(key, 0, now_ts-period*1000)
        # 获取窗口内的行为个数
        piple.zcard(key)
        # 设置Zset过期时间，避免冷用户持续占用内存
        # 过期时间应该等于时间窗口的长度，再多宽限1s
        piple.expire(key,period + 1)
        ## 批量执行
        _,_,current_count,_ = piple.execute()
    # 比较数量是否超标
    return current_count <= max_count

for i in range(20):
    print is_action_allowed("laoqian","reply",60,5)