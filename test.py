import utils

devs = utils.get_network_devices()
for dev in devs:
    print("dev, mac, vendor")
    print(dev.device, dev.mac_address, dev.vendor)
