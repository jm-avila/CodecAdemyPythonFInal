class Game:
    name = "unknown"

    def greet(self):
        self.handleNameInput()
        print("Hello {}".format(self.name))
        print("Please answer with a yes or no to go to the next question.")
        understood = self.handleYesNoInput("Understood?")
        if (understood):
            print("Great")
        else:
            print("Better catch up")
        print("Let's Start!!!")

    def handleNameInput(self):
        print("Whats your name?")
        userInput = input()
        if (len(userInput) == 0):
            return self.name
        self.name = userInput

    def handleYesNoInput(self, question):
        print(question)
        userInput = input()
        userInput = userInput.lower()
        if (userInput == "yes"):
            return True
        if (userInput == "no"):
            return False
        if (len(userInput) == 0):
            print("No input was provided!!!")
        else:
            print("Answer with a yes or no")
        return self.handleYesNoInput()