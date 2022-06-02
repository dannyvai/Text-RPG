import queue

LOCAL_INPUT = False
input_queue = queue.Queue()

def myinput(str):
    if LOCAL_INPUT:
        return input(str)
    else:
        print(str)
        return input_queue.get()