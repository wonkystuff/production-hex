import sys
import subprocess
import os
import glob
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port",
                    type=str,
                    default="",
                    help="Serial port to use.")

parser.add_argument("-f", "--file",
                    type=str,
                    default="",
                    help="Hex file to program.")

parser.add_argument("-m", "--mtc",
                    type=str,
                    default="",
                    help="Path to the MegaTinyCore installation.")

args = parser.parse_args()

if args.port == "" or args.file == "" or args.mtc == "":
    parser.print_help()
    sys.exit(0)

hex_file = args.file
serialPort = args.port

parts = hex_file.split(".")[0].split("_")
device = parts[1].lower()

progpy = glob.glob(os.path.join(args.mtc, "**/prog.py"), recursive=True)[0]

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
        "-f",
        hex_file,
        "-a",
        "write",
    ]
)
