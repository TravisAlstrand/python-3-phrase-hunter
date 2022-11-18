from phrasehunter import game


if __name__ == '__main__':
  new_game = game.Game()
  # UNCOMMENT THE LINE BELOW TO SEE THE PHRASE FOR TESTING PURPOSES!
  # print(new_game.active_phrase.phrase)
  new_game.start()