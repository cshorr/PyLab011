import os

class MindMapComposite:
    # Step 1: Write the __init__ method
    # - Define an __init__ method that takes name and shape as parameters.
    # - Initialize self.name, self.shape, and an empty list self.children.
    ```

**Hint**: Use `self.children = []` to initialize the list.

# Step 2: Write the add and remove methods
# - Use append() to add and remove() to delete from the children list.

# Step 3: Write the __str__ method
# - Format the name using get_shape_representation() and return it.

# Step 4: Write the display method
# - Print the name with the specified indentation.
# - Loop over each child and call display with increased indentation.

# Step 5: Write the get_shape_representation method
# - Create a dictionary with shape templates.
# - Use shapes.get to return the template.