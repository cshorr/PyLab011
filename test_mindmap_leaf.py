from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

# Step 1: Create root node
root = MindMapComposite("Root", "circle")

# Step 2: Create a branch
branch = MindMapComposite("Characters", "oval")

# Step 3: Add leaf nodes to the branch
leaf1 = MindMapLeaf("Jean-Luc Picard", "plain")
leaf2 = MindMapLeaf("Data", "plain")
branch.add(leaf1)
branch.add(leaf2)

# Step 4: Attach the branch to the root
root.add(branch)

# Step 5: Display everything (mermaid-compatible)
print("mindmap")
root.display()
