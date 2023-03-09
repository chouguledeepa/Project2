# concurrency vs parallelism

- concurrency means multiple tasks are running in overlapped time frame.
- In Python, threads running in "time-sliced" manner are "concurrent"


#### concurrency

task1   --------
task2     -------
task3       -------

#### parallelism

task1   -------
task2   -------
task3   -------

-------------------------------------------------------------------->


```python

from multiprocessing.pool import ThreadPool
pool = ThreadPool(10)
results = pool.map(func, iterable)
```


### sychronous and asynchronous 

In asynchronous execution, we use single thread but in `async` manner

- `async` - wait time can be utilised by the existing thread to pick other task
- `sync` - linear approach


# asyncio

3.4 - provisional format
3.7+ - 


#### coroutine
- declared with `async/await` keywords. This syntax is preferred way of writing `async` applications
- function needs to suspend in the middle and 
should hand over execution to some other function
- function passes control to the other function in the middle of execution
- above approach is similar to generator 

```
import asyncio


```
