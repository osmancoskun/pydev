import os

import classes

arch_pci_ids_path = "/usr/share/hwdata/pci.ids"
deb_pci_ids_path = "/usr/share/misc/pci.ids"


network_dev_path = "/sys/class/net"


def pci_ids():
    pci_ids = open("/usr/share/hwdata/pci.ids", "r").readlines()
    devices = {}
    cur_vendor = None
    for line in pci_ids:
        if line.startswith("#") or line.strip() == "":
            continue
        if not line.startswith("\t"):
            vendor_id, vendor_name = line.strip().split(" ", 1)
            print(type(vendor_id))
            devices[vendor_id] = {
                "vendor_id": vendor_id,
                "vendor_name": vendor_name.strip(),
                "devices": {},
            }
            devices[vendor_id]
            cur_vendor = vendor_id
        else:
            device_id, device_name = line.strip().split(" ", 1)

            devices[cur_vendor]["devices"][device_id] = device_name.strip()

    # for dev in devices:
    # print("dev vendor: ", devices[dev]["vendor_id"], devices[dev]["vendor_name"])
    return devices
