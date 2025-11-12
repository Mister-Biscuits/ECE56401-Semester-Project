# receive.py
# Rudimentary TCP server for Computer Security project
# Listens for connections and receives username and password/hash

import socket
import threading

def handle_client(conn: socket.socket, addr):
    print(f"[+] Connection from {addr}")
    try:
        # Wrap socket in a file-like object for easy line reading
        with conn, conn.makefile("r", encoding="utf-8") as client_file:
            # Expect two lines: username and password/hash
            username = client_file.readline().rstrip("\n")
            password_or_hash = client_file.readline().rstrip("\n")

            if not username:
                print("[!] Empty username received")
                return

            print(f"[+] Received login attempt:")
            print(f"    Username: {username}")
            print(f"    Password/Hash: {password_or_hash}")

            # For now, just acknowledge. This is where you will:
            #   - Look up user in DB
            #   - Verify hash
            #   - Apply your blocklist logic, etc.
            response = "OK: credentials received\n"
            conn.sendall(response.encode("utf-8"))

    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")


def main():
    print(f"[*] Starting rudimentary login server on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print("[*] Server listening for incoming connections")

        while True:
            conn, addr = server_sock.accept()
            # Simple threading so multiple clients do not block each other
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()


if __name__ == "__main__":
    main()