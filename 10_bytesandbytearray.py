#a=[10,20,30,40,]    # list
#b=bytes(a)   # covert list to bytes
#print(b[0])  #in bytes array we cannot do the the modification
#print(b[4])   #error
#print(b[3])
#print(b[-2])



#for i in b:
   # print(i)   


a=[10,20,30,40,50]
b=bytearray(a)     #convert list to bytearray
print(b[1])
print(b[-1])   # in byte array we can do the modification
# modify 1st index value
b[1]=200
b[2]=245
for i in b:
    print((i))

