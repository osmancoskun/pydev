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


class GPU(BaseDevice):
    def __init__(self, *args, vendor_id, device_id, is_secondary_gpu, driver, **kwargs):
        super().__init__(*args, **kwargs)
        self.vendor_id = vendor_id
        self.device_id = device_id
        self.driver = driver
        self.is_secondary_gpu = is_secondary_gpu


class Memory:
    def __init__(self, *args, total_memory, **kwargs):
        self.total_memory = total_memory


class Motherboard(BaseDevice):
    def __init__(self, *args, version, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = version
