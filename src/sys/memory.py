import psutil


def get():
    return psutil.virtual_memory().total
