from time import time
import random
class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
    def insert_head(self,node):
        nodes=LinkedListNode(node)
        if not self.head:
            self.head=nodes
            self.tail=nodes
        else:
            nodes.next=self.head
            self.head=nodes

    def insertar(self,node_data):
        node_datas=LinkedListNode(node_data)
        if not self.head:
            self.head=node_datas
        else:
            self.tail.next = node_datas

        self.tail = node_datas
    def insert_position(self,node,position):
        nodes=node
        if position==0:
            self.insert_head(nodes)
        else:
            current=self.head
            count=0
            while(count<position-1):
                current=current.next
                count+=1
            if current==self.tail:
                self.tail.next=nodes
                self.tail=nodes
            else:
                nodes.next=current.next
                current.next=nodes
    def modify(self,node_data,position):
        if not self.head:
            print("la lista está vacia")
        else:
            current=self.head
            count=0
            while(count<position):
                if not current.next:
                    print("no existe la posicion", position )
                    break
                else:
                    current=current.next
                    count+=1
            current.data=node_data
    def search(self,node_data):
        if self.head:
            count=0
            current=self.head
            flag=True
            while current and flag:
                if current.data==node_data:
                    flag=False
                    break
                count+=1
                current=current.next
            if not flag:
                return None
            else:
                return count #posicion


    def delete(self,node_data):

        if self.head:
            flag=True
            current=self.head
            while(flag and current.next):

                if current.next.data==node_data:
                    flag=False
                    break
                current=current.next
            if not flag:
                if current==self.head:
                    self.head=self.head.next
                else:
                    current.next=current.next.next

    def delete_pos(self,position):
        if self.head:
            if position==0:
                self.head=self.head.next

            else:
                current=self.head
                count=0
                flag=True
                while(count<position-1 and flag):
                    if not current:
                        return None
                    current=current.next
                    count+=1
                current.next=current.next.next

    def search_pos(self,position):
        if self.head:
            current=self.head
            count=0
            while(count<position):
                if not current.next:
                    return False
                current=current.next
                count+=1
            return current.data
    def consulta(self):
        listas=[]
        current=self.head
        while(current):
            listas.append(current.data)
            current=current.next
        return listas

    def sumatoria(self):
        a = 0
        current=self.head
        while(current):
            a += current.data
            current=current.next
        return a
"""
a=SinglyLinkedList()
s=time()
for i in range(100000):

    a.insertar(random.randint(0,100000))
print(time()-s)

s=time()

for i in range(100000):
    print(i)
    a.delete((random.randint(0,100000)))
print(time()-s)
s=time()

"""






