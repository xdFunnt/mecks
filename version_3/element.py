class Element:
    def __init__(self, tag, attributes, parent):
        self.tag = tag
        self.children = []
        self.parent = parent
        if parent:
            parent.children.append(self) # Sets the childs parent to the current node
        self.attributes = attributes

    def __repr__(self):
        return "<" + self.tag + ">"