'use strict'

$('#one').on('click', swap);

function swap(){
    $('#one').css('left', '125px')
    $('#two').css('left', '0px')
}

function startBoard(state){
    for (var i = 0; i < 3; i++){
        for (var j = 0; j < 3; j++){
            $(`[data-coords= ${i} + ',' + ${j}]`).find('span').text(state[i][j])
            // $('.tile').data('coords')
        }
    }    
}

startBoard([[2, 5, 7], [1, 9, 6], [3, 4, 8]])