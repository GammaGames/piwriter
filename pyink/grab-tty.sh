#!/bin/sh

GRAB_VT='1'
DEVICE=${FRAMEBUFFER:-/dev/fb0}

current_vt=$(fgconsole)
chvt "$GRAB_VT"
if [ -z "$3" ]
then
    fbcat "$DEVICE"
else
    fbcat "$DEVICE" > "$3"
fi
chvt "$current_vt"
