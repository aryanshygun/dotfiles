#!/bin/zsh
sleep 3
conky -dq -c ~/dev/dotfiles/conky/widgets/system.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/clock.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/battery.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/network.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/processes.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/memory.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/filesystem.conf
conky -dq -c ~/dev/dotfiles/conky/widgets/weather.conf
