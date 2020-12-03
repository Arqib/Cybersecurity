import socket
import ssl
import sys
import subprocess

try:
    host = sys.argv[1]
except Exception as e:
    print "Provide a url"
    exit()

port = 443
# message = "POST / HTTP/1.1\r\n"
# hostHeader = "Host: {0}\r\n".format(host)
# contentLength = "Content-Length: 8\r\n"
# transferEncoding = "Transfer-Encoding: chunked\r\n"
# contentType = "Content-Type: application/x-www-urlencoded\r\n"
# requestBody = "0\r\n\r\nG\r\n"

#finalMessage = message + hostHeader + contentLength + transferEncoding + contentType + "\r\n" + requestBody

#url = sys.argv[1]

subprocess.check_output([r"sed -i 's/Host.*/Host: {0}/g' temp.txt".format(host)], shell=True),
finalMessage =  subprocess.check_output([r"sed -z 's/\n/\r\n/g' temp.txt"], shell=True)

# print subprocess.check_output([r"sed -z 's/\n/\r\n/g' temp.txt"], shell=True),
# filepath='temp.txt'
# with open(filepath) as fp:
#     line2 = fp.read()
#     line2.replace("\\n", "\\r\n")
#     finalMessage = line2
#     print(line2)

#
#  with open(filepath) as fp:
#     line2 = fp.read()
#     print(line2)
#
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslWrappedSock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)
sslWrappedSock.connect((host, port))
sslWrappedSock.sendall(finalMessage)
print(sslWrappedSock.recv(4096))
sslWrappedSock.close()
