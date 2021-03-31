import Game

game = Game.Game()


# Test pour vérifier si la partie est en cours
assert game.getGameResult() == 2 , "La partie est terminée"

#  Test pour vérifier si un jeu d'apprentissage est dispobible
assert not game.getTrainingHistory() , "Un historique d'apprentissage est disponible"

#  Test pour vérifier si une mémorisation d'une partie existe
assert game.getAvailableMoves() , "La mémorisation d'une partie est inexistante"