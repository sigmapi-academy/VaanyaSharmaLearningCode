class Parent:
    def __init__(self, pid, pnm, pemail, paddr, pmobile):
        self.pid = pid
        self.pnm = pnm
        self.pemail = pemail
        self.paddr = paddr
        self.pmobile = pmobile
        
    def greet(self):
        return f"Hello {self.pnm} Good Afternoon"
    

# main code

alice = Parent('p101', 'Alice', 'alice@g.com', 'JK Road Block: B45 Texas', '9876523')
bob = Parent('p102', 'Bob', 'alice@g.com', 'JK Road Block: B78 Texsus', '98765432')
   
print(alice.greet())
print(bob.greet())     