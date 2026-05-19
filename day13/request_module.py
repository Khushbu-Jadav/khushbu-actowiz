import requests

x=requests.get('https://w3schools.com')
# print(x.status_code)
# print(x.text) #the content of the requested file

# y=requests.get('https://w3schools.com',params={"model":"Mustang"})
# print(y)

url = 'http://w3schools.com/python/demopage.htm'

#make a request without setting the 'allow_redirects' parameter to False
# z=requests.get(url)
# print(z.text)
#automatically redirects http requests to https
# z1=requests.get(url,allow_redirects=False)
# print(z1.text)

# auth : A tuple to enable a certain HTTP authentication.
# k1=requests.get(url, auth = ('user', 'pass'))
# print(k1.status_code)
url2 = 'https://w3schools.com/python/demopage.asp'
k2=requests.get(url2,headers={"HTTP_HOST":"MyVeryOwnHost"})
print(k2.text)


url3="https://example.com"
response=requests.get(url3)
print(response)
print(response.status_code)
print(response.text)

#status_code
# 200 → success
# 404 → page not found
# 403 → blocked
# 500 → server error

#add headers

response2 = requests.get("https://httpbin.org/headers",headers={"User-Agent": "Mozilla/5.0"})
print(response2.text)

#HTML Downloading : This downloads the webpage source.
response3 = requests.get("https://quotes.toscrape.com")
html = response.text
print(html[:1000])

#Query Parameters
#ex: https://example.com/search?q=python
params = {
    "q": "python"
}
response4 = requests.get("https://httpbin.org/get",params=params)
print(response4.url)
print(response4.text)

# POST Requests
# login forms
# submitting data
# APIs

data = {
    "username": "test",
    "password": "123"
}

response5 = requests.post(
    "https://httpbin.org/post",
    data=data
)

print(response5.text)