#!/bin/zsh
hiddify &
pid=$!
sleep 5 # give it time to open
qdbus6 org.kde.KWin /KWin org.kde.KWin.minimizeWindow $pid
