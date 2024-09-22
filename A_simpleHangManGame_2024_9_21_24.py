# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:58:43 2024
@author: segal
"""
# hangMan Game time!!!
import random
Words = ("aardvark", "alligator", "alpaca", "ant", "anteater", 
         "antelope", "ape", "armadillo", "baboon", "badger", "bat",
         "bear", "beaver", "bee", "bison", "boar", "buffalo",
         "butterfly", "camel", "capybara", "caribou", "cat",
         "caterpillar", "cattle", "chamois", "cheetah", "chicken",
         "chimpanzee", "chinchilla", "chough", "clam", "cobra",
         "cockroach", "cod", "coyote", "crab", "crane", "crocodile",
         "crow", "curlew", "deer", "dinosaur", "dog", "dogfish",
         "dolphin", "donkey", "dormouse", "dotterel", "dove",
         "dragonfly", "duck", "dugong", "dunlin", "eagle",
         "echidna", "eel", "eland", "elephant",  "elk", "emu",
         "falcon", "ferret", "finch", "fish", "flamingo",
         "fly", "fox", "frog", "gaur", "gazelle",
         "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch",
         "goldfish", "goose", "gorilla", "goshawk", "grasshopper",
         "grouse", "guanaco", "gull", "hamster", "hare", "hawk",
         "hedgehog", "heron", "herring", "hippopotamus", "hornet",
         "horse", "human", "hummingbird", "hyena", "ibex", "ibis",
         "jackal", "jaguar", "jay", "jellyfish", "kangaroo",
         "kingfisher", "koala", "kookabura", "kouprey", "kudu",
         "lapwing", "lark", "lemur", "leopard", "lion", "llama",
         "lobster", "locust", "loris", "louse", "lyrebird", "magpie",
         "mallard", "manatee", "mandrill", "mantis", "marten",
         "meerkat", "mink", "mole", "mongoose", "monkey", "moose",
         "mosquito", "mouse", "mule", "narwhal", "newt",
         "nightingale", "octopus", "okapi", "opossum", "oryx",
         "ostrich", "otter", "owl", "ox", "oyster", "panda",
         "panther", "parrot", "partridge", "peafowl", "pelican",
         "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony",
         "porcupine", "porpoise", "quail", "quelea", "quetzal",
         "rabbit", "raccoon", "rail", "ram", "rat", "raven",
         "red-deer", "red-panda", "reindeer", "rhinoceros",
         "rook", "salamander", "salmon", "sand-dollar",
         "sandpiper", "sardine", "scorpion", "seahorse", "seal",
         "shark", "sheep", "shrew", "skunk", "snail", "snake",
         "sparrow", "spider", "spoonbill", "squid", "squirrel",
         "starling", "stingray", "stoat", "stork", "swallow",
         "swan", "tapir", "tarsier", "termite", "tiger", "toad",
         "trout", "turkey", "turtle", "viper", "vulture", "wallaby",
         "walrus", "wasp", "weasel", "whale", "wildcat", "wolf",
         "wolverine", "wombat", "woodpecker", "worm", "yak", "zebra")

# dict with art: 
HangManArt = {0:("   ",
                 "   ",   
                 "   "),
              1:(" O ",
                 "   ",   
                 "   "),
              2:(" O ",
                 " | ",   
                 "   "),
              3:(" O ",
                 "/| ",   
                 "   "),
              4:(" O ",
                 "/|\\",
                 "   "),
              5:(" O ",
                 "/|\\",   
                 "/  "),
              6:(" O ",
                 "/|\\",   
                 "/ \\")}
#print(HangManArt) # a way to test the dictionary works
#for line in HangManArt[5]:
#    print(line)
# next to know number of wrong guesses
def displayHanging(WrongGuess):
    #pass
    # to display image
    print("===================================")
    for line in HangManArt[WrongGuess]:
        print(line)
    print("===================================")

def DisplayHint(hint):
    #pass
    print(" ".join(hint))

def DisplayAnswer(answer):
    #pass
    print(" ".join(answer))
def main():
    #pass
    answer = random.choice(Words)
    # a test to see from the set
    #print(answer)
    hint = ["_"] * len(answer)
    print(hint)
    # keeping track of wrong guesses
    WrongGuess = 0
    GuessLetters = set()
    IsRunning = True
    
    while IsRunning:
        displayHanging(WrongGuess)
        DisplayHint(hint)
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue
        if guess in GuessLetters:
            print(f"{guess} was already used.")
            continue
        GuessLetters.add(guess)
        
        if guess in answer:
            
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            WrongGuess += 1
        if "_" not in hint:
            displayHanging(WrongGuess)
            DisplayAnswer(answer)
            print("You Won!!")
            IsRunning = False
        elif WrongGuess >= len(HangManArt) - 1:
            displayHanging(WrongGuess)
            DisplayAnswer(answer)
            print("\nYou Suck & You Lost!!")
            IsRunning = False
if __name__ == "__main__":
    main()