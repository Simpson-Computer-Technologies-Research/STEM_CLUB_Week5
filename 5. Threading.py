from threading import *


# // Function to be ran by the threads
def my_function(thread: int):
  for i in range(10):
    requests.get("http://httpbin.org/get")
    print(f"\nThread {thread}: {i}\n")


# // Initialize the threads
t1 = threading.Thread(target=my_function, args=(1))
t2 = threading.Thread(target=my_function, args=(2))

# // Start the threads
t1.start()
t2.start()
