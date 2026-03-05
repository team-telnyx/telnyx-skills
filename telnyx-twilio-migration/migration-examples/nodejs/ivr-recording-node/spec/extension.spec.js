'use strict';

require('./connectionHelper');

const expect = require('chai').expect;
const supertest = require('supertest');
const cheerio = require('cheerio');
const app = require('../app.js');
const Agent = require('../models/agent');

describe('extension', function() {
  describe('POST /extension/connect', function() {
    let brodo = {}; // Agent reference

    before(function(done) {
      Agent.create({extension: 'Brodo', phoneNumber: '555 5555'})
        .then(function(agent) {
          brodo = agent;
          done();
        });
    });

    after(function(done) {
      Agent.remove({}, done);
    });

    context('when there is an agent for a given extension', function() {
      it('responds with return instructions', function(done) {
        const agent = supertest(app);
        agent
          .post('/extension/connect')
          .send({Digits: 2})
          .set('X-Twilio-Signature', ['foo'])
          .expect(function(res) {
            const $ = cheerio.load(res.text);
            expect($('Say').length).to.equal(1);
            expect($('Dial').first().attr('action'))
              .to.equal('/agents/call?agentId=' + brodo.id);
            expect($('Dial').first().text()).to.equal('555 5555');
            expect($('Dial').children().first().attr('url'))
              .to.equal('/agents/screencall');
          })
        .expect(200)
        .end(done);
      });
    });

    context('when there is not an agent for a given extension', function() {
      it('response contains redirect to menu', function(done) {
        const agent = supertest(app);
        agent
          .post('/extension/connect')
          .send({Digits: 0})
          .set('X-Twilio-Signature', ['foo'])
          .expect(function(res) {
            const $ = cheerio.load(res.text);
            expect($('Redirect').first().text()).to.equal('/ivr/welcome');
          })
        .expect(200)
        .end(done);
      });
    });
  });
});
