import tkinter
from url import URL

WIDTH, HEIGHT = 800, 600
HSTEP, VSTEP = 13, 18
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
        for x, y, c in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=c)

    def load(self, url):
        '''
        Gets the webpage contents and draws to window
        '''
        self.url = url
        body = self.url.request()
        text = lex(body)
        self.display_list = layout(text)
        self.draw()
    
    


def lex(body):
        '''
        Removes tags from contents of webpage
        '''
        text = ""
        in_tag = False
        for c in body:
            if c == "<":
                in_tag = True
            elif c == ">":
                in_tag = False
            elif not in_tag:
                text += c
        return text

def layout(text):
        '''
        Organizes the text in the way it should be drawn to the screen
        '''
        display_list = []
        cursor_x, cursor_y = HSTEP, VSTEP
        for c in text:
            display_list.append((cursor_x, cursor_y, c))
            cursor_x += HSTEP
            if cursor_x >= WIDTH - HSTEP:
                 cursor_y += VSTEP
                 cursor_x = HSTEP
        return display_list
                
