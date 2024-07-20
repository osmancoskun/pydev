class BaseDevice:
    def __init__(self, vendor=None, device=None):
        """
        Initialize a base device with optional vendor and device identifiers.

        :param vendor: The vendor identifier of the device (default is None).
        :param device: The device identifier of the device (default is None).
        """

        self.vendor = vendor
        self.device = device

    def __str__(self):
        """
        Return a string representation of the base device.

        :return: A string describing the vendor and device.
        """
        return f"Vendor: {self.vendor}. Device: {self.device}"


class CPU(BaseDevice):
    def __init__(self, *args, model, microcode, core_no, thread_no, **kwargs):
        """
        Initialize a CPU device with specific attributes.

        :param model: The model name of the CPU.
        :param microcode: The microcode version of the CPU.
        :param core_no: The number of cores in the CPU.
        :param thread_no: The number of threads in the CPU.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.model = model
        self.microcode = microcode
        self.core_no = core_no
        self.thread_no = thread_no


class Disk(BaseDevice):
    def __init__(self, *args, serial, firmware_rev, size, **kwargs):
        """
        Initialize a Disk device with specific attributes.

        :param serial: The serial number of the disk.
        :param firmware_rev: The firmware revision of the disk.
        :param size: The size of the disk in sectors.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.serial = serial
        self.firmware_rev = firmware_rev
        self.size = int(size)
        self.size_GB = self.size * 512 / 1024 / 1024 / 1024


class GPU(BaseDevice):
    def __init__(self, *args, vendor_id, device_id, is_secondary_gpu, driver, **kwargs):
        """
        Initialize a GPU device with specific attributes.

        :param vendor_id: The vendor identifier of the GPU.
        :param device_id: The device identifier of the GPU.
        :param is_secondary_gpu: A boolean indicating if it is a secondary GPU.
        :param driver: The driver used by the GPU.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.vendor_id = vendor_id
        self.device_id = device_id
        self.driver = driver
        self.is_secondary_gpu = is_secondary_gpu


class Memory:
    def __init__(self, *args, total_memory, **kwargs):
        """
        Initialize a Memory device with the total memory attribute.

        :param total_memory: The total memory in bytes.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        self.total_memory = total_memory


class Motherboard(BaseDevice):
    def __init__(self, *args, version, **kwargs):
        """
        Initialize a Motherboard device with a version attribute.

        :param version: The version of the motherboard.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.version = version


class Network(BaseDevice):
    def __init__(
        self, *args, interface, mac_address, device_id, vendor_id, is_wireless, **kwargs
    ):
        """
        Initialize a Network device with specific attributes.

        :param interface: The network interface name.
        :param mac_address: The MAC address of the network device.
        :param device_id: The device identifier of the network device.
        :param vendor_id: The vendor identifier of the network device.
        :param is_wireless: A boolean indicating if the network device is wireless.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.interface = interface
        self.device_id = device_id
        self.vendor_id = vendor_id
        self.mac_address = mac_address
        self.is_wireless = is_wireless
