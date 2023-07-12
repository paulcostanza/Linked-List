class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getVal(self):
        return self.val
    
    def setVal(self, val):
        self.val = val

    def setNext(self, val):
        self.next = val

    def getNext(self):
        return self.next
    
class LinkedList:
    def __init__(self, val=None):
        self.val = Node(val)
        self.head = val

    def addToEnd(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = newNode

    def addToFront(self, val):
        newNode = Node(val)

        if self.head:
            tempNode = self.head
            self.head = newNode
            self.head.next = tempNode
        else:
            self.head = newNode

    def addAfter(self, index, val):
        newNode = Node(val)

        if self.head and index > -1:
            current = self.head
            count = 0

            while current.next and count < index:
                current = current.next
                count += 1

            if count == index and current.next:
                temp = current.next
                current.next = newNode
                newNode.next = temp
            else:
                current.next = newNode
        elif index < 0:
            print('Sorry, no negatives...')

    def addBefore(self, index, val):
        newNode = Node(val)

        if self.head:
            if index <= 0:
                temp = self.head
                self.head = newNode
                newNode.next = temp
            else:
                count = 0
                current = self.head

                while current.next and count < index - 1:
                    current = current.next
                    count += 1

                if count == index - 1 and current.next != None:
                    temp = current.next
                    current.next = newNode
                    newNode.next = temp

                else:
                    print('Sorry, can\'t add before an index that does not exist..')
    
    def printList(self):
        if self.head == None:
            print("There is no list to print...")
        else:
            current = self.head

            while current:
                print('[{}]'.format(current.val), end='')
                
                if current.next:
                    print('=>', end='')

                current = current.next
            
            print()



    def deleteHead(self):
        if self.head:
            self.head = self.head.next
        else:
            print('No head to delete!')

    def deleteTail(self):
        if self.head:
            if self.head.next:
                prev = self.head
                current = self.head.next

                if current.next == None:
                    prev.next = None
                else:

                    while current.next:
                        current = current.next
                        prev = prev.next

                    prev.next = None
            else:
                self.head = None

        else:
            print('No tail to delete...')

    def findLength(self):
        if self.head:
            count = 0
            current = self.head

            while current:
                current = current.next
                count += 1

            return count
        return 0

    def deleteIndex(self, index):      

        if index < self.findLength():
            current = self.head

            if index == 0:
                self.head = self.head.next
            else:

                count = 0

                # index - 1 = node before the index we are deleting
                while current.next and count < index - 1:
                    current = current.next
                    count += 1

                current.next = current.next.next

        else:
            print('Index is outside the list...')

    def findValue(self, val):
        if self.head:
            current = self.head

            while current:
                if current.val == val:
                    return True
                current = current.next

        return False
    
    def findIndex(self, index):
        if index < self.findLength():
            current = self.head
            count = 0

            while current and count < index:
                current = current.next
                count += 1

            return current.val
        
    def updateValue(self, index, newVal):

        if index < self.findLength():
            current = self.head
            count = 0

            while current and count < index:
                current = current.next
                count += 1

            current.val = newVal

    def deleteValue(self, val):
        if self.head:
            if self.head.val == val:
                self.deleteHead()
            elif self.head.next:
                prev = self.head
                current = prev.next

                while current:
                    if current.val == val:
                        prev.next = current.next
                        break
                    current = current.next
                    prev = prev.next

                if current == None:
                    print('I am afraid that value is not in the list...')
        else:
            print('Nothing to delete from this list...')


    def middleValue(self):
        if self.head:
            slow = self.head
            fast = self.head

            while fast and slow:
                if fast.next:
                    fast = fast.next.next
                    if fast:
                        slow = slow.next
                else: 
                    fast = fast.next

            return slow.val
        else:
            print('No values!')
                

                
            






# empty list
listOne = LinkedList()

# full list
listTwo = LinkedList()

# one item
listThree = LinkedList()

# adding to list
listTwo.addToEnd(5)
listTwo.addToEnd(342)
listTwo.addToEnd(17)
listTwo.addToFront(9)
listTwo.addAfter(1, 54)
listTwo.addAfter(0, 90)
listTwo.addAfter(5, 23)
listTwo.addAfter(176, 2)
listTwo.addBefore(1, 89)
listTwo.addBefore(0, 2345)
listThree.addToFront(69)

# delete from list
listTwo.deleteHead()
listTwo.deleteTail()
listTwo.deleteIndex(2)
listTwo.deleteIndex(6)
listTwo.deleteIndex(0)
listTwo.deleteIndex(1)


listTwo.updateValue(0,2)
listTwo.updateValue(1, 22)
listTwo.updateValue(2, 222)
listTwo.updateValue(3, 2222)
listTwo.updateValue(4, 22222)
listTwo.addToEnd(22222)
listTwo.addToEnd(222222)

listTwo.deleteValue(2222222)
# listTwo.deleteTail()


# prints our list
print()
print(' * * * * * * * *')
listOne.printList()
listTwo.printList()
print(listTwo.middleValue())
listThree.printList()
print(' * * * * * * * *')
print()