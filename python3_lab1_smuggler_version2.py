import socket
import ssl
import requests
import subprocess as sb
import sys

CRLF = "\r\n"

#host = 'ac1f1fd81ed562d180de04a800d5000b.web-security-academy.net'

try:
    host2 = sys.argv[1]
except Exception as e:
    print("Provide a url")
    exit()

port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE
sock = context.wrap_socket(sock, server_hostname=host2)


try:
    sock.connect((host2, port))
except:
    print("Connection Error")
    exit(1)

#with open("file.txt", "r") as file:
#    count = len(open("file.txt").readlines(  ))
#    #print(count); print("\n")
#    x = ''
#    for y in range(count):
#        #x = ''
#        x += file.readline()
#    x = x.replace("\n", CRLF, count)
    #print(repr(x))
    #print("\n")

#msg = x

#print(msg)

sb.check_output([r"sed -i 's/Host.*/Host: {0}/g' confirm1.txt".format(host2)], shell=True),
finalMessage =  sb.check_output([r"sed -z 's/\n/\r\n/g' confirm1.txt"], shell=True)

print(finalMessage)

msg = finalMessage

sock.sendall(str.encode(str(msg)))
print(sock.recv(4096).decode())

try:
    sock.shutdown(socket.SHUT_RDWR)
except:
    print("Socket shutdown error")

sock.close()
