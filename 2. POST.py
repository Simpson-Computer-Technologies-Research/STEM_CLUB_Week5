# // Use the requests library
import requests

# // The url you want to send a request to
url = "http://httpbin.org/post"

# // Send the http request
# //
# // A POST request is used to add new data to whatever 
# //    url you're sending the request to
# //    
# //    POST is used by API's
# // 
r = requests.post(url)

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
