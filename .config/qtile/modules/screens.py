from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
            wallpaper = "~/.config/qtile/bg.jpg",
            wallpaper-mode = "stretch",
        top=bar.Bar(
            [
                widget.Sep(
                    padding=3, 
                    linewidth=0, 
                    background="#2f343f"),
                widget.Image(
                    filename='~/.config/qtile/menu.png', 
                    margin=3, 
                    background="#2f343f", 
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(
                    padding=4, 
                    linewidth=0, 
                    background="#2f343f"), 
                widget.GroupBox(
                    highlight_method='line',
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f"),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground='#2f343f'),    
                widget.Prompt(),
                widget.Spacer(
                    length=5),
                widget.WindowName(
                    foreground='#99c0de',
                    fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(
                    scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Fedora",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e dnf upgrade -y')
                    },
                    background="#2f343f"),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground='#2f343f'),
                widget.Clock(
                    format=' %m/%d/%Y %a %H:%M',
                    background="#2f343f",
                    foreground='#9bd689'),
                widget.TextBox(                               
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground='#2f343f',),
                widget.TextBox(
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground='#2f343f'),
                widget.Systray(
                    icon_size = 20),
                widget.Battery(
                        charge_char = "+",
                        full_char = "=",
                        discharge_char = "-",
                        format = "{char} {percent:2.0%} {hour:d} {min:02d}",
                        energy_now_file = "charge_now",
                        energy_full_file = "charge_full",
                        power_now_file = "current_now",
                        update_interval = 5,
                        battery_name = "BAT0",
                        ),
                widget.TextBox(                               
                    text = '',
                    padding = 0,
                    fontsize = 28,
                    foreground='#2f343f',),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                )
            ],
            30,  # height in px
            background="#404552"  # background color
        ),
    ),
]