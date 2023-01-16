import requests, threading

# // Define a function
def main():
  r = requests.get("http://httpbin.org/get")
  print(r.content)
  
# // Start the thread
threading.Thread(target=main).start()
