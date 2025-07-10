#!/bin/bash

# VSCode ---------------------------------------------
VSCODE_SETTINGS="$HOME/.config/Code/User/settings.json"
VSCODE_THEME="Monokai Pro (Filter Spectrum)"
tmpfile=$(mktemp)
jq --arg theme "$VSCODE_THEME" '.["workbench.colorTheme"] = $theme' "$VSCODE_SETTINGS" > "$tmpfile" && mv "$tmpfile" "$VSCODE_SETTINGS"
echo "Dark Mode Activated - VScode [$VSCODE_THEME]"

# Konsole ---------------------------------------------
SOURCE="../konsole/RyanDark.colorscheme"
DEST="$HOME/.local/share/konsole/RyanMode.colorscheme"

cp "$SOURCE" "$DEST"
sleep 1
konsoleprofile colors=DarkMode
echo "Dark Mode Activated - Konsole [Monochrome - RyanDark]"

# Conky ---------------------------------------------
COLOR_JSON="$HOME/dev/dotfiles/conky/colors.json"
cat > "$COLOR_JSON" <<EOF
{
  "background": "#1C1C1E",
  "foreground": "#FFFFFF"
}
EOF
pkill conky
"$HOME/dev/dotfiles/conky/launch_conkys.sh"
echo "Dark Mode Activated - Conky [Changed colors.json]"

# KDE Color ---------------------------------------------
plasma-apply-colorscheme Monochrome >/dev/null 2>&1
echo "Dark Mode Activated - KDE Color [Monochrome.colors]"
