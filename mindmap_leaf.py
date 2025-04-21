


class MindMapLeaf:
    # Step 1: Write the __init__ method
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

# Step 2: Write the __str__ method
    def __str__(self):
        shape_template = self.get_shape_representation()
        return shape_template.format(self.name)

# Step 3: Write the display method
    def display(self, indent=0):
        print(" " * indent + str(self))

# Step 4: Write the get_shape_representation method
    def get_shape_representation(self):
        shapes = {
        "circle": "(({}))",
        "oval": "({})",
        "square": "[{}]",
        "cloud": "){}(",
        "hexagon": "{{{{{}}}}}",
        "bang": ")){}((",
        "plain": "{}"
    }
        return shapes.get(self.shape, "{}")
