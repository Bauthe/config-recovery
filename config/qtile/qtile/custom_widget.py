from libqtile import widget

class GroupBox(widget.GroupBox):

    def __init__(self, permanent_groups=None, **config):

        widget.GroupBox.__init__(self, **config)
        self.permanent_groups = permanent_groups

    @property
    def groups(self):
        """
        returns list of visible groups.
        The existing groups are filtered by the visible_groups attribute and
        their label. Groups with an empty string as label are never contained.
        Groups that are not named in visible_groups are not returned.
        """
        if self.visible_groups:
            return [g for g in self.qtile.groups
                    if (g.label and (g.windows or g.screen) and
                    g.name in self.visible_groups)
                    or g.name in self.permanent_groups]
        else:
            return [g for g in self.qtile.groups if (g.label and
                    (g.windows or g.screen))
                    or g.name in self.permanent_groups]


class Clock(widget.Clock):
    
    defaults = [
        ('time_format', '<span size="larger">%H:%M</span>', 'A python time format string'),
        ('date_format', '%d-%m-%Y', 'A python date format string'),
    ]

    def __init__(self, **config):

        widget.Clock.__init__(self, **config)
        self.add_defaults(Clock.defaults)
        self.format = self.time_format
        self.mouse_callbacks.update({
            'Button1': self.toggle_day,
        })

    def toggle_day(self):

        if self.format == self.time_format:
            self.format = self.date_format
        else:
            self.format = self.time_format
        self.tick()

    def draw(self):
        # if the bar hasn't placed us yet
        if self.offsetx is None:
            return
        self.drawer.clear(self.background or self.bar.background)
        self.layout.draw(
            self.actual_padding or 0,
            int(self.bar.height / 2.0 - self.layout.height / 2.0) + 1
        )
        self.drawer.draw(offsetx=self.offsetx, width=self.width)
