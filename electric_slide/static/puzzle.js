'use strict'

$('#one').on('click', swap);

function swap(){
    $('#one').css('left', '125px');
    $('#two').css('left', '0px')
}