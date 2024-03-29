#1
#Traversing a linked list and performing enqueue&deqeue operation
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBeginning(self,newdata):  #deqeue
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode
    def AtEnd(self,newdata):        #enqueue
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=NewNode
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtBeginning("Sun")
list.AtEnd("Thurs")
list.listprint()



#2
#inserting elements in linked list randomly at different position.
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None

    def listprint(self):
        printval=self.head
        while(printval is not None):
            print(printval.data)
            printval=printval.next

    def atBeginning(self,newdata):
        Newdata=Node(newdata)
        Newdata.next=self.head
        self.head=Newdata

    def atEnd(self,newdata):
        Newdata=Node(newdata)
        if self.head==None:
            self.head=Newdata
            return
        current=self.head
        while(current.next is not None):
            current=current.next
        else:
            current.next=Newdata

    def atPosition(self,position,newdata):
        Newdata=Node(newdata)
        if position==0:
            self.atBeginning()
        else:
            count=0
            current=self.head
            while(current.next is not None):
                count+=1
                if count==position-1:
                    next=current.next
                    current.next=Newdata
                    Newdata.next=next
                    return
                current=current.next

    def del_start(self):
        if self.head==None:
            return 0
        else:
            self.head=self.head.next

    def del_end(self):
        if self.head==None:
            print("No Element")
            return
        if self.head.next==None:
            self.head=None
            return
        sec_last=self.head
        while sec_last.next.next is not None:
            sec_last=sec_last.next
        sec_last.next=None

    def del_value(self,data):
        if self.head==None:
            print("No Element")
            return
        if self.head.data==data:
            self.head=None
            return
        current=self.head
        while(current.next is not None):
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
        
List=SLinkedList()
List.head=Node("A")
e1=Node("B")
e2=Node("C")
List.head.next=e1
e1.next=e2
List.listprint()
List.atBeginning("#")
List.listprint()
List.atEnd("|")
List.listprint()
print("--------------------")
List.atPosition(3,"XY")
List.listprint()
print("--------------------")
List.del_start()
List.listprint()
print("--------------------")
List.del_end()
List.listprint()
print("--------------------")
List.del_value("XY")
List.listprint()


#3
#Reversing a linked list

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("list has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no elements to delete")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Item not found in the list")
        else:
            n.ref = n.ref.ref

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("Item not found")
        return False

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()

print("after deletion at the begining")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("after deletion at the end")
new_linked_list.traverse_list()
new_linked_list.delete_element_by_value(20)
print("after deleting 30")
new_linked_list.traverse_list()
new_linked_list.search_item(5)
new_linked_list.search_item(25)
print("the number of Nodes",new_linked_list.get_count())
new_linked_list.insert_at_index(3,8)
new_linked_list.traverse_list()
           
