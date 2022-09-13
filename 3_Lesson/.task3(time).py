import time

for i in range(10):
    a = time.time()
    print((int(a * 1000000)) % 100)