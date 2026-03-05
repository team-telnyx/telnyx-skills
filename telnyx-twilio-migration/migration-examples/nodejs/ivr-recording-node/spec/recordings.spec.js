'use strict';

const expect = require('chai').expect;
const supertest = require('supertest');
const Agent = require('../models/agent');

const app = require('../app.js');

describe('recordings', function() {
  describe('POST /recordings', function() {
    let brodo = {}; // Agent reference

    before(function(done) {
      Agent.create({extension: '123', phoneNumber: '555 5555'})
      .then(function(agent) {
        brodo = agent;
        done();
      });
    });

    after(function(done) {
      Agent.remove({}, done);
    });

    it('creates a new recording', function(done) {
      const agent = supertest(app);
      agent
      .post('/recordings?agentId=' + brodo.id)
      .send({
        From: '555 5556',
        TranscriptionText: 'I am homesick',
        RecordingUrl: 'http://example.com/brd.mpe',
      })
      .expect(201)
      .expect(function(res) {
        Agent.findOne({}, function(err, agent) {
          expect(agent.recordings.length).to.equal(1);
        });
      })
      .end(function(err, res) {
        if (err) {
          throw err;
        }

        done();
      });
    });
  });
});
