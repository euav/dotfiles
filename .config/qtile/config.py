import copy

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

alt = "mod1"
control = "control"
shift = "shift"
super = "mod4"


terminal = guess_terminal()

keys = [
    Key([], "Caps_Lock", lazy.widget["keyboardlayout"].next_keyboard(), swallow=True),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([super], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([super], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([super], "j", lazy.layout.down(), desc="Move focus down"),
    Key([super], "k", lazy.layout.up(), desc="Move focus up"),
    Key([super], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([super, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([super, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right",),
    Key([super, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([super, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([super, control], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([super, control], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([super, control], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([super, control], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([super], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([super], "m", lazy.window.toggle_maximize(), desc="Maximize window"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([super, shift], "Return", lazy.layout.toggle_split()),
    Key([super], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([super], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([super], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([super], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([super, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([super, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([super], "r", lazy.spawn("rofi -show run"), desc="rofi"),
    Key([super, alt], "4", lazy.spawn("rofi-screenshot")),
]
# https://github.com/qtile/qtile/discussions/2453
russian_mapping = {
    "h": "Cyrillic_er",
    "j": "Cyrillic_o",
    "k": "Cyrillic_el",
    "l": "Cyrillic_de",
    "r": "Cyrillic_ka",
    "q": "Cyrillic_shorti",
    "w": "Cyrillic_tse",
    "f": "Cyrillic_a",
}

def translate(key):
    new_key = copy.copy(key)
    new_key.key = russian_mapping[key.key]
    return new_key 

keys += [translate(key) for key in keys if key.key in russian_mapping]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # super1 + letter of group = switch to group
            Key(
                [super],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # super1 + shift + letter of group = switch to & move focused window to group
            Key(
                [super, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # super1 + shift + letter of group = move focused window to group
            # Key([super, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
layout_common = {
    "border_focus": "#31748f",
    "border_normal": "#191724",
}
layouts = [
    layout.MonadTall(ratio=0.6, margin=5, **layout_common),
    layout.MonadWide(ratio=0.6, margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Iosevka Term",
    fontsize=16,
    padding=5,
    foreground="e0def4",
    background="191724",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Pictures/wallpaper.jpg",
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format="%H:%M %a %d.%m.%Y"),
                widget.Bluetooth(),
                widget.KeyboardLayout(configured_keyboards=["us", "ru"]),
                widget.PulseVolume(),
                widget.QuickExit(),
            ],
            size=30,
            margin=5,
            # border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["aaaaaa", "888888", "444444", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [super],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([super], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
