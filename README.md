# production-hex

Public repo for hex firmware files used in non open-source wonkystuff modules. There may be occasional revisions in the case that bugs are found or extra functionality added.

Filename includes module name, target processor and version.

- 2023/12/10 - Initial commit of all MIDI hex files
- 2023/12/10 - Corrected MIDI-CV mode on mcc/4 (v1.1.1)
- 2023/12/11 - Added ATTiny85 and ATTiny25-based firmware
- 2024/03/10 - updated all MIDI modules with improved state machine (note on/off processing was faulty in the case of running status).
- 2024/03/23 - Version 1.3.0 of mb/1 — improved system-exclusive handling and other small improvements