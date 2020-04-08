function playMove(x, y) {
    // just make the array I'll write the ajax call since it's stupid    
    var red = 0
    var blue = 0
    var state = [[0,0,0],[0,0,0],[0,0,0]]
    for(let i = 0; i < state.length; i++) {
        for(let j = 0; j < state[i].length; j++) {
            cName = ""
            try {
                cName = document.getElementById(i + ',' + j).className
            } catch(err) {}
            if(cName == "Red") {
                state[i][j] = 1
                red++
            }
            if(cName == "Blue") {
                state[i][j] = 2
                blue++
            }

        }
    }

    if(state[x][y] != 0) {
        return false;
    }

    if(red == blue) {
        state[x][y] = 1; // Red
    } else {
        state[x][y] = 2; // Blue 
    } 

    let thisUrl = new URL(window.location.href);
    let setStateUrl = new URL(window.location.protocol + "//" + window.location.host + "/tictactoe/setState");
    setStateUrl.searchParams.append("gameId", thisUrl.searchParams.get("gameId"));
    setStateUrl.searchParams.append("state", JSON.stringify(state)); 

    fetch(setStateUrl.toString())  
    .then((response) => {
        return response.json();  
    })
    .then((data) => { 
       let newStateId = data["stateId"]; // Get the stateUI after setting the state. 
       let stateUIUrl = new URL(window.location.protocol + "//" + window.location.host + "/tictactoe/getStateUIUrl"); // URL to getStateUIUrl
       stateUIUrl.searchParams.append("gameId", thisUrl.searchParams.get("gameId")); // Add parameters for getStateUIUrl
       stateUIUrl.searchParams.append("stateId", newStateId);

       window.location.href = stateUIUrl; // Redirect to getStateUIUrl
    })
    .catch(error => console.log(error));

}