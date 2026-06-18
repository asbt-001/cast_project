import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "0.0.0.0"
port = 6666

c.bind((ip, port))

while True :
    my_data, addr = c.recvfrom(1024)

    data_server = my_data.decode()

    if data_server == "C":
        c.close()
        break
    
    print(f"""
    addr : {addr}
    data_server : {data_server}
    """)
    
# date => 6/18/2026  17:16 PM