from GameBot.server import app
from GameBot.games.game.game import Game
from GameBot.games.game.gamemanager import GameManager#
from GameBot.games.tictactoe.tictactoegame import TicTacToeGame
from flask import request, jsonify, url_for
from flask_cors import cross_origin
from urllib.parse import urljoin
import json

gameMapping = {
    "game": Game,
    "tictactoe": TicTacToeGame
}
gameManager = GameManager() # You have to call /tictactoe/create every time you save.

@app.route('/<game>/setState')
def setState(game):
    gameId = request.values.get("gameId")
    state = request.values.get("state")

    print(f"[debug routes/setState] state is {state}")

    newStateId = gameManager.games.get(gameId).state.addState(json.loads(state))
    print(f"[debug routes/setState] newStateId is {newStateId}")  

    return jsonify({"stateId": newStateId})
 
@app.route('/<game>/getStateUIUrl') 
@cross_origin()
def getStateUIUrl(game): 
    gameId = request.values.get("gameId")
    stateId = request.values.get("stateId") # Optional, if the client requests it.

    newStateId = gameManager.games.get(gameId).state.lastState

    if stateId:
        newStateId = stateId
    
    return jsonify({"stateUIUrl": urljoin(request.url_root, url_for("stateUI", game=game, gameId=gameId, stateId=newStateId)) })

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

    