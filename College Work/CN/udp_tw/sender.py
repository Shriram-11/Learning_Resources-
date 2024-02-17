# UDP Client
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server (localhost) and port number
server_address = ('localhost', 12345)

try:
    # Define your message
    while True:
        message = input('Enter message:')

        # Send the message
        print(f'Sending "{message}"')
        sent = sock.sendto(message.encode(), server_address)

except Exception as e:
    print(f'An error occurred: {e}')

finally:
    # Close the socket
    print('Closing socket')
    sock.close()
