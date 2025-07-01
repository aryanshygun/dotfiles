opacity = 191

bg_color = "'#1C1C1E'"
fg_color = "'#FFFFFF'"

global_inner_margin = "8"  # looks best compared to 5 and 10. numbers are adjust for 8
space_between = 5  # space between each widget
base_left_margin = 10 + space_between  # 10 to start from edge + the space between
adjustment_from_top = -2  # offset to match the menubar
widgets = {
    "clock": {
        "name": "clock",
        "space_from_top": 57 + space_between + adjustment_from_top,
        "space_from_left": 0,
        "width": 130,
        "height": 0,
        "text": """
conky.text = [[
${font Oswald:size=14:bold}TODAY  ${hr 3}
${voffset -3}${font Oswald:size=31:bold}${alignc}${time %H:%M}${font}
${voffset 6}${font Oswald:size=13:bold}${alignc}${time %Y - %m - %d}
]];
        """,
    },
    "battery": {
        "name": "battery",
        "space_from_top": 57 + space_between + adjustment_from_top,
        "space_from_left": 130 + base_left_margin + space_between * 2,
        "width": 270,
        "height": 0,
        "text": """
conky.text = [[
${font Oswald:size=14:bold}Battery  ${hr 3}
${font}External ${alignr}${if_existing /sys/class/power_supply/BAT0/status Charging}Charging${else}${if_existing /sys/class/power_supply/BAT0/status Discharging}Discharging${else}${if_existing /sys/class/power_supply/BAT0/status Not charging}${endif}${endif}${endif} ${battery_percent BAT0}%
${battery_bar 5 BAT0}
Internal ${alignr}${if_existing /sys/class/power_supply/BAT1/status Charging}Charging${else}${if_existing /sys/class/power_supply/BAT1/status Discharging}Discharging${else}${if_existing /sys/class/power_supply/BAT1/status Not charging}Full${endif}${endif}${endif} ${battery_percent BAT1}%
${battery_bar 5 BAT1}
]]
        """,
    },
    "system": {
        "name": "system",
        "space_from_top": 186 + space_between * 2 + adjustment_from_top,
        "space_from_left": 0,
        "width": 230,
        "height": 0,
        "text": """
conky.text = [[
${font Oswald:size=13:bold}SYSTEM  ${hr 3}${font}
${font Oswald:size=11:bold}Distro ${font Oswald:size=9:bold}${alignr}${exec lsb_release -ds}
${font Oswald:size=11:bold}Kernel ${font Oswald:size=9:bold}${alignr}${color}${kernel}
${font Oswald:size=11:bold}Uptime ${font Oswald:size=9:bold}${alignr}${uptime}
]]
        """,
    },
    "filesystem": {
        "name": "filesystem",
        "space_from_top": 294 + space_between * 3 + adjustment_from_top,
        "space_from_left": 0,
        "width": 230,
        "height": 74,
        "text": """
conky.text = [[
${font Oswald:size=14:bold}FILE SYSTEM  ${hr 3}
${font}Root${alignr}${fs_used /} / ${fs_size /}
${fs_bar 5 /}
]]        
        """,
    },
    "memory": {
        "name": "memory",
        "space_from_top": 186 + space_between * 2 + adjustment_from_top,
        "space_from_left": 230 + base_left_margin + space_between * 2,
        "width": 170,
        "height": 187,
        "text": """
        conky.text = [[
${font Oswald:size=14:bold}Memory  ${hr 3}
${font}${mem} / ${memmax}${alignr}${memperc}%
${membar 5}
Name${alignr}MEM
${top_mem name 1}${alignr}${top_mem mem 1}gib
${top_mem name 2}${alignr}${top_mem mem 2}gib
${top_mem name 3}${alignr}${top_mem mem 3}gib
${top_mem name 4}${alignr}${top_mem mem 4}gib
${top_mem name 5}${alignr}${top_mem mem 5}gib
]]
        """,
    },
    "processes": {
        "name": "processes",
        "space_from_top": 388 + space_between * 4 + adjustment_from_top,
        "space_from_left": 161 + base_left_margin + space_between * 2,
        "width": 239,
        "height": 100,
        "text": """
conky.text = [[
${font Oswald:size=14:bold}Processes  ${hr 3}
${font}Freq ${alignr}$freq_g Ghz
CPU Temp ${alignr}${exec sensors | grep 'Package' | awk -F'+' '{print $2}' | awk -F'.' '{print $1}'}°C
${cpugraph cpu0 25,236}
Core 1 ${alignr}${cpu cpu1}% ${cpubar cpu1 9,140}
Core 2 ${alignr}${cpu cpu3}% ${cpubar cpu3 9,140}
Core 3 ${alignr}${cpu cpu5}% ${cpubar cpu5 9,140}
Core 4 ${alignr}${cpu cpu7}% ${cpubar cpu7 9,140}
Name ${alignr} PID   CPU   MEM
${top name 1} $alignr ${top pid 1}  ${top cpu 1}
${top name 2} $alignr ${top pid 2}  ${top cpu 2}
${top name 3} $alignr ${top pid 3}  ${top cpu 3}
]]
        """,
    },
    "network": {
        "name": "network",
        "space_from_top": 388 + space_between * 4 + adjustment_from_top,
        "space_from_left": 0,
        "width": 0,
        "height": 267,
        "text": """
conky.text = [[
${font Oswald:size=14:bold}${if_existing /sys/class/net/wlp3s0/operstate up}ONLINE${else}OFFLINE${endif}  ${hr 3}
${font Oswald:size=11:bold}PRIVATE${alignr}${addr wlp3s0}
PUBLIC${alignr}${exec curl -s www.icanhazip.com}
MAC${alignr}${wireless_ap wlp3s0}
${hr 3}
Down - ${downspeedf usb0} kib/s
${if_existing /proc/net/route wlp3s0}${downspeedgraph wlp3s0 25,160}
Up - ${upspeedf usb0} kib/s
${if_existing /proc/net/route wlp3s0}${upspeedgraph wlp3s0 25,160}]]
        """,
    },
    "weather": {
        "name": "weather",
        "space_from_top": 680 + space_between * 4 + adjustment_from_top,
        "space_from_left": 0,
        "width": 425,
        "height": 120,
        "text": r"""
conky.text = [[
${font Oswald:size=14:bold}Weather  ${hr 3}
${execi 10 /home/ryan/dev/dotfiles/conky/scripts/weather.sh "$(cat /home/ryan/dev/dotfiles/conky/scripts/.weather_api)"}
${execi 10 /home/ryan/dev/dotfiles/conky/scripts/weather-icon.sh $(jq -r '.weather[0].icon' /home/ryan/dev/dotfiles/conky/scripts/weather.json)}\
${image /home/ryan/dev/dotfiles/conky/scripts/weather-icon.png -p 240,-1 -s 175x175}\
${font Oswald:size=12:bold}${execi 100 jq -r '.name' /home/ryan/dev/dotfiles/conky/scripts/weather.json} - ${execi 100 jq '.main.temp | floor' /home/ryan/dev/dotfiles/conky/scripts/weather.json}°C
${execi 100 jq -r '.weather[0].description' /home/ryan/dev/dotfiles/conky/scripts/weather.json | sed 's/.*/\u&/'}${font}
Wind: ${execi 100 jq '.wind.speed' /home/ryan/dev/dotfiles/conky/scripts/weather.json} km/h
Humidity: ${execi 100 jq '.main.humidity' /home/ryan/dev/dotfiles/conky/scripts/weather.json}%
Feels Like: ${execi 100 jq '.main.feels_like | floor' /home/ryan/dev/dotfiles/conky/scripts/weather.json}°C
]];

        """,
    },
}


