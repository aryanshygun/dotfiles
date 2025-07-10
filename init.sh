#!/bin/zsh

konsole --noclose -e zsh -c "bpytop" &
konsole --noclose -e zsh -c "pipes.sh -K -C -f 20"
/home/ryan/dev/dotfiles/conky/launch_conkys.sh &
