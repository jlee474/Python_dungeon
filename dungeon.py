import random
from item import Item

class Game:
    def __init__(self) -> None:
        self.running = True # True means the game is running and not over
        self.mapColumns = ['A', 'B', 'C', 'D'] # size of the map columns
        self.mapRows = 4 # size of the map row
        self.map = self.setMap()
        self.items = self.setItems( ["Player", "Monster", "Exit"] ) # the items is dependent on the self.map, so this must come afterwards.
        self.runGame()
    
    def setMap(self): # sets a blank map specified by the map dimensions
        createdMap = []
        for column in self.mapColumns:
            for row in range(1, self.mapRows + 1, 1):
                createdMap.append(f'{column}{row}')
        return createdMap

    def setItems(self, itemsArray):
        newItemsArray = []
        availableLocations = self.map.copy()
        for item in itemsArray:
            randomLocation = random.choice(availableLocations)
            newItem = Item(item, randomLocation)
            randomLocation = [randomLocation] # to convert into an array for operative
            availableLocations = list (set(availableLocations) - set(randomLocation)) # the conversion to set is to do arithmetic function, and list to convert back
            newItemsArray.append(newItem)
        return newItemsArray

    def checkItems(self): # prints the array of items and their location
        for item in self.items:
            print(item)

    def checkAdj(self, item1, item2):
        print("checks if an item is adjacent. not yet implemented")
    
    def get_content_at_location(self, location):
        for item in self.items:
            if item.location == location:
                return item
        return
    
    def printMap(self):
        column_header = ' |  ' + '  |  '.join(self.mapColumns) + '  |'
        print(column_header)
        for row in range(1, self.mapRows + 1, 1):
            rowContent = f'{row}|' # creating the row header
            for column in self.mapColumns:
                content = self.get_content_at_location(f'{column}{row}')
                if content is None: # if the return object was null/undefined (Javascript term), it is None
                    content = "  ░  "
                elif content.type == "Player": 
                    content = "  Ö  "
                else: 
                    content = "  ░  "
                rowContent = rowContent + content + " " # the extra space is because of the | separator also takes up a space
            print(rowContent) 
    
    def runGame(self):
        self.printMap()
        input("This part to be implemented > ") # TODO: implement user command to move Player !!!!!!!!!!!!!!!!!!!!!!!!!




if __name__ == "__main__":
    game = Game()