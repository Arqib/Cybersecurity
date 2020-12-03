import socket
import ssl
import requests

CRLF = "\r\n"

host = 'ac1f1fd81ed562d180de04a800d5000b.web-security-academy.net'
port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE
sock = context.wrap_socket(sock, server_hostname=host)

try:
    sock.connect((host, port))
except:
    print("Connection Error")
    exit(1)

with open("file.txt", "r") as file:
    count = len(open("file.txt").readlines(  ))
    #print(count); print("\n")
    x = ''
    for y in range(count):
        #x = ''
        x += file.readline()
    x = x.replace("\n", CRLF, count)
    #print(repr(x))
    #print("\n")

msg = x

print(msg)

sock.sendall(str.encode(msg))
print(sock.recv(4096).decode())

try:
    sock.shutdown(socket.SHUT_RDWR)
except:
    print("Socket shutdown error")

sock.close()
