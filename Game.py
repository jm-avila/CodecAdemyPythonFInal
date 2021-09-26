class Game:
    name = "unknown"
    ai_name = "Mr Robot"

    def handleStrInput(self, question):
        print(question)
        userInput = input()
        if (len(userInput) == 0):
            return self.handleStrInput(question)
        return userInput

    def handleNumInput(self, question):
        print(question)
        int = "Input a number from 1 - 10"
        print(int)
        userInput = input()
        if (len(userInput) == 0):
            userInput = self.handleNumInput(question)
        try:
            userInput = float(userInput)
        except:
            print("Wrong input, try again.")
            print(int)
            userInput = self.handleNumInput(question)
        if(userInput < 0 or userInput > 10):
            userInput = self.handleNumInput(question)
        return userInput

    def handleBoolInput(self, question, first = False):
        print(question, "yes/no")
        userInput = input()
        userInput = userInput.lower()
        if (userInput == "yes"):
            return True
        if (userInput == "no"):
            return False
        if (len(userInput) == 0):
            print("No input was provided!!!")
        return self.handleBoolInput(question)

    def greet(self):
        name = self.handleStrInput("Whats your name?")
        self.name = name
        print("Hello {}".format(name))
        print("Please answer with a yes or a no.")
        understood = self.handleBoolInput("Understood?")
        if (understood):
            print("Great")
        else:
            print("Better catch up")
        print("Let's Start!!!")
        self.question1()

    def question1(self):
        ans = self.handleBoolInput("Do you know me?")
        if (ans):
            self.sayMyName()
        else:
            self.wannaGuess()

    def sayMyName(self):
        ans = self.handleStrInput("Say my name")
        self.ending1(ans)

    def wannaGuess(self):
        ans = self.handleBoolInput("Wanna guess?")
        if (ans):
            self.guessLen()
        else:
            self.ending3(False)

    def guessLen(self):
        ans = self.handleNumInput("How many letters are in may name?")
        self.ending2(ans)

    def ending1(self, guess):
        if(guess.lower() == self.ai_name.lower()):
            print("You're right I'am: {}".format(self.ai_name))
        else:
            print("Never heard of {}".format(guess))

    def ending2(self, num):
        if (num == len(self.ai_name)):
            print("You're right, My name is: {}".format(self.ai_name))
        else:
            print("Sorry, try again.")

    def ending3(self, bool):
        if (bool):
            print("My name is: {}".format(self.ai_name))
        else:
            print("I guess you'll never know.")
