import os
from ..classes import Disk

disk_path = "/sys/block"


def read(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.readline().strip()
    else:
        return None


def get():
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
