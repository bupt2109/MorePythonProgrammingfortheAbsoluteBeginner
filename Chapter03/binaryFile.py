# P44-46 二进制读取文件
import struct
# file = open("binary.dat", "wb")
# for n in range(1000):
#     data = struct.pack('i', n)
#     file.write(data)
# file.close()

file = open("binary.dat", "rb")
size = struct.calcsize("i")  # size = 4
print(size)
bytes_read = file.read(size)
while bytes_read:
    value = struct.unpack("i", bytes_read)
    value = value[0]
    print(value, end=" ")
    bytes_read = file.read(size)
file.close()

