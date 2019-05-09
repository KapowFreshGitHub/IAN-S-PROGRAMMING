
class node:
    def _init_ (self):
        self.__data = none
        self.__lp = none
        self.__rp = none

    def setData(self,data):
        self.__data = data

    def getData(self):
        return self.__data

    def setlp(self, leftpointer):
        self.__leftpointer = leftpointer

    def getlp(self):
        return self.__leftpointer

    def setrp(self,Rightpointer):
        self.__RightPointer = Rightpointer

    def getrp(self):
        return self.__RightPointer

WirelessBTS =[node,node,node,node,node,node,node,node,node,node,node]

WirelessBTS[0].setData("Drake")
WirelessBTS[0].setRP(1)
WirelessBTS[0].setlp(3)

WirelessBTS[1].setData("Nicki")
WirelessBTS[1].setRP(2)
WirelessBTS[1].setlp(6)

WirelessBTS[1].setData("PND")
WirelessBTS[1].setRP(9)
WirelessBTS[1].setlp(-1)

WirelessBTS[2].setData("Chris")
WirelessBTS[2].setRP(-1)
WirelessBTS[2].setlp(5)

WirelessBTS[3].setData("Tory")
WirelessBTS[3].setRP(-1)
WirelessBTS[3].setlp(9)

WirelessBTS[4].setData("August")
WirelessBTS[4].setRP(7)
WirelessBTS[4].setlp(-1)

WirelessBTS[5].setData("Lil")
WirelessBTS[5].setRP(-1)
WirelessBTS[5].setlp(8)

WirelessBTS[6].setData("BabyFace")
WirelessBTS[6].setRP(-1)
WirelessBTS[6].setlp(-1)

WirelessBTS[7].setData("Jon")
WirelessBTS[7].setRP(-1)
WirelessBTS[7].setlp(-1)

WirelessBTS[8].setData("Skepta")
WirelessBTS[8].setRP(-1)
WirelessBTS[8].setlp(-1)

Freepointer = 9
Rootpointer = 0
#NewItem = "Travis"
def insertNewItem(self,NewItem):
    if FreePointer != --1:
    #Then there is space in the list
    #slot data into free pointer spot
        NewNode= Freepointer
        WirelessBTS[NewNode].setData(NewItem)
        WirelessBTS[NewNode].setlp(-1)
        WirelessBTS[NewNode].setrp(-1)
    #CHECK IF THERE IS IN ANY NODES IN LIST
    if RootPointer == -1:
        #Insert new item at start of the binary tree
        WirelessBTS[Rootpointer].setData(NewItem)
    else:
        #find insertion point
        ThisPtr = Rootpointer
        PreviousPtr = ThisPtr

    while ThisPtr != -1:#while not a leaf node # not null pointer
      ThisPtrData = WirelessBTS[ThisPtr].getData()
      if ThisPtrData > NewItem:
          Turnleft = True
          ThisPtr = WirelessBTS[ThisPtr].getlp()
      else:
          TurnLeft = False
          ThisPtr = WirelessBTS[ThisPtr].getrp()
        #end if
    #end while

    if TurnLeft == True:
        WirelessBTS[PreviousPtr].setlp(NewNode)
    else:
        WirelessBTS[PreviousPtr].setrp(NewNode)


insertNewItem("Travis")
print(WirelessBTS[NewNode].getlp())
print(WirelessBTS[NewNode].getrp())