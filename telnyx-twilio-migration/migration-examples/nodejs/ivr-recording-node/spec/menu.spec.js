'use strict';

const expect = require('chai').expect;
const supertest = require('supertest');
const cheerio = require('cheerio');
const app = require('../app.js');

describe('menu', function() {
  describe('GET /menu', function() {
    context('when the selected option is 1', function() {
      it('responds with return instructions', function(done) {
        const agent = supertest(app);
        agent
        .post('/menu')
        .send({Digits: 1})
        .set('X-Twilio-Signature', ['foo'])
        .expect(function(res) {
          const $ = cheerio.load(res.text);
          expect($('Say').length).to.equal(2);
          expect($('Hangup').length).to.equal(1);
        })
        .expect(200, done);
      });
    });

    context('when the selected option is 2', function() {
      it('responds with planet instructions', function(done) {
        const agent = supertest(app);
        agent
        .post('/menu')
        .send({Digits: 2})
        .set('X-Twilio-Signature', ['foo'])
        .expect(function(res) {
          const $ = cheerio.load(res.text);
          expect($('Gather').first().attr('action'))
            .to.equal('/extension/connect');
          expect($('Gather').children('Say').length).to.equal(1);
        })
        .expect(200, done);
      });
    });

    context('when the selected option is not 1 or 2', function() {
      it('redirects to /ivr/welcome', function(done) {
        const agent = supertest(app);
        agent
        .post('/menu')
        .send({Digits: 3})
        .set('X-Twilio-Signature', ['foo'])
        .expect(function(res) {
          const $ = cheerio.load(res.text);
          expect($('Redirect').first().text()).to.equal('/ivr/welcome');
        })
        .expect(200, done);
      });
    });
  });
});
