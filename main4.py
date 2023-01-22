

from __future__ import print_function, absolute_import, division
import urwid
from random import randint


class RandomNumberWidget(urwid.WidgetWrap):
    def __init__(self):
        self.random_number = None
        self.text_widget = urwid.Text(u'')
        super(RandomNumberWidget, self).__init__(self.text_widget)

    def roll(self):
        self.random_number = randint(0, 100)
        self.update()

    def update(self):
        """Update UI
        """
        if self.random_number is None:
            self.text_widget.set_text('No number set')
        else:
            self.text_widget.set_text('Random number: %s' % self.random_number)


class App(object):
    def __init__(self):
        self.random_number_widget = RandomNumberWidget()
        top_message = 'Press any key to get a random number, or q to quit\n\n\n'
        widget = urwid.Pile([
            urwid.Padding(urwid.Text(top_message),
                          'center', width=('relative', len(top_message))),
            self.random_number_widget,
        ])
        self.widget = urwid.Filler(widget, 'top')

    def play(self):
        self.random_number_widget.roll()

    def play_or_exit(self, key):
        if key in ('q', 'Q', 'esc'):
            raise urwid.ExitMainLoop()
        app.play()


if __name__ == '__main__':
    app = App()
    loop = urwid.MainLoop(app.widget, unhandled_input=app.play_or_exit)
    loop.run()