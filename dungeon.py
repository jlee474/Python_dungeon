import random
import time
from item import Item
# keyHelper -> to help capture keyboard input, more specifically arrow key
import keyHelper
# console.py file for system commands
import console

class Game:
    def __init__(self) -> None:
        self.running = True # True means the game is running and not over
        self.mapColumns = ['A', 'B', 'C', 'D'] # size of the map columns. Put in order
         # sets the first and last column to determine border
        self.firstCol = self.mapColumns[0]
        self.lastCol = self.mapColumns[-1]
        self.mapRows = 5 # size of the map row, maximum up to 9
        self.map = self.setMap()
        self.items = self.setItems( ["Player", "Monster", "Exit"] ) # the items is dependent on the self.map, so this must come afterwards.
        self.gameWon = False
        self.runGame()
    
    def setMap(self): # sets a blank map specified by the map dimensions
        createdMap = []
        for column in self.mapColumns:
            for row in range(1, self.mapRows + 1, 1):
                createdMap.append(f'{column}{row}')
        return createdMap

    def setItems(self, itemsArray):
        
        while (True):
            newItemsArray = []
            availableLocations = self.map.copy()
            
            for item in itemsArray:
                randomLocation = random.choice(availableLocations)
                newItem = Item(item, randomLocation)
                if item == "Player":
                    playerItem = newItem
                elif item == "Monster":
                    monsterItem = newItem
                elif item == "Exit":
                    exitItem = newItem
                # to convert into an array for operative function
                randomLocation = [randomLocation] 
                # the conversion to "set" is to do arithmetic function, and list to convert back
                availableLocations = list (set(availableLocations) - set(randomLocation)) 
                newItemsArray.append(newItem)

            if not(self.checkAdjace(playerItem, monsterItem)) and not(self.checkAdjace(playerItem, exitItem)):
                break
        return newItemsArray

    # prints the array of items and their location
    def checkItems(self): 
        for item in self.items:
            print(item)

    # checks if item2 occupies an adjacent space RELATIVE to item1
    def checkAdjace(self, item1, item2):
        directions = ["Up", "Right", "Down", "Left"]
        prohibitDirection = self.prohbitedDirection(item1.location)
        allowedDirections = list (set(directions) - set(prohibitDirection))
        for direction in allowedDirections: 
            if item2.location == self.direction(item1.location, direction):
                return True
        return False
    
    def checkMatchandWinLoss(self, playerLoc):
        monster = self.grabItem("Monster")
        exit = self.grabItem("Exit")
        if playerLoc == monster.location:
            self.running = False
            self.printMap()
            print(" You landed on the monster! You died ... ")
            time.sleep(1)
        elif playerLoc == exit.location:
            self.running = False
            self.gameWon = True
            self.printMap()
            print(" You found the exit! You Win! ")
            time.sleep(1)

    def get_content_at_location(self, location):
        for item in self.items:
            if item.location == location:
                return item
        return
    
    # returns the item by the given type
    def grabItem(self, type):
        for item in self.items:
            if item.type == type:
                return item

    def printMap(self):
        console.clear()
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
                    if self.running:
                        content = "  Ö  "
                    elif self.gameWon:
                        content = " WIN "
                    else:
                        content = "  M  "
                elif content.type == "Exit":
                    content = " EXIT"
                else: 
                    content = "  ░  "
                # the extra space is because of the | separator also takes up a space
                rowContent = rowContent + content + " " 
            print(rowContent) 
        if (self.checkAdjace(self.grabItem("Player"), self.grabItem("Monster"))) and not(self.gameWon):
            print("The Monster is near you!")
    
    def runGame(self):
        available_commands = ["Up", "Right", "Down", "Left"]

        while (self.running):
            self.printMap()
            # to capture user input
            print('Make your move (Use Arrow Keys. Escape key to exit game) ')
            userInput = keyHelper.keyboard_input()
            if userInput == "Escape":
                # console.exit()
                break; # use break for debugging purposes. change to console.exit() once coding is done.
            elif userInput in available_commands:
                self.move(userInput)
                
    # to determine edge cases outside the map
    def prohbitedDirection(self, baseLoc):
        # set an array of prohibited moves, i.e. when Player is at the edge or corner of map
        prohibitedMove = []
        # TODO: implement a way to parse location so it is not limited by digits
        baseLocCol = baseLoc[0]
        # convert to integer as it is string format
        baseLocRow = int(baseLoc[1])
        if baseLocCol == self.firstCol:
            prohibitedMove.append("Left")
        elif baseLocCol == self.lastCol:
            prohibitedMove.append("Right")
        if baseLocRow == 1:
            prohibitedMove.append("Up")
        elif baseLocRow == self.mapRows:
            prohibitedMove.append("Down")
        return prohibitedMove

    # returns the location is in a given direction, relative to the baseLocation
    def direction(self, baseLoc, direction):
        # TODO: implement a way to parse location so it is not limited by digits
        baseLocCol = baseLoc[0]
        # convert to integer as it is string format
        baseLocRow = int(baseLoc[1])
        if direction == "Up":
            baseLocRow -= 1
        elif direction == "Down":
            baseLocRow += 1
        else:
            baseLocColIndex = self.mapColumns.index(baseLocCol)
            if direction == "Right":
                baseLocColIndex += 1
            elif direction == "Left":
                baseLocColIndex -= 1
            baseLocCol = self.mapColumns[baseLocColIndex]

        newLocation = str(baseLocCol) + str(baseLocRow)
        return newLocation


    # move() is to move a player space
    def move(self, userInput):
        playerObject = self.grabItem("Player")
        playerLocation = playerObject.location
        prohibitedMove = self.prohbitedDirection(playerLocation)
        if (userInput in prohibitedMove):
            return
        playerObject.location = self.direction(playerLocation, userInput)
        self.checkMatchandWinLoss(playerObject.location)


if __name__ == "__main__":
    while (True):
        game = Game()
        print ("Do you want to play again? Press Y for Yes > ")
        userInput = keyHelper.keyboard_input()
        if not(userInput.upper() == "Y"):
            break