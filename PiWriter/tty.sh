#!/bin/sh

GRAB_VT=$1
DEVICE=${FRAMEBUFFER:-/dev/fb0}

current_vt=$(fgconsole)
chvt "$GRAB_VT"
if [ -z "$2" ]
then
    fbcat "$DEVICE"
else
    fbcat "$DEVICE" > "$2"
fi
chvt "$current_vt"
