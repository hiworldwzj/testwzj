import socket
import time

def start_client(host='127.0.0.1', port=65432, message='Hello, Server!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("已连接到服务器")

        # 记录发送时间
        while True:
            start_time = time.time()
            client_socket.sendall(message.encode())
            print(f"发送数据: {message}")
    
            data = client_socket.recv(1024)
            end_time = time.time()
    
            # 计算延迟
            delay = end_time - start_time
            print(f"接收到数据: {data.decode()}")
            print(f"发送到接收的延迟: {delay:.6f} 秒")

if __name__ == "__main__":
    start_client()
