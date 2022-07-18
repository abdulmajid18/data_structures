from binarytree import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: BinaryTreeNode = None) -> None:
        self.root = root

    """The Recursive pprocess depends on a base case to Recurse
    : The base case is ---> if the root gets to None terminate
        NB every point is consisdred as a root node"""

    def preOrder_DLR(self, root: BinaryTreeNode):
        if root is None:
            return
        print(root.data, sep="-->", end="-->")
        self.preOrder_DLR(root.left)
        self.preOrder_DLR(root.right)

    def preOrder_DRL(self, root: BinaryTreeNode):
        if root is None:
            return
        print(root.data, sep="-->", end="-->")
        self.preOrder_DRL(root.right)
        self.preOrder_DRL(root.left)
    """ Making a Non-Recursive call itt implies using a loop
    With a condition"""

    def preOrderIterattive(self, root: BinaryTreeNode, result: list):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(result)
    def preOrder(self):
        path, result = [self.head], []
        while path:
            curr = path.pop()
            if curr:
                result.append(curr.data)
                path += [curr.right, curr.left]
        return result


    def inOrderLDR(self, root: BinaryTreeNode):
        if root is None:
            return
        self.inOrderLDR(root.left)
        print(root.data, sep="-->", end="-->")
        self.inOrderLDR(root.right)

    def inOrderRDL(self, root: BinaryTreeNode):
        if root is None:
            return
        self.inOrderRDL(root.right)
        print(root.data, sep="-->", end="-->")
        self.inOrderRDL(root.left)

    def inOrderIterative(self, root: BinaryTreeNode, result: list):
        if not root:
            return
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        print(result)

    def postOrderLRD(self, root):
        if root == None:
            return
        self.postOrderLRD(root.left)
        self.postOrderLRD(root.right)
        print(root.data, sep="-->", end="-->")

    def postOrderRLD(self, root):
        if root == None:
            return
        self.postOrderRLD(root.right)
        self.postOrderRLD(root.left)
        print(root.data, sep="-->", end="-->")


x1 = BinaryTreeNode(1)
x2 = BinaryTreeNode(2)
x3 = BinaryTreeNode(3)
x4 = BinaryTreeNode(4)
x5 = BinaryTreeNode(5)
x6 = BinaryTreeNode(6)
x7 = BinaryTreeNode(7)
x1.left = x2
x1.right = x3
x2.left = x4
x2.right = x5
x3.left = x6
x3.right = x7

tree = BinaryTree(x1)
# tree.preOrder_DLR(x1)
# print("\n")
# tree.preOrder_DRL(x1)
# print("\n")
print(x1)
tree.preOrderIterattive(x1, [])
# tree.inOrderLDR(x1)
# print("\n")
# tree.inOrderRDL(x1)
# tree.inOrderIterative(x1, [])
