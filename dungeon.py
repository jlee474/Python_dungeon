
import random
from item import Item
# keyHelper -> to help capture keyboard input, more specifically arrow key
import keyHelper
# console.py file for system commands
import console

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
            # to convert into an array for operative function
            randomLocation = [randomLocation] 
            # the conversion to "set" is to do arithmetic function, and list to convert back
            availableLocations = list (set(availableLocations) - set(randomLocation)) 
            newItemsArray.append(newItem)
        return newItemsArray

    # prints the array of items and their location
    def checkItems(self): 
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
            # creating the row header
            rowContent = f'{row}|' 
            for column in self.mapColumns:
                content = self.get_content_at_location(f'{column}{row}')
                # if the return object was null/undefined (Javascript term), it is None
                if content is None: 
                    content = "  ░  "
                elif content.type == "Player": 
                    content = "  Ö  "
                else: 
                    content = "  ░  "
                # the extra space is because of the | separator also takes up a space
                rowContent = rowContent + content + " " 
            print(rowContent) 
    
    def runGame(self):
        available_commands = ["Up", "Right", "Down", "Left"]

        while (self.running):
            console.clear()
            self.printMap()
            # to capture user input
            print('Make your move (Use Arrow Keys. Escape key to exit game) ')
            userInput = keyHelper.keyboard_input()
            if userInput == "Escape":
                console.exit()
            elif userInput in available_commands:
                print (userInput)
                self.move(userInput)
    
    # move() is to move a player space
    def move(self, userInput):
        print(f' **in Game function move()**  The userInput value is {userInput}')

        # TODO: define the function to move the Player item one adjacent space
        pass
        








if __name__ == "__main__":
    game = Game()