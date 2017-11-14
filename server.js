'use strict';

const EXPRESS = require('express');
const APP = EXPRESS();
const PORT = process.env.PORT || 3000;
const requestProxy = require('express-request-proxy');

APP.use(EXPRESS.static('startbootstrap-business-casual/'));

APP.get('/', function(request, response){
  response.sendFile('index.html', {root: 'startbootstrap-business-casual/'});
})

APP.listen(PORT, function(){
  console.log(`Express server currently running on port ${PORT}`);
})