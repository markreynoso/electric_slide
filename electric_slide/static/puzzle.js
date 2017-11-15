'use strict'

var solutionList = [[[6, 4, 7], [8, 5, 9], [3, 2, 1]], [[6, 4, 9], [8, 5, 7], [3, 2, 1]], [[6, 9, 4], [8, 5, 7], [3, 2, 1]], [[6, 5, 4], [8, 9, 7], [3, 2, 1]], [[6, 5, 4], [9, 8, 7], [3, 2, 1]], [[6, 5, 4], [3, 8, 7], [9, 2, 1]], [[6, 5, 4], [3, 8, 7], [2, 9, 1]], [[6, 5, 4], [3, 8, 7], [2, 1, 9]], [[6, 5, 4], [3, 8, 9], [2, 1, 7]], [[6, 5, 4], [3, 9, 8], [2, 1, 7]], [[6, 9, 4], [3, 5, 8], [2, 1, 7]], [[9, 6, 4], [3, 5, 8], [2, 1, 7]], [[3, 6, 4], [9, 5, 8], [2, 1, 7]], [[3, 6, 4], [2, 5, 8], [9, 1, 7]], [[3, 6, 4], [2, 5, 8], [1, 9, 7]], [[3, 6, 4], [2, 5, 8], [1, 7, 9]], [[3, 6, 4], [2, 5, 9], [1, 7, 8]], [[3, 6, 9], [2, 5, 4], [1, 7, 8]], [[3, 9, 6], [2, 5, 4], [1, 7, 8]], [[9, 3, 6], [2, 5, 4], [1, 7, 8]], [[2, 3, 6], [9, 5, 4], [1, 7, 8]], [[2, 3, 6], [1, 5, 4], [9, 7, 8]], [[2, 3, 6], [1, 5, 4], [7, 9, 8]], [[2, 3, 6], [1, 9, 4], [7, 5, 8]], [[2, 3, 6], [1, 4, 9], [7, 5, 8]], [[2, 3, 9], [1, 4, 6], [7, 5, 8]], [[2, 9, 3], [1, 4, 6], [7, 5, 8]], [[9, 2, 3], [1, 4, 6], [7, 5, 8]], [[1, 2, 3], [9, 4, 6], [7, 5, 8]], [[1, 2, 3], [4, 9, 6], [7, 5, 8]], [[1, 2, 3], [4, 5, 6], [7, 9, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

// $('#one').on('click', swap);
$('#puzzle-container').on('click', solveBoard)

function swap(){
    $('#one').css('left', '125px')
    $('#two').css('left', '0px')
}

function startBoard(state){
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            $("div").find("[data-coords='" + i + ',' + j + "']").text(state[i][j]);
        }
    }
}

function solveBoard() {
    // for (var i = 0; i < solutionList.length; i++) {
        startBoard(solutionList.shift())
    // }
}


startBoard([[6, 4, 7], [8, 5, 9], [3, 2, 1]])
// solveBoard(
//     [[[6, 4, 7], [8, 5, 9], [3, 2, 1]], [[6, 4, 9], [8, 5, 7], [3, 2, 1]], [[6, 9, 4], [8, 5, 7], [3, 2, 1]], [[6, 5, 4], [8, 9, 7], [3, 2, 1]], [[6, 5, 4], [9, 8, 7], [3, 2, 1]], [[6, 5, 4], [3, 8, 7], [9, 2, 1]], [[6, 5, 4], [3, 8, 7], [2, 9, 1]], [[6, 5, 4], [3, 8, 7], [2, 1, 9]], [[6, 5, 4], [3, 8, 9], [2, 1, 7]], [[6, 5, 4], [3, 9, 8], [2, 1, 7]], [[6, 9, 4], [3, 5, 8], [2, 1, 7]], [[9, 6, 4], [3, 5, 8], [2, 1, 7]], [[3, 6, 4], [9, 5, 8], [2, 1, 7]], [[3, 6, 4], [2, 5, 8], [9, 1, 7]], [[3, 6, 4], [2, 5, 8], [1, 9, 7]], [[3, 6, 4], [2, 5, 8], [1, 7, 9]], [[3, 6, 4], [2, 5, 9], [1, 7, 8]], [[3, 6, 9], [2, 5, 4], [1, 7, 8]], [[3, 9, 6], [2, 5, 4], [1, 7, 8]], [[9, 3, 6], [2, 5, 4], [1, 7, 8]], [[2, 3, 6], [9, 5, 4], [1, 7, 8]], [[2, 3, 6], [1, 5, 4], [9, 7, 8]], [[2, 3, 6], [1, 5, 4], [7, 9, 8]], [[2, 3, 6], [1, 9, 4], [7, 5, 8]], [[2, 3, 6], [1, 4, 9], [7, 5, 8]], [[2, 3, 9], [1, 4, 6], [7, 5, 8]], [[2, 9, 3], [1, 4, 6], [7, 5, 8]], [[9, 2, 3], [1, 4, 6], [7, 5, 8]], [[1, 2, 3], [9, 4, 6], [7, 5, 8]], [[1, 2, 3], [4, 9, 6], [7, 5, 8]], [[1, 2, 3], [4, 5, 6], [7, 9, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

// )