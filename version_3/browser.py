import tkinter
import tkinter.font
from layout import Layout
from htmlparser import HTMLParser


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
        # what the hell does e do 
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
        nodes = HTMLParser(body).parse()
        # print_tree(nodes)
        self.display_list = Layout(nodes).display_list
        self.draw()

def print_tree(node, indent=0):
    '''
    Debug: Prints the html Document Object Model tree
    '''
    print(" " * indent, node)
    for child in node.children:
        print_tree(child, indent + 2)