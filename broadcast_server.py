import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

broadcast_ip = "255.255.255.255"
port = 6666

while True :
    data_send = input("Enter data for send : ")
    if data_send == "exit":
        s.sendto("C".encode(), (broadcast_ip, port))
        s.close()
        break
        
    s.sendto(data_send.encode(), (broadcast_ip, port))

# date => 6/18/2026  17:16 PM