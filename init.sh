#!/bin/zsh
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 1
sleep 1
konsole --noclose -e zsh -c "pipes.sh -K -C -f 20" &
konsole --noclose -e zsh -c "bpytop" &
/home/ryan/dotfiles/conky/launch_conkys.sh &