import os
import json
from src import classes

arch_pci_ids_path = "/usr/share/hwdata/pci.ids"
deb_pci_ids_path = "/usr/share/misc/pci.ids"

pci_dev_path = "/sys/bus/pci/devices"
pci_id_paths = ["/usr/share/misc/pci.ids", "/usr/share/hwdata/pci.ids"]

pci_ids = None
for pci_id_path in pci_id_paths:
    if os.path.exists(pci_id_path):
        with open(arch_pci_ids_path) as f:
            pci_ids = f.readlines()


def int2hex(num):
    """
    Convert an integer to its hexadecimal string representation.

    :param num: The integer to convert.
    :return: A string representing the hexadecimal value of the integer.
    """
    return str(hex(num)[2:]).upper()


def get_pci_vendor(pci):
    """
    Retrieve the PCI vendor information from the pci.ids file.

    :param pci: The PCI vendor ID as a string.
    :return: The line from the pci.ids file that starts with the provided PCI vendor ID.
    """
    for line in pci_ids:
        if line.startswith(pci):
            return line


def get_pci_devices():
    """
    Generator function to retrieve PCI devices information.

    :yield: An instance of the BaseDevice class with vendor and device information.
    """
    for paths, dirs, files in os.walk(pci_dev_path):
        if dirs:
            for dir in dirs:
                vendor_pci = None
                vendor_path = os.path.join(pci_dev_path, dir, "vendor")
                if os.path.exists(vendor_path):
                    with open(vendor_path) as f:
                        vendor_pci = f.readline().strip()

                with open(os.path.join(pci_dev_path, dir, "device")) as f:
                    device_name = f.read().strip()[2:].upper()

                yield classes.BaseDevice(
                    vendor=get_pci_vendor(vendor_pci), device=device_name
                )


def parse_pci_ids():
    """
    Parse the PCI IDs from the pci.ids files and create a dictionary of devices.

    :return: A dictionary where keys are vendor IDs and values are dictionaries with vendor and device information.
    """
    for p in pci_id_paths:
        if os.path.isfile(p):
            with open(p, "r") as f:
                lines = f.readlines()
            devices = {}
            current_vendor = None

            for line in lines:
                if line.startswith("#") or line.strip() == "":
                    continue

                if not line.startswith("\t"):
                    # This is a vendor entry
                    if current_vendor:
                        devices[current_vendor] = vendor_info
                    vendor_id, vendor_name = line.strip().split(" ", 1)
                    current_vendor = int2hex(int(vendor_id, 16))
                    vendor_info = {"vendor_name": vendor_name.strip(), "devices": []}
                else:
                    # This is a device entry
                    device_id, device_name = line.strip().split(" ", 1)
                    vendor_info["devices"].append(
                        {
                            "device_id": int2hex(int(device_id, 16)),
                            "device_name": device_name.strip(),
                            "vendor_name": vendor_info["vendor_name"],
                        }
                    )
            if current_vendor:
                devices[current_vendor] = vendor_info
            with open("qwe.json", "a") as f:
                f.write(json.dumps(devices))
            return devices


parsed_pci_ids = parse_pci_ids()


def get_device_name(vendor_id, device_id):
    """
    Retrieve the device name for a given vendor and device ID.

    :param vendor_id: The vendor ID of the device.
    :param device_id: The device ID of the device.
    :return: The name of the device.
    """
    for dev in parsed_pci_ids[vendor_id]["devices"]:
        if dev["device_id"] == device_id:
            return dev["device_name"]
