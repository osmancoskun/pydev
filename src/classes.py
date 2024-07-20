class BaseDevice:
    def __init__(self, vendor=None, device=None):
        self.vendor = vendor
        self.device = device

    def __str__(self):
        return f"Vendor: {self.vendor}. Device: {self.device}"


class CPU(BaseDevice):

    def __init__(self, *args, model, microcode, core_no, thread_no, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.microcode = microcode
        self.core_no = core_no
        self.thread_no = thread_no


class Disk(BaseDevice):
    def __init__(self, *args, serial, firmware_rev, size, **kwargs):
        super().__init__(*args, **kwargs)
        self.serial = serial
        self.firmware_rev = firmware_rev
        self.size = int(size)
        self.size_GB = self.size * 512 / 1024 / 1024 / 1024
