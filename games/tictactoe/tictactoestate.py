from GameBot.games.game.gamestate import GameState
import string

class TicTacToeState(GameState):
    def __init__(self):
        super().__init__()
        self.states = {"": [[0,0,0], [0,0,0], [0,0,0]]}
    
    def addState(self, state):
        super().addState(state)