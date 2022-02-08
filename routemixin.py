import socket
import subprocess

class RouteMixin:


    def _traceroute(self):
        netloc = self.form_url().netloc
        p = subprocess.Popen(['tracert',netloc],stdout=subprocess.PIPE,shell=True)
        return b''.join(p.stdout.readlines()).decode()

    @classmethod
    def query_server(cls, server, query, port: int=43):
        msg = b''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server,port))
        sock.send(bytes(query + '\r\n','UTF-8'))
        while len(msg) < 10000:
            rec = sock.recv(100)
            if rec == b'':
                break
            msg += rec
        return msg

    
        
        
        

        

    
        
