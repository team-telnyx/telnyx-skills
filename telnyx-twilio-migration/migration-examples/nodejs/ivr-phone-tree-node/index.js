const app = require('./app');
const config = require('./config');

const server = app.listen(config.port, function() {
  console.log('Express server listening on port ' + server.address().port);
});

module.exports = server;
