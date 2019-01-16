import collections
import os
import time
import psutil


def bandwidth_stats():
    netvars = psutil.net_io_counters(pernic=False, nowrap=True)
    timer = time.time()
    list_down = collections.deque(maxlen=50)
    list_up = collections.deque(maxlen=50)
    mb_u_0 = netvars[1]
    mb_d_0 = netvars[0]

    while True:
        os.system("cls")
        time.sleep(1 - (time.time() - timer))

        netvars = psutil.net_io_counters(pernic=False, nowrap=True)
        timer = time.time()
        mb_u_1 = netvars[1]
        mb_d_1 = netvars[0]
        down_speed = round((mb_u_1 - mb_u_0) / (1024 ** 2) * 8, 4)
        up_speed = round((mb_d_1 - mb_d_0) / (1024 ** 2) * 8, 4)
        list_down.append(down_speed)
        list_up.append(up_speed)
        avg_down = round(sum(list_down) / len(list_down), 4)
        avg_up = round(sum(list_up) / len(list_up), 4)

        # Print the stats
        print("Download stats")
        print("Download speed Mbps: " + str(down_speed))
        print("AVG Download speed Mbps: " + str(avg_down))
        print("PEAK Download speed Mbps: " + str(max(list_down)))
        print("")
        print("Upload stats")
        print("Upload speed Mbps: " + str(up_speed))
        print("AVG Upload speed Mbps: " + str(avg_up))
        print("PEAK Upload speed Mbps: " + str(max(list_up)))
        print("")
        print("")
        mb_u_0 = mb_u_1
        mb_d_0 = mb_d_1


if __name__ == "__main__":
    bandwidth_stats()
