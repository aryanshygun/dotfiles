#!/bin/zsh
pkill -x conky
sleep 1
python3 /home/ryan/dotfiles/conky/app.py
sleep 2
conky -dq -c ~/dotfiles/conky/widgets/system.conf
conky -dq -c ~/dotfiles/conky/widgets/clock.conf
conky -dq -c ~/dotfiles/conky/widgets/battery.conf
conky -dq -c ~/dotfiles/conky/widgets/network.conf
conky -dq -c ~/dotfiles/conky/widgets/processes.conf
conky -dq -c ~/dotfiles/conky/widgets/memory.conf
conky -dq -c ~/dotfiles/conky/widgets/filesystem.conf
conky -dq -c ~/dotfiles/conky/widgets/weather.conf
