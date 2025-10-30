class Package:
    def __init__(self,number,sender,recipient, weight):   # Dunder init method, here self refers to instance for object we are creating
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        

def main():
    packages = [
        Package(number=1,sender="vivek",recipient="golu",weight=10),
        Package(number=2,sender="Bob",recipient="Charlie",weight=5)
    ]
    
    
main()