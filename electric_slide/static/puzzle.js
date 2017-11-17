'use strict'


let solutionGreedy, solutionAstar, solutionTree;
let startingState = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

function greedySolve() {
    $('.greedy-loader').show()
    $.get({
        url: '/api/solve/greedy',
        data: {'state': JSON.stringify(startingState)},
        success: function(data) {
            solutionGreedy = data['solution']
            console.log(solutionGreedy)
            $('.greedy-loader').hide()
            greedyTimer();
        }
    });
}


function astarSolve() {
    $('.astar-loader').show()
    $.get({
        url: '/api/solve/astar',
        data: {'state': JSON.stringify(startingState)},
        success: function(data) {
            solutionAstar = data['solution']
            console.log(solutionAstar)
            $('.astar-loader').hide()
            astarTimer();
        }
    });
}


function treeSolve() {
    $('.tree-loader').show()
    $.get({
        url: '/api/solve/tree',
        data: {'state': JSON.stringify(startingState)},
        success: function(data) {
            solutionTree = data['solution']
            console.log(solutionTree)
            $('.tree-loader').hide()
            treeTimer();
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
            $("div").find("[data-coords='" + state[i][j] + "']").attr('coords', '' + i + j)
        }
    }
}


function greedyTimer() {
    let interval = setInterval(function() {solveGreedy(interval)}, 100);
}


function astarTimer() {
    let interval = setInterval(function() {solveAstar(interval)}, 100);
}


function treeTimer() {
    let interval = setInterval(function() {solveTree(interval)}, 100);
}


function solveGreedy(interval) {
    if (solutionGreedy.length > 1) {
        solutionGreedy.shift()
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                $(".greedy").find("[data-coords='" + solutionGreedy[0][i][j] + "']").attr('coords', '' + i + j)
            }
        }
    } else {
        clearInterval(interval)
    }
}


function solveAstar(interval) {
    if (solutionAstar.length > 1) {
        solutionAstar.shift()
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                $(".astar").find("[data-coords='" + solutionAstar[0][i][j] + "']").attr('coords', '' + i + j)
            }
        }
    } else {
        clearInterval(interval)
    }
}


function solveTree(interval) {
    if (solutionTree.length > 1) {
        solutionTree.shift()
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                $(".tree").find("[data-coords='" + solutionTree[0][i][j] + "']").attr('coords', '' + i + j)
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

$('#all-button').on('click', function() {
    astarSolve();
    treeSolve();
    greedySolve();
});