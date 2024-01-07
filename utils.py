import os

import classes
arch_pci_ids_path = '/usr/share/hwdata/pci.ids'
deb_pci_ids_path = '/usr/share/misc/pci.ids'

pci_ids = open('/usr/share/hwdata/pci.ids',"r").readlines()



def get_pci_vendor(pci):
    for line in pci_ids:
        if line.startswith(pci):
            return line


def get_pci_devices():
    pci_dev_path = "/sys/bus/pci/devices/"

    for paths, dirs, files in os.walk(pci_dev_path):
        if dirs:
            for dir in dirs:
                with open(os.path.join(pci_dev_path,dir,'vendor')) as f:
                    vendor_name = f.read().strip()[2:].upper()
                with open(os.path.join(pci_dev_path,dir,'device')) as f:
                    device_name = f.read().strip()[2:].upper()
                
                yield classes.BaseDevice(vendor=get_pci_vendor(vendor_name),device=device_name)

