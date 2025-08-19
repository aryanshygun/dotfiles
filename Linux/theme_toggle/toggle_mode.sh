#!/bin/bash

STATE_FILE="/tmp/mode_toggle_state"

if [[ ! -f "$STATE_FILE" ]]; then
    echo "light" > "$STATE_FILE"
fi

CURRENT_MODE=$(cat "$STATE_FILE")

if [[ "$CURRENT_MODE" == "light" ]]; then
    echo "dark" > "$STATE_FILE"
    /home/ryan/dotfiles/Linux/theme_toggle/dark_mode.sh
else
    echo "light" > "$STATE_FILE"
    /home/ryan/dotfiles/Linux/theme_toggle/light_mode.sh
fi
