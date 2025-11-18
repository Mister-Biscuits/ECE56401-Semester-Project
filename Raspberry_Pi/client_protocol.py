import cli_login as cli
import socket
import ssl

#This will be the main program to run for the client side. This will be dictating what actions need to be taken at a time
#

SERVER_HOST = "127.0.0.1"   # server IP or hostname
SERVER_PORT = 5000
SERVER_CERT = "/media/sf_School/ECE56401_Computer_Security/ECE56401-Semester-Project/linux_server/server.crt"

#gets salt from server and username and hashed password
#Returns username and hashed_pass
def run_login_flow():
    salt = diffie_hellman_comm()

    username, hashed_pass = cli.get_credentials()
    return username, hashed_pass


def diffie_hellman_comm():
    salt = 234
    return salt

def main():
    #Initialize ssl
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    #Gather information to send
    username, hashed_pass = run_login_flow()


    with socket.create_connection((SERVER_HOST, SERVER_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=SERVER_HOST) as ssock:
            # for self-signed local cert:
            context.load_verify_locations(cafile=SERVER_CERT)
            # Send lines as before
            ssock.sendall(f"{username}\n{hashed_pass}\n".encode("utf-8"))
            resp = ssock.recv(4096).decode("utf-8", errors="ignore").strip()
            print("Server:", resp)

if __name__ == "__main__":
    main()