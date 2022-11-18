import random

from phrasehunter.phrase import Phrase


class Game():
  
  def __init__(self):
    self.missed = 0
    self.phrases = self.create_phrases()
    self.active_phrase = self.get_random_phrase()
    self.guesses = [" "]

  def create_phrases(self):
    phrases_list = [Phrase('GrEaTeSt PhRaSe Of AlL tImE'),
                    Phrase('WoRsT pHrAsE eVeR'),
                    Phrase('I hAtE cOmInG uP wItH pHrAsEs'),
                    Phrase('NeVeR sEeN a BeTtEr PhRaSe'),
                    Phrase('oNe PhRaSe To RuLe ThEm AlL')
    ]
    return phrases_list

  def get_random_phrase(self):
    random_phrase = random.choice(self.phrases)
    return random_phrase

  def welcome(self):
    print("\n*** Welcome to Phrase Hunter! ***\n")
    print("\nThe first rule of Phrase Hunter is: We do not talk about Phrase Hunter.\n")
    print("\nThe second rule of Phrase Hunter is: WE DO NOT TALK ABOUT PHRASE HUNTER!!\n")
    print("... \nok have fun\n")

  def start(self):
    self.welcome()
    while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
      print(f"\n*** Number missed: {self.missed}\n")
      self.active_phrase.display(self.guesses)
      user_guess = self.get_guess()
      self.guesses.append(user_guess)
      if not self.active_phrase.check_guess(user_guess):
        self.missed += 1
    self.game_over()

  def get_guess(self):
    guess = input('\n\nGuess a letter! >>> ')
    return guess

  def game_over(self):
    if self.missed >= 5:
      print("I'm sorry, you lost!")
    else:
      print("Good job! You won!")