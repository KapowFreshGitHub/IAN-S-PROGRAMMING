
FreeListPtr = 0
def InsertNode(List, StartPointer, FreeListPtr, NewItem) :
    if FreeListPtr != NULLPOINTER :
    # there is space in the array
    # take node from free list and store data item
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        # find insertion point
    PreviousNodePtr = NULLPOINTER
    ThisNodePtr = StartPointer # start at beginning of list
    while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data < NewItem:
    # while not end of list
        PreviousNodePtr = ThisNodePtr # remember this node
    # follow the pointer to the next node
        ThisNodePtr = List[ThisNodePtr].Pointer

        if PreviousNodePtr == NULLPOINTER:
        # insert new node at start of list
            List[NewNodePtr].Pointer = StartPointer
        StartPointer = NewNodePtr
        else:
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr
            # insert new node between previous node and this node
    else:
        print("no space for more data")
    return (List, StartPointer,FreeListPtr)