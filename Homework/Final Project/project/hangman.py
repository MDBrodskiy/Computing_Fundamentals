"""
 * =====================================================
 *
 *       Filename:  hangman.py
 *       Assignment: EECE 2140 Final Project
 *       Title: Hangman
 *
 *    Description:  A rendition of the classic hangman game
 *
 *        Version:  1.0
 *        Created:  04/20/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * =====================================================
""" 

import random

class hangman: # Create a class for the game

    def __init__(self): # Initialize the class

        # Create a tui-based figure for the game
        self.figure = ["\t  ____\t\n\t |    |\n\t |    \n\t |   \n\t |    \n\t |   \n\t_|_", "\t  ____\t\n\t |    |\n\t |    o\n\t |   \n\t |    \n\t |   \n\t_|_", "\t  ____\t\n\t |    |\n\t |    o\n\t |   /|\n\t |    \n\t |   \n\t_|_", "\t  ____\t\n\t |    |\n\t |    o\n\t |   /|\\\n\t |    \n\t |   \n\t_|_", "\t  ____\t\n\t |    |\n\t |    o\n\t |   /|\\\n\t |    |\n\t |   / \n\t_|_", "\t  ____\t\n\t |    |\n\t |    o\n\t |   /|\\\n\t |    |\n\t |   / \\\n\t_|_"] 

    def __str__(self, lost_limbs):

        # Print the figure above
        return self.figure[lost_limbs]

class game(hangman):

    def __init__(self, mode = 0): # Initialize

        super().__init__() # Initialize the superclass

        # Create a value to keep track of the mode, protected
        self._mode = mode # 0 for single player, 1 for multi player
        self.limbs_lost = 0 # Create a lives lost variable
        self.totalguesses = 0 # Create a total guess value
        self.guessedLetters = [] # Create guessed letter bank


    @property # read property of the mode
    def mode(self):
        return self._mode

    @mode.setter # write property of the mode
    def mode(self, mode):
        if mode not in [0, 1]: # Raise an error if mode not valid
            raise ValueError("The mode has to be one or zero")
        else:
            self._mode = mode

    def enter_word(self, word):

        self.generate_secret(word) # generates the secret
        self.word = word # sets the word to entered word
            
    def guess_part(self, guess): # Guess part of the word

        if (len(guess) > 1): # Checks that a single letter was entered
            print("Not a letter")
            return -1

        guess = str(guess.lower()) # Make the guess lower case
        if (guess not in self.guessedLetters): # Checks if a letter was already guessed
            self.guessedLetters.append(guess)
        else:
            print("Letter has already been guessed!")
            return -1

        try: # If there is a ValueError, return -1
            index = self.word.index(guess)
        except ValueError:
            index = -1
        if (index == -1):
            self.totalguesses += 1 # Increase total guesses
            self.limbs_lost += 1 # Otherwise, lose a limb
            return -1

        while (index != -1): # Find if guess is in the word

            # Replace secret to contain all instances of guess
            self.secret = self.secret[:self.word.index(guess)] + guess + self.secret[self.word.index(guess) + len(guess):]
            # Replace the word contents of guess to uppercase so replacement is not repeated
            self.word = self.word[:self.word.index(guess)] + guess.upper() + self.word[self.word.index(guess) + len(guess):]

            try: # If there is a ValueError, return -1
                index = self.word.index(guess)
            except ValueError:
                index = -1

        self.totalguesses += 1 # Increase total guesses

        return 0

    def guess_phrase(self, guess): # Guess the whole phrase

        if (self.word.lower() == guess.lower()): # If correct return true
            self.secret = self.word.lower()
            self.totalguesses += 1
            return True
        else: # Otherwise, lose a limb and return false
            self.totalguesses += 1
            self.limbs_lost += 1
            return False

    def generate_word(self): # Used to generate a new word

        # Randomly obtain a word from the word bank below
        bank = ["abruptly", "absurd", "abyss", "affix" "askew" "avenue" "awkward" "axiom" "azure" "bagpipes" "bandwagon" "banjo" "bayou" "beekeeper" "bikini" "blitz" "blizzard" "boggle" "bookworm" "boxcar" "boxful" "buckaroo" "buffalo" "buffoon" "buxom" "buzzard" "buzzing" "buzzwords" "caliph" "cobweb" "cockiness" "croquet" "crypt" "curacao" "cycle" "daiquiri" "dirndl" "disavow" "dizzying" "duplex" "dwarves" "embezzle" "equip" "espionage" "euouae" "exodus" "faking" "fishhook" "fixable" "fjord" "flapjack" "flopping" "fluffiness" "flyby" "foxglove" "frazzled" "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

        self.word = bank[random.randint(0, len(bank))]

        return (self.word, self.generate_secret(self.word))

    def generate_secret(self, word): # Used to generate a secret corresponding to the word, must be called after word generation

        self.secret = ""

        for i in word:

            if (i != " "): # Set all letters to underscores

                self.secret += "_"

            else: # Keep spaces as spaces

                self.secret += " "

        return self.secret

    def end(self):

        # Check for game end
        try: # If there is a ValueError, return -1
            index = self.secret.index("_")
        except ValueError:
            index = -1
        if (index == -1 or self.limbs_lost == 5):
            return True

        return False

    def menu(self): # Prints the menu
        return int(input("What would you like to do?\n1. Guess a letter\n2. Guess a word\nChoice: "))

    def play(self): # Runs the game

        if (self.mode == 0): # If the mode is single player, generate a word

            self.generate_word()

        else: # If mode is 1, have other player enter a phrase

            self.enter_word(input("enter a word: ").lower())

        while (not self.end()): # Loops until game is won or lost
            self.__str__() # Prints this object as a string
            choice = self.menu() # Prints menu
            if (choice == 1): # Routes to guess letter, phrase, or choose again
                self.guess_part(input("Guess: "))
            elif (choice == 2):
                self.guess_phrase(input("Guess: "))
            else:
                print("Choose again")
        if (self.limbs_lost < 5): # Win state
            print("You guessed the phrase! You win!")
            print(f"Your accuracy was: {((1 - (self.limbs_lost / self.totalguesses)) * 100):.2f}%")
        else: # Loss state
            print(super().__str__(self.limbs_lost))
            print("You were hung! You lose!")
            print(f"The correct phrase was \"{self.word.lower()}\"")

    def __str__(self): # Prints the game
        print() # Spacer
        print("Total Guesses:", self.totalguesses) # Prints guess count
        print("Lives Lost (5 Total):", self.limbs_lost) # Prints Lives
        print(super().__str__(self.limbs_lost)) # Prints hangman figure
        print("Letters Guessed: ", self.guessedLetters) # Print guessed letter list
        print(self.secret) # Prints the remaining characters to guess
        print() # Spacer

# The code below is an example of how the above classes would be implemented
mSel = int(input("Welcome to hangman!\nWhat mode would you like to play in?\n1. Singleplayer\n2. Multiplayer\nMode: ")) - 1 # Obtains a mode
while (mSel not in [0, 1]): # If mode is invalid, tries again
    mSel = int(input("Invalid option, choose again: "))
Game = game(mSel) # Creates object with mode
Game.play() # Plays game
while (mSel != -1): # Asks user to play again
    choice = input("Play again? (y/n): ")[0].lower()
    if (choice == "y"):
        Game = game(int(input("What mode would you like to play in (0 to exit)?\n1. Singleplayer\n2. Multiplayer\nMode: ")) - 1) # Runs mode select again
        Game.play()
        mSel = -1
    else: # If user is done, exits
        print("Exiting...")
        mSel = -1

