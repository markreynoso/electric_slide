'use strict'


let solutionList, startingState;

function greedySolve() {
    $.get({
        url: '/api/solve/greedy',
        data: {'state': JSON.stringify(startingState)},
        success: function(data) {
            solutionList = data['solution']
            console.log(solutionList)
            timer();
        }
    });
}


function astarSolve() {
    $.get({
        url: '/api/solve/astar',
        data: {'state': JSON.stringify(startingState)},
        success: function(data) {
            solutionList = data['solution']
            console.log(solutionList)
            timer();
        }
    });
}


function treeSolve() {
    $.get({
        url: '/api/solve/tree',
        data: {'state': JSON.stringify(startingState)},
        success: function(data) {
            solutionList = data['solution']
            console.log(solutionList)
            timer();
        }
    });
}


function shuffle() {
    $.get('/api/shuffle', function(data) {
        startingState = data['shuffle']
        startBoard(startingState);
        console.log(startingState);
    }).then(console.log(startingState));
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


function solveBoard(interval) {
    if (solutionList.length > 1) {
        solutionList.shift()
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                $("div").find("[data-coords='" + solutionList[0][i][j] + "']").attr('id', '' + i + j)
            }
        }
    } else {
        clearInterval(interval)
    }
}

// startBoard(startingState);
startBoard([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);


$('#shuffle-button').on('click', function() {
    shuffle();
});

$('#astar-button').on('click', function() {
    astarSolve();
});

$('#greedy-button').on('click', function() {
    greedySolve();
});

$('#tree-button').on('click', function() {
    treeSolve();
});