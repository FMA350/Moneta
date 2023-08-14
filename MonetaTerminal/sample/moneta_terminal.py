import threading
import time
from endpoint import ServerWrapper


def main_loop():
    while True:
        print("Updating prices...")
        time.sleep(5)

def main() -> None:
    print("Terminal Starting...")

    server = ServerWrapper()
    tcp_server = threading.Thread(target=server.run_server)
    tcp_server.run()

    print("Entering the main loop...")
    main_loop()
    

if __name__ == "__main__":
    main()