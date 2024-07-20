import os
from ..classes import Disk

disk_path = "/sys/block"


def read(file_path):
    """
    Read the content of a file if it exists.

    :param file_path: The path to the file.
    :return: The first line of the file stripped of leading and trailing whitespace, or None if the file does not exist.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.readline().strip()
    else:
        return None


def get():
    """
    Generator function to retrieve disk information from the /sys/block directory.

    :yield: An instance of the Disk class populated with information about each disk.
    """
    for root, dirs, files in os.walk(disk_path):
        for dir in dirs:
            if "loop" in dir:
                continue
            else:
                size = read(os.path.join(root, dir, "size"))
                device = read(os.path.join(root, dir, "device", "model"))
                serial = read(os.path.join(root, dir, "device", "serial"))
                firmware_rev = read(os.path.join(root, dir, "device", "firmware_rev"))
                if not firmware_rev:
                    firmware_rev = read(os.path.join(root, dir, "device", "rev"))
                yield Disk(
                    size=size, device=device, serial=serial, firmware_rev=firmware_rev
                )
