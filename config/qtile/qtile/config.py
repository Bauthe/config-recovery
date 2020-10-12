import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.command_client import InteractiveCommandClient, CommandInterface

from libqtile.lazy import lazy
from typing import List  # noqa: F401

import custom_widget


##############
### GROUPS ###
##############

group_basenames = ['WWW', 'DEV', 'SYS', 'DOC', 'MUS', 'CHAT', '', '', '', '']

group_names = []
groups = []
permanent_groups = []
#·
for i, name in enumerate(group_basenames):
    if name != '':
        group_names.append(f'{i+1}·{name}')
        groups.append(Group(group_names[i]))
        permanent_groups.append(group_names[i])
    else:
        group_names.append(' '+str(i+1)+' ')
        groups.append(Group(group_names[i]))


###################
### KEYBINDINGS ###
###################

mod = 'mod4'
alt = 'mod1'

terminal = 'termite'
dmenu = 'rofi -show drun'
browser = 'firefox'
file_manager = terminal + ' -e ranger'
resource_monitor = terminal + ' -e htop'

keys = [
    # Switch between windows in current stack pane
    Key([mod], 'Down', lazy.layout.down(), desc='Move focus down in stack pane'),
    Key([mod], 'Up', lazy.layout.up(), desc='Move focus up in stack pane'),
    Key([mod], 'Right', lazy.layout.right(), desc='Move focus right in stack pane'),
    Key([mod], 'Left', lazy.layout.left(), desc='Move focus left in stack pane'),

    # Move windows up or down in current stack
    Key([mod, 'shift'], 'Down', lazy.layout.shuffle_down(), desc='Move window down in current stack '),
    Key([mod, 'shift'], 'Up', lazy.layout.shuffle_up(), desc='Move window up in current stack '),
    Key([mod, 'shift'], 'Right', lazy.layout.shuffle_right(), desc='Move window right in current stack '),
    Key([mod, 'shift'], 'Left', lazy.layout.shuffle_left(), desc='Move window left in current stack '),

    # General Qtile controls
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'f', lazy.window.toggle_fullscreen(), desc='Toggle fullscreen for focused window'),
    Key([mod, 'shift'], 'space', lazy.window.toggle_floating(), desc='Toggle floating for focused window'),
    Key([mod, 'shift'], 'q', lazy.window.kill(), desc='Kill focused window'),
    Key([mod, 'shift'], 'r', lazy.restart(), desc='Restart qtile'),
    Key([mod, 'control', 'shift'], 'q', lazy.shutdown(), desc='Shutdown qtile'),

    # Volume
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer sset Master 4%+'), desc='Raise volume'),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer sset Master 4%-'), desc='Lower volume'),
    Key([], 'XF86AudioMute', lazy.spawn('amixer sset Master toggle'), desc='Toggle mute'),

    # Brightness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('smart-backlight up'), desc='Brightness up'),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('smart-backlight down'), desc='Brightness down'),

    # Media controls
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause'), desc='Toggle play/pause'),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next'), desc='Next'),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous'), desc='Previous'),

    # Screenshots
    Key([mod], 'Print', lazy.spawn('gnome-screenshot -wc'), desc='Take window screenshot to clipboard'),
    Key([mod, alt], 'Print', lazy.spawn('gnome-screenshot -w'), desc='Take window screenshot to file'),
    Key([mod, 'shift'], 'Print', lazy.spawn('gnome-screenshot -ac'), desc='Take screenshot of an area to clipboard'),
    Key([mod, alt, 'shift'], 'Print', lazy.spawn('gnome-screenshot -a'), desc='Take screenshot of an area to file'),

    # Basic app launchers
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod], 'd', lazy.spawn(dmenu), desc='Launch dmenu'),
    Key([mod], 'b', lazy.spawn(browser), desc='Launch web browser'),
    Key([mod], 'e', lazy.spawn(file_manager), desc='Launch file manager'),
    Key([mod, 'shift'], 'Escape', lazy.spawn(resource_monitor), desc='Launch resource monitor'),

    # App launchers
    Key([mod, alt], 'b', lazy.spawn('baobab'), desc='Launch baobab'),
    Key([mod, alt], 'c', lazy.spawn('chromium'), desc='Launch chromium'),
    Key([mod], 'c', lazy.spawn('code'), desc='Launch code'),
    Key([mod, alt], 'd', lazy.spawn('discord'), desc='Launch discord'),
    Key([mod, alt], 'e', lazy.spawn('dolphin'), desc='Launch dolphin'),
    Key([mod], 'g', lazy.spawn('gimp'), desc='Launch gimp'),
    Key([mod, alt], 'g', lazy.spawn('godot'), desc='Launch godot'),
    Key([mod, alt], 'l', lazy.spawn('lutris'), desc='Launch lutris'),
    Key([mod], 'm', lazy.spawn('MellowPlayer'), desc='Launch MellowPlayer'),
    Key([mod, alt], 'm', lazy.spawn('minecraft-launcher'), desc='Launch minecraft-launcher'),
    Key([mod], 'o', lazy.spawn('libreoffice'), desc='Launch libreoffice'),
    Key([mod], 'p', lazy.spawn('pavucontrol'), desc='Launch pavucontrol'),
    Key([mod], 's', lazy.spawn('prime-run steam'), desc='Launch steam'),
    Key([mod], 't', lazy.spawn('teams'), desc='Launch teams'),
    Key([mod], 'v', lazy.spawn('vlc'), desc='Launch vlc'),
]

# Group controls
group_keys = ['ampersand', 'eacute', 'quotedbl', 'apostrophe', 'parenleft', 'minus', 'egrave', 'underscore', 'ccedilla', 'agrave']

for name, key in zip(group_names, group_keys):

    keys.extend([
        Key([mod], key, lazy.group[name].toscreen(), desc=f'Switch to group {name}'),
        Key([mod, 'shift'], key, lazy.window.togroup(name, switch_group=True), desc=f'Switch to & move focused window to group {name}'),
    ])


###############
### LAYOUTS ###
###############

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Floating(),
]


###########
### BAR ###
###########

color = dict(
    normal = '#ffffff',
    grey = '#888888',
    primary = '#ff0000',
    background = '#000000',
    warning = '#ffff00',
    test = '#05fc47',
)

widget_defaults = dict(
    font = 'Noto Sans',
    fontsize = 12,
    padding = 3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom = bar.Bar(
            [
                custom_widget.GroupBox(
                    # color scheme
                    active = color['normal'],
                    inactive = color['grey'],
                    foreground = color['normal'],
                    background = color['background'],
                    highlight_color = color['background'],
                    block_highlight_text_color = color['normal'],
                    this_current_screen_border = color['primary'],
                    this_screen_border = color['background'],
                    urgent_border = color['warning'],
                    urgent_text = color['normal'],

                    # methods: 'border', 'text', 'block', or 'line'
                    highlight_method = 'block',
                    urgent_alert_method = 'line',

                    # other settings
                    rounded = True,
                    disable_drag = True,
                    hide_unused = False,
                    permanent_groups = permanent_groups,
                ),

                widget.Prompt(),

                widget.WindowName(),

                widget.CPU(),

                widget.Memory(),

                widget.Battery(),

                widget.Volume(
                    foreground = color['normal'],
                    background = color['primary'],
                    padding = 5,
                    update_interval = 0.05,
                ),

                widget.Chord(
                    chords_colors={
                        'launch': ('#ff0000', '#ffffff'),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Systray(),

                custom_widget.Clock(
                    width = 80,
                ),
            ],
            size = 30,
            opacity = 0.8,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = 'smart'


#############
### HOOKS ###
#############

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'