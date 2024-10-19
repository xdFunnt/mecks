import tkinter
import tkinter.font
from layout import Layout
# from htmlparser import HTMLParser
from text import Text
from tag import Tag

HSTEP, VSTEP = 13, 18
WIDTH, HEIGHT = 800, 600
SCROLL_STEP = 100

class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
            self.window,
            width=WIDTH,
            height=HEIGHT,
        )
        self.canvas.pack()
        self.url = None

        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)

    def scrolldown(self, e):
         self.scroll += SCROLL_STEP
         self.draw()
    
    def draw(self):
        '''
        Draws display_list to window
        '''
        self.canvas.delete("all")
        for x, y, c, font in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=c, anchor="nw", font=font)

    def load(self, url):
        '''
        Gets the webpage contents and draws to window
        '''
        self.url = url
        body = self.url.request()
        tokens = lex(body)
        self.display_list = Layout(tokens).display_list
        self.draw()

def lex(body):
    '''
    Removes tags from contents of webpage
    '''
    out = []
    buffer = ""
    in_tag = False

    for c in body:
        if c == "<":
            in_tag = True
            if buffer == "i":
                print(buffer)
            if buffer: out.append(Text(buffer))
            buffer = ""
        elif c == ">":
            in_tag = False
            out.append(Tag(buffer))
            buffer = ""
        else:
            buffer += c
    if not in_tag and buffer:
            out.append(Text(buffer))
    return out
