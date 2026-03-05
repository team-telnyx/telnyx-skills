'use strict';

const expect = require('chai').expect;
const supertest = require('supertest');
const cheerio = require('cheerio');

const app = require('../app.js');

describe('ivr', function() {
  describe('GET /ivr/welcome', function() {
    it('response contains Gather', function(done) {
      const agent = supertest(app);
      agent
      .post('/ivr/welcome')
      .set('X-Twilio-Signature', ['foo'])
      .expect(function(res) {
        const $ = cheerio.load(res.text);
        expect($('Gather').children('Play').length).to.equal(1);
        expect($('Gather').first().attr('action'))
          .to.equal('/menu');
      })
      .expect(200, done);
    });
  });
});
