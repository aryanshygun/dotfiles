#!/bin/zsh
sleep 1

konsole --new-tab -e bpytop &
konsole --new-tab -e pipes.sh &
konsole --new-tab -e cmatrix -a -b -C White &