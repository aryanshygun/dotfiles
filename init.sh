#!/bin/zsh
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 1 &
~/dotfiles/conky/launch_conkys.sh &
sleep 1
konsole -e 'pipes.sh -K -C -f 20 -t 3' &
sleep 1
konsole -e 'bpytop' &
sleep 1
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 2
sleep 1
konsole -e 'cava' &
konsole -e 'tty-clock -c -C 7 -S -b -n -B -D' &
spotify &
sleep 1
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 3
hiddify