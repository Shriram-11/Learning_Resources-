from time import sleep


def leakyBucket(bucket_size, packets, rate):
    cycle = bucket = 0
    for p in packets:
        if bucket+p > bucket_size:
            bucket = 0
            cycle += 1
            print(f"Dropped {p}\nCycle {cycle} complete\n")
            sleep(1/rate)
        else:
            bucket += p
            print(f"Sent {p}\t")


packets = [2, 3, 5, 6, 7, 9, 2, 8, 10, 11, 2, 4, 7, 5, 8, 9, 1, 3, 12]
bucket_size = 10
rate = 2
leakyBucket(bucket_size, packets, rate)
