#/bin/bash -e

# not particularly user-friendly, but I'm trying. Uses python installed alongside the megaTinyCore package, and their prog.py script also.

if [ "$#" -ne 3 ]; then
   echo "Usage : $0 <Arduino package directory> <serial port> <hex file>"
   exit 1
fi

SERPORT=$2
HEXFILE=$3

# locate the installation path for megaTinyCore
MEGATINYCOREPATH=$(find $1 -name 'megaTinyCore' -type d -print -quit)
if [[ -z "$MEGATINYCOREPATH" ]]; then
   echo "megaTinyCore is not installed - please install it using the boards manager of the Arduino IDE (See https://github.com/SpenceKonde/megaTinyCore)"
   exit 1
fi
echo megaTinyCore has been found here: $MEGATINYCOREPATH

PYTHONPATH=$(find $MEGATINYCOREPATH -name 'python3' -type f -print -quit)

$PYTHONPATH ./progUpdi.py -f $HEXFILE -p $SERPORT -m $MEGATINYCOREPATH
