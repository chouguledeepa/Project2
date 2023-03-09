import asyncio
import time

async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")

async  def main():
    await asyncio.gather(count(),count(),count())

if __name__ == "__main__":
    print(f"started time at {time.strftime('%x')}")
    asyncio.run(main())
    print(f"finished time at {time.strftime('%x')}")