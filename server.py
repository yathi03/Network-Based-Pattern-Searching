import socket
import threading as th
from search import Search

class Mythread(th.Thread):
    def __init__(self, client):
        th.Thread.__init__(self)
        self.client = client
    
    def run(self):
        
        data = self.client.recv(5000).decode("utf-8")
        filename,word=data.split(":")
        result_word=Search(filename,word)
        final_word=str(result_word.results)
        self.client.send(final_word.encode("utf-8"))

s1 = socket.socket()
host = '127.0.0.1'
port = 5656
s1.bind((host, port))
s1.listen(1)



while True:
    client, addr = s1.accept()
    t1 = Mythread(client)
    t1.start()