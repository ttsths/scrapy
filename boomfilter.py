import redis

client = redis.StrictRedis()
client.delete("codehole")
for i in range(100000):
    client.execute_command("bfadd","codehole","user%d" %i)
    ret = client.execute_command("bf.exists", "codehole", "user%d" % i+1)
    if ret == 0:
        print i;
        break