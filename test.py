import utils
devs = utils.get_pci_devices()
for dev in devs:
    print(dev.vendor)
