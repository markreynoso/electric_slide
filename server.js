'use strict';

const EXPRESS = require('express');
const APP = EXPRESS();
const PORT = process.env.PORT || 3000;
const requestProxy = require('express-request-proxy');

APP.use(EXPRESS.static('startbootstrap-business-casual/vendor'));

APP.get('/', function(request, response){
  response.sendFile('index.html', {root: 'startbootstrap-business-casual/vendor'});
})
// APP.get('/portfolio', function(request, response){
//   response.sendFile('index.html', {root: './public'});
// })
// APP.get('/experience', function(request, response){
//   response.sendFile('index.html', {root: './public'});
// })
// APP.get('/github/*', sendTheGit);

APP.get('*', function(request, response){
  response.sendFile('404.html', {root: './public'});
})

APP.listen(PORT, function(){
  console.log(`Express server currently running on port ${PORT}`);
})

// function sendTheGit(request, response) {
//   (requestProxy({
//     url: `https://api.github.com/${request.params[0]}`,
//     headers: {
//       Authorization: `token ${process.env.GITHUB_TOKEN}`
//     }
//   }))(request, response);
// }