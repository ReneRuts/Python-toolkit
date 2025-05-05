class Config:
    def __init__(self):
        self.MAX_HOSTS = 5
        self.DEFAULT_PORTS = [20, 80, 443, 3306]
    
    def update_config(self, max_hosts=None, default_ports=None):
        if max_hosts is not None:
            self.MAX_HOSTS = max_hosts
        if default_ports is not None:
            if all(isinstance(port, int) for port in default_ports):
                self.DEFAULT_PORTS = default_ports
            else:
                raise ValueError("All ports must be integers.")
    def show_config(self):
            print("\n[Current Configuration]")
            print(f"Max Hosts: {self.MAX_HOSTS}")
            print(f"Default Ports: {self.DEFAULT_PORTS}")

config = Config()