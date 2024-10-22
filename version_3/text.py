class Text:
    def __init__(self, text, parent):
        self.text = text
        self.children = []
        self.parent = parent
        if parent:
            parent.children.append(self)  # Sets the childs parent to the current node

    def __repr__(self):
        return repr(self.text)