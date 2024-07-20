from ..classes import CPU

cpuinfo_path = "/proc/cpuinfo"


def line_split(line):
    """
    Split a line from /proc/cpuinfo on the tab and colon characters and strip whitespace.

    :param line: The line to split.
    :return: The part of the line after the tab and colon, stripped of leading and trailing whitespace.
    """
    return line.split("\t:")[1].strip()


def get():
    """
    Parse the /proc/cpuinfo file to retrieve CPU information and return an instance of the CPU class.

    :return: An instance of the CPU class populated with information from /proc/cpuinfo.
    """
    with open(cpuinfo_path, "r") as f:
        file_content = f.readlines()
        model = None
        vendor = None
        core_no = None
        microcode = None
        thread_no = None
        for line in file_content:
            if "model name" in line:
                model = line_split(line)
            if "vendor_id" in line:
                vendor = line_split(line)
            if "microcode" in line:
                microcode = line_split(line)
            if "cpu core" in line:
                core_no = line_split(line)
            if "siblings" in line:
                thread_no = line_split(line)

        return CPU(
            model=model,
            microcode=microcode,
            core_no=core_no,
            thread_no=thread_no,
            vendor=vendor,
            device="CPU",
        )
