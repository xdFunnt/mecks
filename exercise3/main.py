from url import URL
from browser import Browser
import tkinter


if __name__ == "__main__":
    import sys
    Browser().load(URL(sys.argv[1]))
    tkinter.mainloop()



'''# Debug mode
url = URL("https://browser.engineering/examples/example1-simple.html")
print(url)'''
