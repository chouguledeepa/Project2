
"""
started  at 15:51:14
one
two
one
two
one
two
finished at15:51:15


"""
import asyncio
import time

def count3():
    print("five")
    time.sleep(1)
    print("six")

def count2():
    print("three")
    time.sleep(1)
    print("four")

def count1():
    print("one")
    time.sleep(1)
    print("two")


def main():
    for _ in range(3):
        count1()
    for _ in range(3):
        count2()

    for _ in range(3):
        count3()


if __name__ == "__main__":
    print(f"started  at {time.strftime('%x')}")
    main()
    print(f"finished at {time.strftime('%x')}")