def set_config(space_from_top, space_from_left, width, height):
    conky_config = {
        "alignment": "'top_left'",
        "font": "'Oswald:size=10:bold'",
        "use_xft": "true",
        "own_window": "true",
        "own_window_type": "'window'",
        "own_window_hints": "'undecorated,below,sticky,skip_taskbar,skip_pager'",
        "own_window_argb_visual": "true",
        "double_buffer": "true",
        "draw_shades": "no",
        "no_buffers": "true",
        "cpu_avg_samples": "1",
        "update_interval": "1.0",
        "uppercase": "true",
        "maximum_width": width,
        "minimum_width": width,
        "maximum_height": height,
        "minimum_height": height,
        "border_inner_margin": global_inner_margin,
        "own_window_argb_value": opacity,
        "own_window_colour": bg_color,
        "default_color": fg_color,
        "gap_x": space_from_left + base_left_margin,
        "gap_y": space_from_top,
    }
    config = """conky.config = {"""
    for i, j in conky_config.items():
        config += f"""
    {i} = {j},"""

    config += """
}
    """
    return config


def set_widget(widget):
    file = (
        set_config(
            widget["space_from_top"],
            widget["space_from_left"],
            widget["width"],
            widget["height"],
        )
        + widget["text"]
    )
    with open(f"/home/ryan/dev/dotfiles/conky/widgets/{widget['name']}.conf", "w") as f:
        f.write(file)


set_widget(widgets["clock"])
set_widget(widgets["system"])
set_widget(widgets["battery"])
set_widget(widgets["memory"])
set_widget(widgets["processes"])
set_widget(widgets["filesystem"])
set_widget(widgets["network"])
set_widget(
    widgets["weather"]
)  # create your own weather api and add to the weather.sh file

# after this run the launch_conkys.sh file in order for the widgets to run
