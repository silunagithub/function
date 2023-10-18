msg="welcome to python"
print(msg[1:12:2])
print(msg[3:15:2])
print(msg[::])    #[0:17:1]
print(msg[::2])   #[0:17:2]
print(msg[1:12:2])
print(msg[:5000:2])   #[0:16:2]
print(msg[0:16:2])
print(msg[100:12:2])
print(msg[::-1])  #start=-2   stop-(-length+1)
print(msg[::-2])   #nothing nothing -2  start=-1  end/stop=-(length+1) step/jump=-2
print(msg[-15:-14:-1])   #backwod direction so that empty but moving foreward direction
print(msg[8:15:-1])      #back ward direction so that not execuating i.e blank but it is moving fareward direction
print(msg[5000:2:-1])    #backward direction start=16,end/stop=3 ,backward index=-1
print(msg[-6::])    #start=-6  stop=last one(jump value=-1)
print(msg[-1:-4:-1])  #backward direction
print(msg[:-4:])    #end=-4 start=0(fareward direction)
print(msg[-4:-1:])  #start=-4  end=-1 stop=nothing means 1  -4+1=-3 so on  note:stop value -1 means it is not included
print(msg[2:9])       #
print(msg[2:])       #start=2
print(msg[::-+1])    #start=-1 stop=-18i.e(length+1)=-18+1=-17 backward direction   note:it is called as reverse order
print(msg[1:-12:])   #
print(msg[-2:-12:])
print(msg[True:-1:1])
print(msg[False+10:(True-True):-1])