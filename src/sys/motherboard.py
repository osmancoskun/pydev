import os
from ..classes import Motherboard

demi_path = "/sys/devices/virtual/dmi/id"


def read(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            return f.readline().strip()


def get():
    vendor = read(os.path.join(demi_path, "board_vendor"))
    device = read(os.path.join(demi_path, "board_name"))
    version = read(os.path.join(demi_path, "board_version"))
    yield Motherboard(vendor=vendor, device=device, version=version)
