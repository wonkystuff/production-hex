import sys
import subprocess
import os
import glob

hex_file = sys.argv[1]
serialPort = sys.argv[2]

parts = hex_file.split(".")[0].split("_")
print(parts)

device = parts[1].lower()

# avrdude must be v7.0 or more to support serialupdi
# if it's not already on the path, then add it like this when invoking this script:
# PATH=$PATH:<path to avrdude> python3 prog.py <hex file> <serial port>

subprocess.call(
    [
        "avrdude",
        "-v",
        "-p",
        device,
        "-c",
        "serialupdi",
        "-b",
        "57600",
        "-P",
        serialPort,
        "-U",
        "flash:w:"+hex_file+":i",
    ]
)
