import threading
import time
from random import choice
from string import ascii_letters

def first_thread():
    while True:
        print("Текущее состояние списка:")
        for i in list_str:
            print(i, end="")
        print()
def second_thread():
    while True:
        with open("output.txt", "w") as f:
            list_str.sort()
            f.writelines(list_str)
        time.sleep(5)


list_str = []
first = threading.Thread(target=first_thread)
second = threading.Thread(target=second_thread)
first.start()
second.start()
while True:
    list_str.append("".join(choice(ascii_letters) for i in range(20)))
    list_str[-1]+="\n"
    time.sleep(1)