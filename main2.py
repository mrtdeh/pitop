import urwid as u

class SelectedPipeWidget(u.WidgetWrap):
    def __init__(self):
        self.pipe = None
        self.text_widget = u.Text(u'')
        super(SelectedPipeWidget, self).__init__(self.text_widget)

    def get_pipe(self,pipe_name):
        self.pipe = pipe_name
        self.update()

    def update(self):
        """Update UI
        """
        if self.pipe is None:
            self.text_widget.set_text('No Pipe selected')
        else:
            self.text_widget.set_text('Selected pipe is : %s' % self.pipe)

class App(object):

    def handle_key(self, key):
        global sel
        if key in ('w',):
            sel ="asdasd"
        if key in ('a',):
            x = u.AttrMap(u.Button("x"), "normal", "highlighted")
            self.walker.append(x)
        if key in ('q',):
            raise u.ExitMainLoop()
    
    def selectPipe(self,a,stat,pipe):
        self.selected_pipe_widget.get_pipe(a)

    def __init__(self):
        self.selected_pipe_widget= SelectedPipeWidget()
        contents = []
        l = "abcde"
        for x in l:
            chk = u.CheckBox(x)
            contents.append(u.AttrMap(chk, "normal", "highlighted") )
            u.connect_signal(chk, 'change', self.selectPipe, x)

        self.walker = u.SimpleFocusListWalker(contents)
        
        listbox = u.ListBox(self.walker)
        
        box_adapter = u.BoxAdapter(listbox, height=10)
        
        filler = u.Filler(box_adapter, 'top')
        
        t = u.Text("a to append item, q to exit")
        f = self.selected_pipe_widget
        frame = u.Frame(header=u.AttrMap(t, "header"), body=filler,footer=f)
        
        PALETTE = [("header",      "white", "dark red"),
                   ("normal",      "black", "white"),
                   ("highlighted", "black", "dark cyan")]
        
        loop = u.MainLoop(frame, PALETTE, unhandled_input=self.handle_key)
        
        loop.run()

app = App()