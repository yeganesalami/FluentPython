import struct

fmt='<3ssHH'
with open('a.gif','rb') as fp:
    file = memoryview(fp.read())
    
header = file[:1]

struct.unpack(fmt,header)
print(struct.unpack(fmt,header))

#have error!!!! fix first

# 3800 showtempcredit 
# 3100 userinfo