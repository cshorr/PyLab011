import os
class MindMapComposite:

    def __init__(self):
        self.name = name
        self.shape =shape
        self.children=[]


    def remove(self, child):
        self.children.remove(child)
    def add(self, child):
        self.childrem.append(child)


    def display(self, indent=0):
        if indent == 0:
            print("mindmap" + os.linesep+ 'root', 'end')
        print(" " * indent + str(self))
        indent += 2
        for child in self.children:
            child.display(indent + 2)

    def__str__(self)
    return self.get_shape_representation().format(self.name)
