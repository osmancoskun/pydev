import os
from ..classes import Motherboard

demi_path = "/sys/devices/virtual/dmi/id"


def read(file_path):
    """
    Read the content of a file if it exists and return the first line stripped of leading and trailing whitespace.

    :param file_path: The path to the file.
    :return: The first line of the file, stripped of leading and trailing whitespace, or None if the file does not exist.
    """
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            return f.readline().strip()


def get():
    """
    Retrieve motherboard information from the /sys/devices/virtual/dmi/id directory and yield an instance of the Motherboard class.

    :yield: An instance of the Motherboard class populated with vendor, device, and version information.
    """
    vendor = read(os.path.join(demi_path, "board_vendor"))
    device = read(os.path.join(demi_path, "board_name"))
    version = read(os.path.join(demi_path, "board_version"))
    yield Motherboard(vendor=vendor, device=device, version=version)
