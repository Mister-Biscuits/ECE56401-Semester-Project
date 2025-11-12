import cli_login as cli
import socket

def run_login_flow():
    salt = diffie_hellman_comm()

    username, hashed_pass = cli.get_credentials(salt)


def diffie_hellman_comm():
    salt = 234

    
    return salt