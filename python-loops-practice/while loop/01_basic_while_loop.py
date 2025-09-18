# basic syntax of while loop
count=1
while (count<=5):
    print("Hello",count)
    count+=1  
print("................")

# while+ else 
x=3
while (x>0):
    print("Counting down:",x)
    x-=1  # decrement  # x+=1  increment continue forever
else:
    print("Loop finished")
print("................")


#while + break + continue
num=0 
while(num<10):
      num+=10
      if (num==5):
            continue
      if (num==8):
           break
      print(num)
print("................")
#while + break + continue
i=0
while True:
     i+=1
     print(i)
     if (i==20):
          print("************")
          break
print("................")
x=0
y=5
while (x<y and y>0):
    print("x:",x,"y:",y)
    x+=1
    y-=1
print("................")

start=1
while (start<=10):
    print(start)
    start+=1
print("................")

# with list 
names=["Alice","Bob","Charlie","David","Eve","Frank",
       "Grace","Hannah","Ivy","Jack"  ]
for name in names:
     if name=="David":
          print("Found:",name)
          break
          print(name)
print("................")

names=["Alice","Bob","Charlie","David","Eve","Frank",
       "Grace","Hannah","Ivy","Jack"  ]
found=False
for name in names :
     if name == "David":
            print("Found:",name)
            found=True
            break
if not found:
     print("Not found")



# infinite loop
while True:
    name=input("Enter your name:")
    if name=="exit":
        break
    
        