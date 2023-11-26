import socket

def handle_connection(client_socket):
    # Receive data from the client
    data = client_socket.recv(1024)
    
    # Echo back the received data
    client_socket.sendall(data)
    
    # Close the connection
    client_socket.close()

def run_server():
    # Specify the host and port to bind to
    host = '127.0.0.1'
    port = 12345
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Wait for a connection from a client
        client_socket, client_address = server_socket.accept()
        
        print(f"Accepted connection from {client_address}")
        
        # Handle the connection in a separate thread or process for scalability
        
        # For simplicity, we handle each connection in the main thread here
        handle_connection(client_socket)

if __name__ == "__main__":
    run_server()
