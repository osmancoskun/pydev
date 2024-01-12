class BaseDevice:
    def __init__(self, vendor: str = None, device: str = None):
        self.vendor = vendor
        self.device = device

    def __str__(self):
        return f"Vendor: {self.vendor}. Device: {self.device}"


class NetworkDevice(BaseDevice):
    def __init__(self, mac_address: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mac_address = mac_address
