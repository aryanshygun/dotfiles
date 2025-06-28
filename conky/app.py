opacity = 256
bg_color = "'#1C1C1E'"
fg_color = "'#FFFFFF'"
global_inner_margin = "8"
# space_between = 10
space_between = 5
interval = space_between
margin_left = 10 + 5
# y_adjustment = -13
y_adjustment = -8

widgets = {
    "clock": {
        "name": "clock",
        "height": 65 + y_adjustment,
        "text": """
conky.text = [[
TIME  ${hr 2}
${font Roboto:pixelsize=50}${alignr}${time %H:%M}${font}
${font Open Sans:pixelsize=11}${alignr}${time %Y-%m-%d}${font}
]];
        """,
    },
    "system": {
        "name": "system",
        "height": 192 + y_adjustment,
        "text": """
conky.text = [[
system  ${hr 2}
${font Oswald:size=8}Distro ${alignr}${exec lsb_release -ds}
Uptime: $alignr$uptime
]]
        """,
    },
    "battery": {
        "name": "battery",
        "height": 266 + y_adjustment,
        "text": """
conky.text = [[
BATTERIES  ${hr 2}
${font Oswald:size=8}Battery A: ${alignr}${if_existing /sys/class/power_supply/BAT0/status Charging}Charging${else}${if_existing /sys/class/power_supply/BAT0/status Discharging}Discharging${else}${if_existing /sys/class/power_supply/BAT0/status Not charging}Full${endif}${endif}${endif} ${battery_percent BAT0}%
${battery_bar 5 BAT0}
Battery B: ${alignr}${if_existing /sys/class/power_supply/BAT1/status Charging}Charging${else}${if_existing /sys/class/power_supply/BAT1/status Discharging}Discharging${else}${if_existing /sys/class/power_supply/BAT1/status Not charging}Full${endif}${endif}${endif} ${battery_percent BAT1}%
${battery_bar 5 BAT1}
]]
        """,
    },
    "memory": {
        "name": "memory",
        "height": 372 + y_adjustment,
        "text": """
        conky.text = [[
MEMORY  ${hr 2}
${font Oswald:size=8}${mem}/${memmax}${alignr}${memperc}%
${membar 5}

Name: ${alignr}MEM
${top_mem name 1}${alignr}${top_mem mem 1}gib
${top_mem name 2}${alignr}${top_mem mem 2}gib
${top_mem name 3}${alignr}${top_mem mem 3}gib
]]
        """,
    },
    "processes": {
        "name": "processes",
        "height": 526 + y_adjustment,
        "text": """
conky.text = [[
Processes ${hr 2}
${font Oswald:size=8}CPU ${alignr}$cpu%
${cpugraph cpu0 25,225}
Freq ${alignr}$freq_g Ghz
CPU Temp: ${alignr}${exec sensors | grep 'Package' | awk -F'+' '{print $2}' | awk -F'.' '{print $1}'}°C
Core 1: ${cpu cpu1}% ${alignr}${cpubar cpu1 6,140}
Core 2: ${cpu cpu3}% ${alignr}${cpubar cpu3 6,140}
Core 3: ${cpu cpu5}% ${alignr}${cpubar cpu5 6,140}
Core 4: ${cpu cpu7}% ${alignr}${cpubar cpu7 6,140}

Name: ${alignr} PID   CPU   MEM
${top name 1} $alignr ${top pid 1}  ${top cpu 1}  ${top mem 1}
${top name 2} $alignr ${top pid 2}  ${top cpu 2}  ${top mem 2}
${top name 3} $alignr ${top pid 3}  ${top cpu 3}  ${top mem 3}
${top name 4} $alignr ${top pid 4}  ${top cpu 4}  ${top mem 4}
${top name 5} $alignr ${top pid 5}  ${top cpu 5}  ${top mem 5}
]]
        """,
    },
    "filesystem": {
        "name": "filesystem",
        "height": 833 + y_adjustment,
        "text": """
conky.text = [[
Capacity  ${hr 2}
${font Oswald:size=8}Root${alignr}${fs_used /}/${fs_size /}
${fs_bar 5 /}
]]        
        """,
    },
    "network": {
        "name": "network",
        "height": 907 + y_adjustment,
        "text": """
conky.text = [[
Network  ${hr 2}
${alignc}${font Oswald:size=8}${if_up usb0}USB${else}${if_existing /proc/net/route wlp3s0}${wireless_essid wlp3s0}${else}Not Connected${endif}${endif}
${if_existing /proc/net/route wlp3s0}${upspeedgraph wlp3s0 25,105}${alignr}${downspeedgraph wlp3s0 25,105}
UP ${upspeedf usb0} kib/s${alignr}Down ${downspeedf usb0} kib/s${endif}
]]
        """,
    },
}


def set_config(height):
    conky_config = {
        "alignment": "'top_left'",
        "font": "'Oswald:size=10:bold'",
        "use_xft": "true",
        "own_window": "true",
        "own_window_type": "'window'",
        "own_window_hints": "'undecorated,below,sticky,skip_taskbar,skip_pager'",
        "own_window_argb_visual": "true",
        "double_buffer": "true",
        "minimum_width": "225",
        "draw_shades": "no",
        "no_buffers": "true",
        "cpu_avg_samples": "1",
        "uppercase": "true",
        "border_inner_margin": global_inner_margin,
        "own_window_argb_value": opacity,
        "own_window_colour": bg_color,
        "default_color": fg_color,
        "gap_x": margin_left,
        "gap_y": height,
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
    global space_between
    file = set_config(widget["height"] + space_between) + widget["text"]
    with open(f"/home/ryan/dev/dotfiles/conky/widgets/{widget['name']}.conf", "w") as f:
        f.write(file)
    space_between += interval


set_widget(widgets["clock"])
set_widget(widgets["system"])
set_widget(widgets["battery"])
set_widget(widgets["memory"])
set_widget(widgets["processes"])
set_widget(widgets["filesystem"])
set_widget(widgets["network"])
