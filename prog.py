import sys
import subprocess
import os
import glob

hex_file = sys.argv[1]
serialPort = sys.argv[2]

parts = hex_file.split(".")[0].split("_")
device = parts[1].lower()

home_dir = os.path.expanduser("~")
progpy = glob.glob(os.path.join(home_dir, "Library", "Arduino15", "**/prog.py"), recursive=True)[0]

subprocess.call(
    [
        "python3",
        "-u",
        progpy,
        "-t",
        "uart",
        "-u",
        serialPort,
        "-b",
        "57600",
        "-d",
        device,
        "--fuses",
        "0:0x00",
        "2:0x00",
        "6:0x00",
        "7:0x00",
        "8:0x00",
        "-f",
        hex_file,
        "-a",
        "write",
        "-v",
    ]
)
