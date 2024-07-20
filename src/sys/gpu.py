import os
from ..classes import GPU
from ..utils import parsed_pci_ids, int2hex, get_device_name

gpu_class = 0x030000
sec_gpu_class = 0x030200
pci_dev_path = "/sys/bus/pci/devices"
pci_id_paths = ["/usr/share/misc/pci.ids", "/usr/share/hwdata/pci.ids"]


def get():
    """
    Generator function to retrieve GPU information from the /sys/bus/pci/devices directory.

    :yield: An instance of the GPU class populated with information about each GPU.
    """
    for root, dirs, files in os.walk(pci_dev_path):
        for pci_dir in dirs:
            dev_content_path = os.path.join(root, pci_dir, "class")
            if os.path.exists(dev_content_path):
                with open(dev_content_path, "r") as f:
                    cont = f.readline().strip()
                    cont = int(cont, 16)
                    if cont == gpu_class or cont == sec_gpu_class:
                        is_secondary_gpu = cont == sec_gpu_class
                        vendor_id = None
                        driver = None
                        device_id = cont
                        ven_content_path = os.path.join(root, pci_dir, "vendor")
                        if os.path.exists(ven_content_path):
                            with open(ven_content_path) as f:
                                vendor_id = f.readline().strip()
                                vendor_id = int2hex(int(vendor_id, 16))
                        dev_content_path = os.path.join(root, pci_dir, "device")
                        if os.path.exists(dev_content_path):
                            with open(dev_content_path) as f:
                                device_id = f.readline().strip()
                                device_id = int2hex(int(device_id, 16))
                        drv_content_path = os.path.join(
                            root, pci_dir, "driver", "module"
                        )
                        if os.path.exists(drv_content_path):
                            gpu_drv_p = os.readlink(drv_content_path)
                            driver = os.path.basename(gpu_drv_p)
                        vendor = parsed_pci_ids[vendor_id]["vendor_name"]
                        device = get_device_name(vendor_id, device_id)
                        yield GPU(
                            vendor=vendor,
                            vendor_id=vendor_id,
                            device=device,
                            device_id=device_id,
                            driver=driver,
                            is_secondary_gpu=is_secondary_gpu,
                        )
