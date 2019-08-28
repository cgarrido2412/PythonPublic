from threading import Timer

def timeout():
    print("15 minutes have passed!")

# duration is in seconds
t = Timer(15 * 60, timeout)
t.start()

# wait for time completion
t.join()
