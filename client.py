import socket
'''
sending the data to the server in form of the string 

filename : word to found

'''
c1=socket.socket()
HOST='127.0.0.1'
PORT=5656

c1.connect((HOST,PORT))


filename=input("enter the filename ")
word=input("enter the word to be found ")
DATA=f"{filename}:{word}"
word=bytes(DATA,'utf-8')

c1.send(word)
result=c1.recv(5000)

result=result.decode("utf-8")
print(result)
c1.close()