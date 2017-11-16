'use strict'


var solutionList = [[[6, 4, 7], [8, 5, 9], [3, 2, 1]], [[6, 4, 9], [8, 5, 7], [3, 2, 1]], [[6, 9, 4], [8, 5, 7], [3, 2, 1]], [[6, 5, 4], [8, 9, 7], [3, 2, 1]], [[6, 5, 4], [9, 8, 7], [3, 2, 1]], [[6, 5, 4], [3, 8, 7], [9, 2, 1]], [[6, 5, 4], [3, 8, 7], [2, 9, 1]], [[6, 5, 4], [3, 8, 7], [2, 1, 9]], [[6, 5, 4], [3, 8, 9], [2, 1, 7]], [[6, 5, 4], [3, 9, 8], [2, 1, 7]], [[6, 9, 4], [3, 5, 8], [2, 1, 7]], [[9, 6, 4], [3, 5, 8], [2, 1, 7]], [[3, 6, 4], [9, 5, 8], [2, 1, 7]], [[3, 6, 4], [2, 5, 8], [9, 1, 7]], [[3, 6, 4], [2, 5, 8], [1, 9, 7]], [[3, 6, 4], [2, 5, 8], [1, 7, 9]], [[3, 6, 4], [2, 5, 9], [1, 7, 8]], [[3, 6, 9], [2, 5, 4], [1, 7, 8]], [[3, 9, 6], [2, 5, 4], [1, 7, 8]], [[9, 3, 6], [2, 5, 4], [1, 7, 8]], [[2, 3, 6], [9, 5, 4], [1, 7, 8]], [[2, 3, 6], [1, 5, 4], [9, 7, 8]], [[2, 3, 6], [1, 5, 4], [7, 9, 8]], [[2, 3, 6], [1, 9, 4], [7, 5, 8]], [[2, 3, 6], [1, 4, 9], [7, 5, 8]], [[2, 3, 9], [1, 4, 6], [7, 5, 8]], [[2, 9, 3], [1, 4, 6], [7, 5, 8]], [[9, 2, 3], [1, 4, 6], [7, 5, 8]], [[1, 2, 3], [9, 4, 6], [7, 5, 8]], [[1, 2, 3], [4, 9, 6], [7, 5, 8]], [[1, 2, 3], [4, 5, 6], [7, 9, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
var startingState;

function greedySolve() {
    solutionList = $ajax(get, greedy(current_state))
    solveBoard()
}


function astarSolve() {

}


function treeSolve() {

}


function shuffle() {
    $.get('/api/shuffle', function(data) {
        startingState = data['shuffle']
        startBoard(data['shuffle']);
    });
}


function startBoard(state){
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            $("div").find("[data-coords='" + state[i][j] + "']").attr('id', '' + i + j)
        }
    }
}


function timer() {
    let interval = setInterval(function() {solveBoard(interval)}, 100);
}


function solveBoard() {
    if (solutionList.length > 1) {
        solutionList.shift()
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                $("div").find("[data-coords='" + solutionList[0][i][j] + "']").attr('id', '' + i + j)
            }
        }
    }
}

// startBoard(startingState);
startBoard([[6, 4, 7], [8, 5, 9], [3, 2, 1]]);

$('#puzzle-container').one('click', function() {
    timer();
});

$('#shuffle-button').on('click', function() {
    shuffle();
});