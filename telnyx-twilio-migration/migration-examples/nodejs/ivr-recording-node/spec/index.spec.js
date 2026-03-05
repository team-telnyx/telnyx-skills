'use strict';

const supertest = require('supertest');
const app = require('../app.js');

describe('home', function() {
  describe('GET /', function() {
    it('redirects to /agents', function(done) {
      const agent = supertest(app);
      agent
        .get('/')
        .expect('location', '/agents')
        .expect(302, done);
    });
  });
});
