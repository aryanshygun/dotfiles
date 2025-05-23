#!/bin/zsh
sleep 1
conky -dq -c ~/Documents/startup_scripts/conky_widgets/memory.conf
conky -dq -c ~/Documents/startup_scripts/conky_widgets/battery.conf
conky -dq -c ~/Documents/startup_scripts/conky_widgets/filesystem.conf
conky -dq -c ~/Documents/startup_scripts/conky_widgets/network.conf
conky -dq -c ~/Documents/startup_scripts/conky_widgets/system.conf
conky -dq -c ~/Documents/startup_scripts/conky_widgets/processes.conf
conky -dq -c ~/Documents/startup_scripts/conky_widgets/time.conf
