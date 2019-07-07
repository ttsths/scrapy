import threading

import time


def sheep():
    print("sheep eat grass")
    time.sleep(2)

def cat():
    print("cat eat fish")

class sheep_class(threading.Thread):
    name = "sheep_calss"
    def __init__(self):
        super(sheep_class, self).__init__()
    def run(self):
        print("sheep_class eat grass")
if __name__ == "__main__":
    new_thread1 = threading.Thread(target=sheep, args=())
    new_thread2 = threading.Thread(target=cat, args=())

    sheep_thread = sheep_class()
    sheep_thread.run()

    start_time = time.time()

    new_thread1.start()
    new_thread2.start()

    new_thread1.join()
    new_thread2.join()
    print("excute time:{}".format(time.time()-start_time))

"""
协程
async
await
"""
import asyncio
async  def find_even(num):
    print("finding in range {} event".format(num))
    located = []
    #同步的机制
    for i in range(num):
        if i % 2 == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)
        print("Done{} % 2 in range{}".format(num, num))
        return located
async def main():
    even1 = loop.create_task(find_even(5080000))
    even2 = loop.create_task(find_even(100200))
    even3 = loop.create_task(find_even(400))

    await  asyncio.wait([even1,even2,even3])
if __name__ =="__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        print(e)
    finally:
        loop.close()