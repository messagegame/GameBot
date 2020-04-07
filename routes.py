from GameBot.server import app
from GameBot.games.game.game import Game
from GameBot.games.game.gamemanager import GameManager#
from GameBot.games.tictactoe.tictactoegame import TicTacToeGame
from flask import request, jsonify

gameMapping = {
    "game": Game,
    "tictactoe": TicTacToeGame
}
gameManager = GameManager() # You have to call /tictactoe/create every time you save.

@app.route('/<game>/setState')
def setState(game):
    gameId = request.values.get("gameId")
    stateId = request.values.get("stateId")

    return f"State {state} is Invalid for {game}?{id}"

@app.route('/<game>/getSetState?id=<id>')
def getSetState(game):
    return f"{game}?{id} does not have a setState URL"

@app.route('/<game>/stateUI')
def stateUI(game):
    stateId = request.values.get("stateId") or ""
    gameId = request.values.get("gameId") or ""

    print(f"[debug stateUI]: gameId is {gameId}")
    
    if gameManager.games.get(gameId):
        return gameManager.games.get(gameId).stateUI(stateId)
    
    return {"render": False}


@app.route('/<game>/create/')                                   #Creates a game
def create(game):
    gameId = False
    if gameMapping.get(game):                                   #Make sure game exists
        gameId = gameManager.addGame(gameMapping.get(game)())   #Makes a new game and game id

    return jsonify({"gameId": gameId})

    