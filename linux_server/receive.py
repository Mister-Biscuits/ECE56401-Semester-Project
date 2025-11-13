# tls_server.py
import socket, ssl, threading

HOST = "0.0.0.0"
PORT = 5000
CERTFILE = "/path/to/server.crt"
KEYFILE  = "~/media/sf_School/ECE56401_Computer_Security/project_server/server.key"

def handle_client(ssock, addr):
    print("[+] TLS connection from", addr)
    try:
        with ssock, ssock.makefile("r", encoding="utf-8") as f:
            username = f.readline().rstrip("\n")
            pw_or_hash = f.readline().rstrip("\n")
            print("User:", username)
            print("Payload:", pw_or_hash[:80], "...")
            ssock.sendall(b"OK: secure credentials received\n")
    except Exception as e:
        print("Client handler error:", e)

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    lsock.bind((HOST, PORT))
    lsock.listen(5)
    print("TLS server listening", HOST, PORT)

    while True:
        conn, addr = lsock.accept()
        try:
            ssock = context.wrap_socket(conn, server_side=True)
        except ssl.SSLError as e:
            print("SSL wrap failed:", e)
            conn.close()
            continue
        threading.Thread(target=handle_client, args=(ssock, addr), daemon=True).start()

if __name__ == "__main__":
    main()
