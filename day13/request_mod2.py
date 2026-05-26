import requests
from rich import print

response=requests.get("https://www.w3schools.com/Python/module_requests.asp")
# print(response.text) #returns the response body as a string (str) #use for plain text
# print(response.content) #Returns the raw response body as bytes (bytes) #use for images,pdfs etc.

with open(r"C:\python practice\day13\index.html","w",encoding='utf-8') as f:
    f.write(response.text)
    
r=requests.get('https://api.github.com/events')
print(r.url)
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.get('https://httpbin.org/get', params=payload)

r3=requests.post('https://httpbin.org/post?a=b',data={'key':'value'})
# a:b will come in args
# data will come in form

r4 = requests.put('https://httpbin.org/put', data={'name': 'khushi'})
r5 = requests.delete('https://httpbin.org/delete')
#A HEAD,options request only returns headers, not the response body.
r6 = requests.head('https://httpbin.org/get')
#options Ask what methods are allowed
r7 = requests.options('https://httpbin.org/get')
# print(r.json())
# print(r2.json())
# print(r3.json())
# print(r4.json())
# print(r5.json())
print("\n")
# print(r6.headers)
# print(r6.status_code)

# print(r7.status_code)
# print(r7.headers)