from GameBot.games.game.game import Game
from GameBot.games.tictactoe.tictactoestate import TicTacToeState
from flask import render_template

class TicTacToeGame(Game):
    def __init__(self, computer=None):
        super().__init__(computer, state=TicTacToeState())
    
    def stateUI(self, stateId):
        state = self.state.states.get(stateId) 
        if state:
            return render_template("tictactoe/tictactoe.template.html", stateData=state, 
                gameEditable=(stateId == self.state.lastState)) # Can only edit if this is actually the previous state ID
                # TODO: Handle gameEditable
        return False

    def setState(self, state):
        return self.state.addState(state)