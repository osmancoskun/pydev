import os

from src import classes

arch_pci_ids_path = "/usr/share/hwdata/pci.ids"
deb_pci_ids_path = "/usr/share/misc/pci.ids"


pci_ids = None
if os.path.exists(arch_pci_ids_path):
    with open(arch_pci_ids_path) as f:
        pci_ids = f.readlines()
else:
    with open(deb_pci_ids_path) as f:
        pci_ids = f.readlines()


def get_pci_vendor(pci):
    for line in pci_ids:
        if line.startswith(pci):
            return line


def get_pci_devices():
    pci_dev_path = "/sys/bus/pci/devices/"
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
