class CatTreeNode:
    def __init__(self, cat_name, left_child=None, right_child=None):
        self.cat_name = cat_name
        self.left_child = left_child
        self.right_child = right_child

bella = CatTreeNode("Bella")
clyde = CatTreeNode("Clyde", left_child=bella)
mittens = CatTreeNode("Mittens")
rosie = CatTreeNode("Rosie", clyde, mittens)
gizmo = CatTreeNode("Gizmo")
nugget = CatTreeNode("Nugget")
blu = CatTreeNode(cat_name="Blu", left_child=gizmo, right_child=nugget)
tiptoe = CatTreeNode(cat_name="Tiptoe", right_child=blu)
daisy = CatTreeNode("Daisy", tiptoe, rosie)

# daisy is a root.

# We have a binary tree with nodes containing cats’ names.
# Each node has a text field with the name and references to the “left” and “right” descendants.
# The task is to write a piece of code that traverses all the nodes of the tree and displays all names.

def cat_lookup(cat):
    print(cat.cat_name)
    if cat.left_child:
        cat_lookup(cat.left_child)
    if cat.right_child:
        cat_lookup(cat.right_child)

cat_lookup(daisy)