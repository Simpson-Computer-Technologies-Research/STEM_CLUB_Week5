# // Use the requests library
import requests

# // The url you want to send a request to
url = "http://httpbin.org/get"

# // Send the http request
r = requests.get(url)

# // Print the response status code
# // 200 == Success
# // 500 == Internal Error
# // 404 == Page not Found
# // etc.
print(r.status_code)


# // Print the response body
print(r.content)

# // Print the response json
print(r.json())
