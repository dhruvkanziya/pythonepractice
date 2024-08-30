import socket

def scanports(ip,startingpoint,endingpoint):

    for port in range(startingpoint,endingpoint+1):
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     socket.setdefaulttimeout(1)

    ip = "43.204.75.218"
    start = 79
    end = 83

    result = not socket.socket().connect_ex((ip,80))
    socket.timeout(1)
    print(result)