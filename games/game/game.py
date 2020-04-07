from flask import render_template
from GameBot.games.game.gamestate import GameState
import random
import string

class Game:
    def __init__(self, computer=None, state=GameState()):
        self.state = state # This is a dictionary of states. Having a state id mitigates issues.
        self.id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))
        if computer: 
            self.computer = computer
    
    def stateUI(self, stateId):
        """
        Override this method.
        This method takes the parameter previousStateId and renders a playable game. 
        Returns false if the stateId cannot be found.
        stateUI: returns a template from render_template
        """
        state = self.state.states.get(stateId)
        if state:
            # Change the below line to game/tictactoe/tictactoe.template.html, etc.
            return render_template("game/game.template.html", stateData=state, 
                                    gameEditable=(stateId == self.state.lastState)) # Can only edit if this is actually the previous state ID
        
        return False
    
    def setState(self, state):
        """
        Gets called as an AJAX request from stateUI.
        Returns the created state's ID.
        """
        return self.state.addState(state)

