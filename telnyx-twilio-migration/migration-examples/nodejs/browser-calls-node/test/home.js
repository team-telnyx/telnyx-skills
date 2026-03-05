const expect = require('chai').expect
const supertest = require('supertest')
const app = require('../app.js');

describe('home', function () {
  describe('GET /', function () {
    it('respond with ok', function (done) {
      var agent = supertest(app);
      agent
        .get('/')
        .expect(function (response) {
          expect(response.text).to.contain('Submit ticket');
        })
        .expect(200, done);
    });
  });

  describe('GET /home', function () {
    it('respond with ok', function (done) {
      var agent = supertest(app);
      agent
        .get('/home')
        .expect(function (response) {
          expect(response.text).to.contain('Submit ticket');
        })
        .expect(200, done);
    });
  });
});
