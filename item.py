class Item:
    def __init__(self, type, location) -> None:
        self.type = type
        self.location = location
        
    def __eq__(self, other): # (dunder eq is a reserved method) to check if location matches
        return self.location == other.location

    def __str__(self) -> str: # for output
        return f'Type: {self.type}; Location: {self.location}'

if __name__ == '__main__':
    pass

