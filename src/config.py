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
    
    def update_config(self, max_hosts=None, default_ports=None, max_threads=None, request_rate=None, payload_size=None, target_host=None, target_port=None):
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
        print("----------------------------------")

config = Config()