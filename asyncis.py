"""
Inntroduction to corutine

how to write coroutine
how to execute corutine
"""


import asyncio

async  def main():#main is corutine
    print("hello")
    await asyncio.sleep(1)#function is suspended in middle
    print("world")


asyncio.run(main())