# production-hex

Public repo for hex firmware files used in non open-source wonkystuff modules. There may be occasional revisions in the case that bugs are found or extra functionality added.

Filename includes module name, target processor and version.

- 2023/12/10 - Initial commit of all MIDI hex files
- 2023/12/10 - Corrected MIDI-CV mode on mcc/4 (v1.1.1)
- 2023/12/11 - Added ATTiny85 and ATTiny25-based firmware
- 2024/03/10 - updated all MIDI modules with improved state machine (note on/off processing was faulty in the case of running status).
- 2024/03/23 - Version 1.3.0 of mb/1 — improved system-exclusive handling and other small improvements
- 2024/03/24 - Added hacky script to program UPDI devices.
  - Usage: "python3 prog.py <hex-name> <serial-port>" where hex name is one of the files in this directory and serial port is where your updi-programmer is attached. Only 'tested' on MacOS.
  - Needs the arduino 'MegaTinyCore' package installed.
- 2024/03/25 - added wrapper shell script which sorts out paths to the megaTinyCore package and its embedded python installation. An attempt to be cross-platform
  - Usage : `./progUpdi.sh <Arduino package directory> <serial port> <hex file>`
    - e.g. (on MacOS) `./progUpdi.sh ~/Library/Arduino15 /dev/cu.usbserial-21130 mdiv_ATtiny412_v1.1.0.hex`
- 2024/03/26 - Version 1.2.0 of mdiv — improved system-exclusive handling and other small improvements
