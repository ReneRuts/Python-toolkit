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
    
    def update_config(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
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