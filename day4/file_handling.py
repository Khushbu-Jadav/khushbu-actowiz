with open("demo.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demo.txt") as f:
  print(f.read())

with open("demofile.txt", "r+") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

f = open("demofile.txt")
print(f.read())

with open("test.txt", "a") as f:
  f.write("\n my hometown is patan")

  # w+(right or read)*******

  with open("test.txt","w+")as f:
    f.write("hello!\n i am vidhi Thakkar ")

  with open ("test.txt","r")as f:
    content = f.read()
    print(content)

  data = b"hello, binory......."

  with open("example.bin","wb")as f:
    f.write(data)

  with open ("example.bin","r")as f:
   content = f.read()
  print(content)

  print("binory file save")

  with open(r"C:\Users\vidhi.thakkar\Pictures\Screenshots\Screenshot 2026-04-30 141353.png", "rb") as f:
   data = f.read(20)
  print(data)
