class Config:
    def __init__(self):
        # Service comparator settings
        self.MAX_HOSTS = 5
        self.DEFAULT_PORTS = [20, 80, 443, 3306]
        # Mini DDOS settings
        self.MAX_THREADS = 10
        self.REQUEST_RATE = 5
        self.PAYLOAD_SIZE = 5
        self.TARGET_HOST = "127.0.0.1"
        self.TARGET_PORT = 80
        # Password generator & Strength Analyzer settings
        self.PASS_INCLUDE_LOWER = True
        self.PASS_INCLUDE_UPPER = True
        self.PASS_INCLUDE_DIGITS = True
        self.PASS_INCLUDE_SYMBOLS = True
        self.PASS_LENGTH = 12

    def update_config(
        self,
        max_hosts=None, default_ports=None,
        max_threads=None, request_rate=None, payload_size=None,
        target_host=None, target_port=None,
        pass_lower=None, pass_upper=None, pass_digits=None, pass_symbols=None,
        pass_length=None
    ):
        if max_hosts is not None:
            self.MAX_HOSTS = max_hosts
        if default_ports is not None:
            self.DEFAULT_PORTS = default_ports
        if max_threads is not None:
            self.MAX_THREADS = max_threads
        if request_rate is not None:
            self.REQUEST_RATE = request_rate
        if payload_size is not None:
            self.PAYLOAD_SIZE = payload_size
        if target_host is not None:
            self.TARGET_HOST = target_host
        if target_port is not None:
            self.TARGET_PORT = target_port
        if pass_lower is not None:
            self.PASS_INCLUDE_LOWER = pass_lower
        if pass_upper is not None:
            self.PASS_INCLUDE_UPPER = pass_upper
        if pass_digits is not None:
            self.PASS_INCLUDE_DIGITS = pass_digits
        if pass_symbols is not None:
            self.PASS_INCLUDE_SYMBOLS = pass_symbols
        if pass_length is not None:
            self.PASS_LENGTH = pass_length

    def show_config(self, mode="all"):
        print("\n[Current Configuration]")

        if mode == "all" or mode == "service_comparator":
            print(f"Max Hosts: {self.MAX_HOSTS}")
            print(f"Default Ports: {self.DEFAULT_PORTS}")

        if mode == "all" or mode == "mini_ddos":
            print(f"Max Threads: {self.MAX_THREADS}")
            print(f"Request Rate: {self.REQUEST_RATE}")
            print(f"Payload Size: {self.PAYLOAD_SIZE}")
            print(f"Target Host: {self.TARGET_HOST}")
            print(f"Target Port: {self.TARGET_PORT}")

        if mode == "all" or mode == "password":
            print(f"Include Lowercase: {self.PASS_INCLUDE_LOWER}")
            print(f"Include Uppercase: {self.PASS_INCLUDE_UPPER}")
            print(f"Include Digits: {self.PASS_INCLUDE_DIGITS}")
            print(f"Include Symbols: {self.PASS_INCLUDE_SYMBOLS}")
            print(f"Default Length: {self.PASS_LENGTH}")

        print("----------------------------------")

config = Config()