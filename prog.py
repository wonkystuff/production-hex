import sys
import subprocess
import os
import glob

hex_file = sys.argv[1]
serialPort = sys.argv[2]

parts = hex_file.split(".")[0].split("_")
print(parts)

device = parts[1].lower()
home_dir = os.path.expanduser("~")

progpy = glob.glob(
    os.path.join(home_dir, "Library", "Arduino15", "**/prog.py"), recursive=True
)[0]

# Use avrdude if it's installed (v7.0 or more supports serialupdi):
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

# or use prog.py from the 'megaTinyCore' package
# subprocess.call(
#     [
#         "python3",
#         "-u",
#         progpy,
#         "-t",
#         "uart",
#         "-u",
#         serialPort,
#         "-b",
#         "57600",
#         "-d",
#         DEVICE,
#         "-f",
#         hex_file,
#         "-a",
#         "write",
#         "-v",
#     ]
# )
