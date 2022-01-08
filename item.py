class Item:
    def __init__(self, type, location) -> None:
        self.type = type
        self.location = location

    # (dunder eq is a reserved method) to check if location matches    
    def __eq__(self, other): 
        return self.location == other.location

    # for print output display 
    def __str__(self) -> str: 
        return f'Type: {self.type}; Location: {self.location}'

if __name__ == '__main__':
    pass

