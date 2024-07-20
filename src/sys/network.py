import os
from ..utils import parsed_pci_ids, get_device_name
from ..classes import Network

if_path = "/sys/class/net"


def read(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.readline().strip().upper()
    else:
        return None


def get():
    for root, dirs, files in os.walk(if_path):
        for interface in dirs:
            if interface != "lo":
                mac_address = read(os.path.join(root, interface, "address")).upper()
                is_wireless = os.path.exists(os.path.join(root, interface, "wireless"))
                device, vendor = None, None
                vendor_id = read(os.path.join(root, interface, "device", "vendor"))
                if vendor_id:
                    vendor_id = vendor_id[2:]
                    vendor = parsed_pci_ids[vendor_id]["vendor_name"]

                device_id = read(os.path.join(root, interface, "device", "device"))
                if device_id:
                    device_id = device_id[2:]
                    device = get_device_name(vendor_id, device_id)

                yield Network(
                    mac_address=mac_address,
                    is_wireless=is_wireless,
                    interface=interface,
                    vendor_id=vendor_id,
                    device_id=device_id,
                    vendor=vendor,
                    device=device,
                )
