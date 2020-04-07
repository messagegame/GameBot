import string

class GameState:
    """
    GameState is an abstract class that helps you store data.
    """
    def __init__(self):
        self.states = {"": [1]}
        self.lastState = ""

    def addState(self, state):
        """
        Given a state, (could be a 2d array, etc, add it to the state dictionary).
        Returns the stateId
        """
        stateId = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
        while self.states.get(stateId):
            stateId = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
            
        self.states[stateId] = state
        self.lastState = stateId

        return stateId

    
