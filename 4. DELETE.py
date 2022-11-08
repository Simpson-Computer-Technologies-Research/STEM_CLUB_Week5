# // Use the requests library
import requests

# // The url you want to send a request to
url = "http://httpbin.org/delete"

# // Send the http request
# //
# // A DELETE request is used to delete data from whatever 
# //    url you're sending the request to
# //    
# //    DELETE is used by API's
# // 
r = requests.delete(url)

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
