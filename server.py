import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"服务器启动，监听 {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"连接来自 {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"接收到数据: {data.decode()}")
                conn.send(data)  # 回传接收到的数据

if __name__ == "__main__":
    start_server()
