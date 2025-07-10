#!/bin/bash

# VSCode ---------------------------------------------
VSCODE_SETTINGS="$HOME/.config/Code/User/settings.json"
VSCODE_THEME="Tokyo Night Light"
tmpfile=$(mktemp)
jq --arg theme "$VSCODE_THEME" '.["workbench.colorTheme"] = $theme' "$VSCODE_SETTINGS" > "$tmpfile" && mv "$tmpfile" "$VSCODE_SETTINGS"
echo "Light Mode Activated - VScode [$VSCODE_THEME]"

# Konsole ---------------------------------------------
SOURCE="../konsole/RyanLight.colorscheme"
DEST="$HOME/.local/share/konsole/RyanMode.colorscheme"

cp "$SOURCE" "$DEST"
sleep 1
echo "Light Mode Activated - Konsole [Monochrome - RyanLight]"

# Conky ---------------------------------------------
COLOR_JSON="$HOME/dev/dotfiles/conky/colors.json"
cat > "$COLOR_JSON" <<EOF
{
  "background": "#D6D8DF",
  "foreground": "#808284"
}
EOF
pkill conky
"$HOME/dev/dotfiles/conky/launch_conkys.sh"
echo "Light Mode Activated - Conky [Changed colors.json]"

# KDE Color ---------------------------------------------
plasma-apply-colorscheme Ryantest >/dev/null 2>&1
echo "Light Mode Activated - KDE Color [Ryantest.colors]"
