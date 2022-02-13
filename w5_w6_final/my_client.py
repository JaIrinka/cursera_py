import socket
import time


class Client:

    def __init__(self, address="", port=10001, timeout=None):
        try:
            self.sock = socket.create_connection((address, port), timeout)
        except Exception:
            raise ClientError

    def put(self, metric_key: str, metric_value: float, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        try:
            self.sock.sendall(f"put {str(metric_key)} {str(metric_value)} {str(timestamp)}\n".encode("utf-8"))
            status = self.sock.recv(1024).decode()
        except Exception as e:
            raise ClientError

        if status.startswith("ok"):
            pass
        else:
            raise ClientError

    def get(self, metric_key: str):
        result = {}

        try:
            self.sock.sendall(f"get {str(metric_key)}\n".encode("utf-8"))
            data = self.sock.recv(1024).decode()

            data_strs = data.split('\n')
            if data_strs[0] != "ok":
                raise ClientError

            for data_item in data_strs[1:-2]:
                metric_key, metric_value, timestamp = data_item.split()
                if metric_key not in result:
                    result[metric_key] = []
                result[metric_key].append((int(timestamp), float(metric_value)))

            for res in result:
                # тут нужно поситать про sotr
                result[res].sort(key=lambda y: y[0])

        except Exception:
            raise ClientError

        return result


class ClientError(Exception):
    pass
