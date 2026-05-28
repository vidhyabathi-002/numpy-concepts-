# Threading and Multithreading in Python

## Table of Contents

1. [Introduction to Threading](#introduction)
2. [Threading vs Multithreading](#threading-vs-multithreading)
3. [Global Interpreter Lock (GIL)](#gil)
4. [Threading Module](#threading-module)
5. [Key Concepts with Examples](#key-concepts)
6. [Interview Q&amp;A](#interview-qa)

---

## Introduction to Threading

**Threading** is a technique in programming that allows multiple tasks or operations to run concurrently (at the same time) within a single program.

### What is a Thread?

A **thread** is the smallest unit of execution within a process. It is a lightweight sub-process that shares the same memory space as other threads in the process.

### Key Points:

- Threads allow you to execute multiple operations simultaneously
- All threads within a process share the same memory and resources
- Threads are faster to create than processes
- In Python, you need to import the `threading` module to use threading

```python
import threading
```

### Real-World Analogy

Think of a restaurant:

- **Process** = The entire restaurant
- **Thread** = Each waiter serving different tables simultaneously
- All waiters (threads) work in the same restaurant (process) and share the same kitchen (memory)

---

## Threading vs Multithreading

### Threading

**Threading** is executing multiple tasks within a single process in an overlapping time period. Only one thread executes at any given moment, but they take turns running.

```python
import threading
import time

def task1():
    for i in range(3):
        print(f"Task 1 - Iteration {i}")
        time.sleep(1)

def task2():
    for i in range(3):
        print(f"Task 2 - Iteration {i}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

print("All tasks completed!")
```

**Output:**

```
Task 1 - Iteration 0
Task 2 - Iteration 0
Task 1 - Iteration 1
Task 2 - Iteration 1
Task 1 - Iteration 2
Task 2 - Iteration 2
All tasks completed!
```

### Multithreading

**Multithreading** is the execution of multiple threads simultaneously (in parallel) on multi-core processors. However, in Python, due to GIL, true parallelism is limited to I/O operations.

### Key Difference

| Threading                         | Multithreading                                          |
| --------------------------------- | ------------------------------------------------------- |
| Single thread executes at a time  | Multiple threads execute simultaneously (on multi-core) |
| Context switching between threads | Parallel execution on different cores                   |
| Slower for CPU-intensive tasks    | Better for I/O-bound tasks                              |

---

## Global Interpreter Lock (GIL)

### What is GIL?

The **Global Interpreter Lock (GIL)** is a mutex (mutual exclusion lock) used by the Python interpreter to protect access to Python objects. It prevents multiple threads from executing Python bytecode simultaneously within a single process.

### Key Points About GIL:

1. **Only one thread can execute Python code at a time**

   ```python
   import threading
   import time

   def cpu_intensive_task(name):
       start = time.time()
       total = 0
       for i in range(100000000):
           total += i
       end = time.time()
       print(f"{name} took {end - start:.2f} seconds")

   # Single threaded
   print("Single-threaded execution:")
   cpu_intensive_task("Task")

   # Multi-threaded (NOT faster due to GIL)
   print("\nMulti-threaded execution:")
   t1 = threading.Thread(target=cpu_intensive_task, args=("Task 1",))
   t2 = threading.Thread(target=cpu_intensive_task, args=("Task 2",))

   t1.start()
   t2.start()

   t1.join()
   t2.join()
   ```
2. **Why does Python have GIL?**

   - Memory management is simplified
   - Reference counting for garbage collection is thread-safe
   - C extensions are easier to write
3. **GIL doesn't affect I/O operations**

   ```python
   import threading
   import time
   import requests

   def fetch_data(url):
       start = time.time()
       response = requests.get(url)
       end = time.time()
       print(f"Fetched {url} in {end - start:.2f} seconds")

   # Multithreading is beneficial for I/O-bound tasks
   t1 = threading.Thread(target=fetch_data, args=("https://api.github.com",))
   t2 = threading.Thread(target=fetch_data, args=("https://api.github.com",))

   t1.start()
   t2.start()

   t1.join()
   t2.join()
   ```

---

## Threading Module

### Basic Thread Creation

```python
import threading

def my_function(name):
    print(f"Hello from {name}")

# Create a thread
thread = threading.Thread(target=my_function, args=("Thread-1",))

# Start the thread
thread.start()

# Wait for thread to complete
thread.join()
```

### Thread Class with Arguments

```python
import threading

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
  
    def run(self):
        print(f"Starting {self.name}")
        # Your code here
        print(f"Finishing {self.name}")

# Create and start thread
thread = MyThread("Worker-1")
thread.start()
thread.join()
```

---

## Key Concepts with Examples

### 1. join() Method

The **join()** method makes the main thread wait until the specified thread completes execution.

```python
import threading
import time

def worker(name):
    print(f"Worker {name} started")
    time.sleep(2)
    print(f"Worker {name} finished")

print("Main thread started")

t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()

# Main thread waits here until both threads complete
t1.join()
t2.join()

print("Main thread finished")
```

**Output:**

```
Main thread started
Worker A started
Worker B started
Worker A finished
Worker B finished
Main thread finished
```

### 2. Daemon Threads

A **daemon thread** is a thread that runs in the background and doesn't prevent the program from exiting.

```python
import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

def main_task():
    time.sleep(3)
    print("Main task finished")

# Create daemon thread
daemon = threading.Thread(target=daemon_task, daemon=True)
daemon.start()

main = threading.Thread(target=main_task)
main.start()

main.join()
print("Program ended")
```

**Output:**

```
Daemon thread running...
Daemon thread running...
Daemon thread running...
Main task finished
Program ended
```

### 3. Thread Lock (Mutex)

A **lock** prevents multiple threads from accessing shared resources simultaneously.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Acquire lock
            counter += 1
        # Lock is automatically released

# Without lock, counter might be incorrect due to race conditions
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Counter value: {counter}")  # Output: 200000
```

### 4. RLock (Reentrant Lock)

Allows the same thread to acquire the lock multiple times.

```python
import threading

lock = threading.RLock()

def reentrant_function():
    with lock:
        print("First acquisition")
        with lock:  # Same thread can acquire again
            print("Second acquisition")

thread = threading.Thread(target=reentrant_function)
thread.start()
thread.join()
```

### 5. Semaphore

Controls access to a shared resource by a fixed number of threads.

```python
import threading
import time

semaphore = threading.Semaphore(2)  # Allow 2 threads at a time

def access_resource(name):
    with semaphore:
        print(f"{name} accessing resource")
        time.sleep(2)
        print(f"{name} releasing resource")

threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 6. Event

Used for communication between threads.

```python
import threading
import time

event = threading.Event()

def waiter():
    print("Waiter: Waiting for event...")
    event.wait()  # Block until event is set
    print("Waiter: Event received!")

def signaler():
    time.sleep(2)
    print("Signaler: Setting event...")
    event.set()

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=signaler)

t1.start()
t2.start()

t1.join()
t2.join()
```

### 7. Condition Variable

Allows threads to wait for a specific condition.

```python
import threading
import time

condition = threading.Condition()
shared_data = []

def producer():
    for i in range(5):
        time.sleep(1)
        with condition:
            shared_data.append(i)
            print(f"Produced: {i}")
            condition.notify()  # Wake up waiting threads

def consumer():
    while True:
        with condition:
            if len(shared_data) == 0:
                print("Waiting for data...")
                condition.wait()
            if shared_data:
                item = shared_data.pop(0)
                print(f"Consumed: {item}")

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
```

---

## Interview Q&A

### Q1. What is the difference between threading and multiprocessing?

**Answer:**

- **Threading**: Multiple threads within a single process sharing the same memory

  - Lightweight and faster to create
  - Context switching is faster
  - Affected by GIL in Python
  - Good for I/O-bound tasks
- **Multiprocessing**: Multiple separate processes, each with its own memory

  - Heavier, slower to create
  - True parallelism on multi-core systems
  - No GIL limitation
  - Good for CPU-bound tasks

### Q2. What is the Global Interpreter Lock (GIL)?

**Answer:**
The GIL is a mutex that protects access to Python objects. It allows only one thread to execute Python bytecode at a time, even on multi-core processors. This means:

- CPU-bound tasks don't benefit from multithreading
- I/O-bound tasks benefit significantly (lock is released during I/O)
- Reason: Simplifies memory management and reference counting

### Q3. When should you use threading vs multiprocessing?

**Answer:**

- **Use Threading for**: I/O-bound tasks like web scraping, file I/O, API calls
- **Use Multiprocessing for**: CPU-bound tasks like data processing, mathematical computations
- **Example**:
  ```python
  # Threading for I/O
  import threading
  def fetch_url(url):
      response = requests.get(url)  # I/O operation

  # Multiprocessing for CPU
  from multiprocessing import Process
  def cpu_task():
      result = sum([i**2 for i in range(10000000)])
  ```

### Q4. What does the join() method do?

**Answer:**
`join()` blocks the calling thread until the thread on which it's called completes execution. It's used to ensure that a thread finishes before the main program continues.

```python
thread.start()
thread.join()  # Main thread waits here
print("Thread completed")
```

### Q5. What is a race condition and how do you prevent it?

**Answer:**
A **race condition** occurs when multiple threads access and modify shared data simultaneously without synchronization, leading to unpredictable results.

**Prevention methods**:

1. **Lock/Mutex**:

   ```python
   with lock:
       shared_variable += 1
   ```
2. **Semaphore**: Limit concurrent access
3. **Event**: Coordinate thread execution
4. **Avoid shared state**: Use thread-local storage

### Q6. What is a daemon thread?

**Answer:**
A daemon thread runs in the background and doesn't prevent the program from exiting. It's useful for background tasks like logging or monitoring. When the main program exits, all daemon threads are terminated immediately.

```python
thread = threading.Thread(target=function, daemon=True)
```

### Q7. How do you handle exceptions in threads?

**Answer:**

```python
import threading
import sys

def thread_function():
    try:
        # Thread code
        result = 1 / 0
    except Exception as e:
        print(f"Exception in thread: {e}")

# Exceptions in threads don't propagate to main thread
thread = threading.Thread(target=thread_function)
thread.start()
thread.join()
```

### Q8. What is a deadlock in threading?

**Answer:**
A **deadlock** occurs when two or more threads are blocked forever waiting for each other.

```python
# Example of deadlock
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_func():
    with lock1:
        time.sleep(1)
        with lock2:  # Waiting for lock2
            pass

def thread2_func():
    with lock2:
        time.sleep(1)
        with lock1:  # Waiting for lock1
            pass
```

**Prevention**: Always acquire locks in the same order.

### Q9. Explain Thread Pool

**Answer:**
A thread pool manages a fixed number of threads efficiently. Instead of creating/destroying threads frequently, reuse them.

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

# Create thread pool with 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])
    for result in results:
        print(result)
```

### Q10. What is Thread-Local Storage?

**Answer:**
Thread-local storage allows each thread to have its own independent copy of a variable.

```python
import threading

local_data = threading.local()

def thread_function(value):
    local_data.value = value  # Each thread has separate value
    print(f"Thread {threading.current_thread().name}: {local_data.value}")

t1 = threading.Thread(target=thread_function, args=(10,))
t2 = threading.Thread(target=thread_function, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()
```

---

## Practical Example: Producer-Consumer Problem

```python
import threading
import queue
import time

# Thread-safe queue
data_queue = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        data_queue.put(i)
        time.sleep(1)

def consumer():
    while True:
        item = data_queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(0.5)
        data_queue.task_done()

# Create and start threads
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
data_queue.put(None)  # Signal consumer to stop
c.join()

print("Done!")
```

---

## thread life cycle:

235 stages in a sigle thread 

their are 5 stage in  single  thred life cycle 

1. creation of new thread
2. runable stage
   interpriter will check whether our thread is ready to run are not
3. running stage :
4. terminated stage

## syncronization:

its a process of controlling multiple  threads to acces  all resourcess without any conflict


## DEADLOCK:

ITS A situvation 2 are 3 wait infinaitly  for eachother to execute 

THREAD SHEDULAR:


ITS A system component which is responsble for the  designing  which thread should execute ata perticulr thread 

## Summary

- **Threading** allows concurrent execution within a single process
- **GIL** limits true parallelism in Python for CPU-bound tasks
- Use **threading for I/O-bound** tasks and **multiprocessing for CPU-bound** tasks
- Always use **locks/synchronization** when accessing shared data
- **Daemon threads** run in background and don't block program exit
- Thread pools provide efficient thread management
- Understanding threading is crucial for building responsive applications
