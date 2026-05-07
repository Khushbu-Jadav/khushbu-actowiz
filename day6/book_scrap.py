import re
url = "https://books.toscrape.com/"
with open('book_to_scrap.html','r')as f:
    data = f.read()
# email_pattern = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",data)
page = re.findall(r'href="([^"]+\.html)"',data)
img = re.findall(r'src="([^"]+\.jpg)"',data)
img_url = [url + img for img in img]
name = re.findall(r'title="([^"]+)"',data)
# price = re.findall(r"£\d.+[0-9]",data)
price = re.findall(r"£\d+\.\d+", data)

print("Number of books: ",len(name))
print("---pages---")
print("\n",page)
print("---image path---")
print("\n",img)
print("---image url---")
print("\n",img_url)
print("---Book name---")
print("\n",name)
print("---Book price---")
print("\n",price)

