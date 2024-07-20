from ..classes import CPU

cpuinfo_path = "/proc/cpuinfo"


def line_split(line):
    return line.split("\t:")[1].strip()


def get():
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
