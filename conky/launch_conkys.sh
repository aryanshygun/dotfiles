#!/bin/zsh
sleep 1
conky -dq -c conky_widgets/memory.conf
conky -dq -c conky_widgets/battery.conf
conky -dq -c conky_widgets/filesystem.conf
conky -dq -c conky_widgets/network.conf
conky -dq -c conky_widgets/system.conf
conky -dq -c conky_widgets/processes.conf
conky -dq -c conky_widgets/time.conf
