import socket
import traceback


def run(host, port):
    try:
        with socket.socket(family=socket.AF_INET) as soc:
            soc.settimeout(5)
            soc.connect((host, port))
            soc.send("hello".encode("utf-8"))

            recv = soc.recv(4096).decode()
            print(recv)
    except ConnectionError:
        print(traceback.format_exc())
    except TimeoutError:
        print(traceback.format_exc())
    except Exception:
        print(traceback.format_exc())


if __name__ == "__main__":
    run("127.0.0.1", 1234)
