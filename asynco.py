import asyncio
import time

def say_after(delay, what):

    await asyncio.sleep(delay)
    print(what)

def main():
    print(f"started time at {time.strftime('%x')}")
    await say_after(1, "hello")

    await say_after(2, "hello")
    print(f"finished time at {time.strftime('%x')}")

    #we use asyncio.run() for entry point

asyncio.run(main())#entry point