import socket

HOST = ''
PORT = 8081
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
connection, address = listen_socket.accept()
request = connection.recv(1024)
print(request)
connection.sendall("""HTTP/1.1 200 OK
Content-type: text/html


<html>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>""".encode())
connection.close()
