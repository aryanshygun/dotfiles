#!/bin/zsh
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 1 &
~/dotfiles/Linux/conky/launch_conkys.sh &
sleep 1
konsole -e 'pipes.sh -K -C -f 20 -t 3' &
sleep 1
konsole -e 'tty-clock -c -C 7 -S -b -n -B -D' &
sleep 1
konsole -e 'neofetch' &
sleep 1
konsole -e 'cmatrix -B -u 9 -C white -m' &
sleep 1
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 2
sleep 1
konsole -e 'bpytop' &
sleep 1
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 3
sleep 1
konsole -e 'cava' &
sleep 1
spotify &
sleep 1
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 4
hiddify
qdbus6 org.kde.KWin /KWin org.kde.KWin.setCurrentDesktop 5