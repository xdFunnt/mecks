class Element:
    def __init__(self, tag, parent):
        self.tag = tag
        self.children = []
        self.parent = parent
        child.parent = self # Sets the childs parent to the current node
