class BSTNode:
    def __init__(self, data) -> None:
        self.data = data  # root node
        self.left = None  # left  child node
        self.right = None  # right child node

    # set data
    def setData(self, data):
        self.data = data
    # get data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRighht(self):
        return self.right
