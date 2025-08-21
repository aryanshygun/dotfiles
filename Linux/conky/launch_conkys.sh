#!/bin/zsh
pkill -x conky
sleep 1
python3 /home/ryan/dotfiles/Linux/conky/app.py
sleep 2
conky -dq -c ~/dotfiles/Linux/conky/widgets/system.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/clock.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/battery.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/network.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/processes.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/memory.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/filesystem.conf
conky -dq -c ~/dotfiles/Linux/conky/widgets/weather.conf
