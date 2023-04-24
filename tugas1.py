class Stack:
    def __init__(self):
        self.stacko =[]
        self.top = -1
        
    def push(self,value):
        self.top += 1
        self.stacko.insert(self.top, value)
        
    def is_empty(self):
        return self.top == -1
    
    def  size(self):
        return self.top + 1
    
    def pop(self):
        if not self.is_empty():
           self.top -= 1
           return self.stacko.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stacko[self.top]
        else: 
            return None
            
    def reversed(self):
        reversed_str = ""
        while not self.is_empty():
            reversed_str += self.pop()
        return reversed_str
    
st = Stack()
userInput = input("Masukan kata : ")

for i in range(len(userInput)):
    st.push(userInput[i])

reversed_outp = st.reversed()

print("Reversed : ", reversed_outp)


    
        
       