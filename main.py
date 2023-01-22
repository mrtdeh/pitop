import urwid as u
import actions as ac


class SelectedPipeWidget(u.WidgetWrap):
    def __init__(self):
        self.file = open("./pipelines.yml", "r+")  
        self.pipe = None
        self.text_widget = u.Text(u'')
        super(SelectedPipeWidget, self).__init__(self.text_widget)

    def get_pipe(self,pipe_name):
        self.pipe = pipe_name
        self.update()

    def enable(self,pipe_name):
        ac.uncommentPipe(self.file,pipe_name)
    
    def disable(self,pipe_name):
        ac.commentPipe(self.file,pipe_name)

    def update(self):
        """Update UI
        """
        if self.pipe is None:
            self.text_widget.set_text('No Pipe selected')
        else:
            self.text_widget.set_text('Selected pipe is : %s' % self.pipe)

class App(object):

    def handle_key(self, key):
        # if key in ('a',):
        #     x = u.AttrMap(u.Button("x"), "normal", "highlighted")
        #     self.walker.append(x)
        if key in ('q',):
            raise u.ExitMainLoop()
    
    def selectPipe(self,a,stat,pipe):
        if stat == True:
            self.selected_pipe_widget.enable(pipe["id"])
        else:
            self.selected_pipe_widget.disable(pipe["id"])

    def __init__(self):
        self.selected_pipe_widget = SelectedPipeWidget()
        contents = []
        l = "abcde"
        l = ac.loadPipelines()
        for x in l:
            chk = u.CheckBox(x["id"],state=x["enabled"])
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