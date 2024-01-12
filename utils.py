import os

import classes
import parsers

arch_pci_ids_path = "/usr/share/hwdata/pci.ids"
deb_pci_ids_path = "/usr/share/misc/pci.ids"


pci_ids = open("/usr/share/hwdata/pci.ids", "r").readlines()

network_dev_path = "/sys/class/net"
parsed_pci_ids = parsers.pci_ids()


def get_pci_names(vendor: str = None, device: str = None):
    if not vendor:
        return None
    try:
        result = {"vendor_name": parsed_pci_ids[vendor]["name"]}
    except KeyError:
        result = "Vendor not found"
    if device:
        result["device_name"] = parsed_pci_ids[vendor]["devices"][device]["name"]
    return result


def get_pci_devices():
    pci_dev_path = "/sys/bus/pci/devices/"

    for paths, dirs, files in os.walk(pci_dev_path):
        if dirs:
            for dir in dirs:
                with open(os.path.join(pci_dev_path, dir, "vendor")) as f:
                    vendor_name = f.read().strip()[2:].upper()
                with open(os.path.join(pci_dev_path, dir, "device")) as f:
                    device_name = f.read().strip()[2:].upper()

                data = get_pci_names(vendor_name, device_name)
                yield classes.BaseDevice(
                    vendor=data["vendor_name"],
                    device=data["device_name"],
                )


def get_network_devices():
    for paths, dirs, files in os.walk(network_dev_path):
        if dirs:
            for dir in dirs:
                mac_address = None
                device_pci = None
                vendor_pci = None
                mp = os.path.join(network_dev_path, dir, "address")
                if os.path.exists(mp):
                    mac_address = open(mp).read()[:-2]

                dp = os.path.join(network_dev_path, dir, "device", "device")
                if os.path.exists(dp):
                    device_pci = open(dp).read()[:-2]

                vp = os.path.join(network_dev_path, dir, "device", "vendor")
                if os.path.exists(vp):
                    vendor_pci = open(vp).read()[:-1]

                yield classes.NetworkDevice(
                    mac_address=mac_address,
                    vendor=get_pci_names(vendor=vendor_pci),
                    device=device_pci,
                )
