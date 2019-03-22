#NULLPOINTER should be set to -1 if using array elemnt with index 0
NULLPOINTER = - 1

#DECLARE Listnode as a record type to store data and pointer
class ListNode:
    def __init__(self):
        self.data = ""
        self.pointer = NULLPOINTER

def initialiselist():
    List = [ListNode() for i in range(8)]
    StartPointer = NULLPOINTER
    FreeListPtr = 0
    for i in range(7):
        List[i].pointer = i + 1
    List(7).pointer = NULLPOINTER
    return (List, StartPointer,FreeListPtr)

