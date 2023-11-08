import threading
import time
from CLI.CommandLineInterface import CLI
from endpoint import ServerWrapper


def main_loop():
    while True:
        print("Updating prices...")
        time.sleep(5)

def start_server():
    server = ServerWrapper()
    tcp_server = threading.Thread(target=server.run_server)
    tcp_server.run()

def start_cli():
    cli = CLI()
    cli_loop = threading.Thread(target=cli.MainLoop)
    cli_loop.run()


def main() -> None:
    #print("Terminal Starting...")
    #start_server()
    print("Starting Interpreter...")
    start_cli()

if __name__ == "__main__":
    main()