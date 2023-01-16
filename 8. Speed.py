import requests, threading, asyncio, time


# // Define a function
def main():
  requests.get("http://httpbin.org/get")


# // IO-BlockingIOError
start_time = time.time()
for _ in range(3):
  main()

# // Print speed
print(f"Default: {time.time()-start_time}")

# // Threading
start_time = time.time()
for _ in range(3):
  t = threading.Thread(target=main)
  t.start()
  
# // Print speed
print(f"Threading: {time.time()-start_time}")

# // Async (Non-IO Blocking)
# // Define an async_main() function
async def async_main():
  requests.get("http://httpbin.org/get")


# // Initialize async function for asyncio
async def run_main():
  for _ in range(3):
    await async_main()

# // Async functions start time
start_time = time.time()

# // Asyncio run the run_main() function
asyncio.run(run_main())

# // Print speed
print(f"Async: {time.time()-start_time}")
