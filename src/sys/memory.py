import psutil


def get():
    """
    Retrieve the total physical memory in bytes using the psutil library.

    :return: The total physical memory in bytes.
    """
    return psutil.virtual_memory().total
