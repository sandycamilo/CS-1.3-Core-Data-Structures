#Implementing a stack with a dynamic array
# (non Object Oriented)

#create a stack 
#instantiate a python list
my_stack = []

#update stack ~ add 
item = "A"
my_stack.append(item)
my_stack.append("B")
my_stack.append("C")

#delete from my_stack
#remove the last item 
my_stack.pop(len(my_stack) - 1)  

#read - only from the last item 
print(my_stack[len(my_stack)-1])


# __________________________________________________________________________

# Stack implemention using OOP ~ reusable 

class Stack:
  def __init__(self):
    #create a stack 
    self.my_stack = []

# add something to the top of the stack 
def push(self, item):
  #push item to the end of the stack
  self.my_stack.append(item)

#delete ~ remove something from the top of the stack 
def my_pop(self):
  return self.my_stack.pop(len(self.my_stack) - 1) 

#read the top of the stack 
def peek(self):
    return self.my_stack[len(self.my_stack) - 1]
    