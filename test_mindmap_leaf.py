from mindmap_leaf import MindMapLeaf
from mindmap_composite import Mindmap_composite

root =
branch =
leaf1
leaf2
leaf = MindMapLeaf("Jean-Luc Picard", "circle")
print(str(leaf))  # Should display "((Jean-Luc Picard))"
leaf.display(2)   # Should display "  ((Jean-Luc Picard))" with two spaces

print("MindMapLeaf tests completed!")

