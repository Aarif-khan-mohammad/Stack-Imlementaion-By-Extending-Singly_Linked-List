from Singly_Linked_List import *

class Stack(SLL):

    def __init__(self):
        super().__init__() #we need to use super() for calling parents class's __init__ method , beacause of method overriding
        self.item_count = 0

    def is_empty(self):
        return super().is_empty() #we used super() method beacuse , is_empty method already existed so , to prevent method overriding we aare using super() method.
    
    def push(self , data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack UnderFlow")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack UnderFlow")
    
    def size(self):
        return self.item_count

s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print()
print("top value = " , s1.peek())
s1.pop()
print("top value = " , s1.peek())
print("size of array = ",s1.size())