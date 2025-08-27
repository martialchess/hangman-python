import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    "aardvark", "baboon", "camel",
    "python", "java", "keyboard", "monitor", "pencil",
    "guitar", "violin", "puzzle", "mystery", "rocket",
    "castle", "pirate", "treasure", "island", "jungle",
    "pyramid", "bridge", "planet", "galaxy", "universe",
    "school", "teacher", "library", "garden", "circus"
]


# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if "_" not in display:
        game_over = True
        print("You win.")
    elif guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You lose a life. Lives left: {lives}")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You lose.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
