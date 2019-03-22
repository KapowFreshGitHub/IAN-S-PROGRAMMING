class bNode:
    # private leftpointer : INTEGER
    # private rightpointer: INTEGER
    # private data : STRING

    def __init__(self):
        self.leftpointer = 0
        self.rightpointer = 0
        self.data = ''

    def setData(self, value):
        self.data = value

    def getData(self):
        return self.data

    def setleftpointer(self, value):
        self.leftpointer = value

    def getleftpointer(self):
        return self.leftpointer

    def setrightpointer(self, value):
        self.rightpointer = value

    def getrightpointer(self):
        return self.rightpointer


rootPointer = 0
freePointer = 7

bTree = [bNode(), bNode(), bNode(), bNode(), bNode(), bNode(), bNode(), bNode()]  # 8 nodes in the binary tree
bTree[0].setData('Celtic')
bTree[0].setleftpointer(3)
bTree[0].setrightpointer(1)

bTree[1].setData('Rangers')
bTree[1].setleftpointer(2)
bTree[1].setrightpointer(5)

bTree[2].setData('Kilmarnock')
bTree[2].setleftpointer(4)
bTree[2].setrightpointer(0)

bTree[3].setData('Aberdeen')
bTree[3].setleftpointer(0)
bTree[3].setrightpointer(0)

bTree[4].setData('Hearts')
bTree[4].setleftpointer(0)
bTree[4].setrightpointer(6)

bTree[5].setData('St Johnstone')
bTree[5].setleftpointer(0)
bTree[5].setrightpointer(0)

bTree[6].setData('Hibernian')
bTree[6].setleftpointer(0)
bTree[6].setrightpointer(0)


# in order traversal SHOULD output
# Aberdeen, Celtic, Hearts, Hibernian, Kilmarnock, Motherwell, Rangers, St Johnstone

def traverse(id):
    # get the node using id
    thisNode = bTree[id]

    # if the leftpointer > 0
    if thisNode.getleftpointer() > 0:
        # call traverse with the new node id (leftpointer)
        traverse(thisNode.getleftpointer())

    # output node data item
    print(thisNode.getData())

    # if the rightpointer > 0
    if thisNode.getrightpointer() > 0:
        # call traverse with the new node id (rightpointer)
        traverse(thisNode.getrightpointer())


foundLocation = 0


def searchNode(dataTarget, id):
    global foundLocation
    # get the node using id
    thisNode = bTree[id]
    if thisNode.getData() == dataTarget:
        print('Item ', dataTarget, ' found at id ', id)
        foundLocation = id
    else:
        # if the leftpointer > 0
        if thisNode.getleftpointer() > 0:
            # call traverse with the new node id (leftpointer)
            value = searchNode(dataTarget, thisNode.getleftpointer())

        # output node data item
        # print(thisNode.getData())

        # if the rightpointer > 0
        if thisNode.getrightpointer() > 0:
            # call traverse with the new node id (rightpointer)
            value = searchNode(dataTarget, thisNode.getrightpointer())
    return foundLocation


thisID = searchNode('Liverpool', rootPointer)
if thisID == 0:
    print('No match found')


def insertNode(newNode, parentID):
    bTree[freePointer] = newNode

    # Rangers node is no 1, left pointer links to Kilmarnock is no 2
    # We want to add 'Queens Park' between these two

    # We get Rangers node and take left pointer id - save it as temp
    tempNode = bTree[parentID]
    tempID = tempNode.getleftpointer()
    # We change Rangers left pointer id to freePointer
    tempNode.setleftpointer(freePointer)

    # We add temp left pointer id as the left pointer id of newNode
    newNode.setleftpointer(tempID)


newNode = bNode()
newNode.setData('Queens Park')
thisID = searchNode('Rangers', rootPointer)
print(thisID)
insertNode(newNode, thisID)
traverse(rootPointer)

