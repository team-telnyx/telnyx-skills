
const expect = require('chai').expect
const supertest = require('supertest')
const cheerio = require('cheerio');

const app = require('../app.js');

describe('call', function () {
  describe('POST to /call/connect', function () {
    context('when connecting from a phone number', function () {
      it('response verb DIAL and a phone number', function (done) {
        var phoneNumber = '555 5555'

        var agent = supertest(app);
        agent
        .post('/call/connect')
        .send({
          phoneNumber: phoneNumber,
        })
        .expect(function (res) {
          var $ = cheerio.load(res.text);
          expect($('Dial').children('Number').length).to.equal(1);
          expect($('Dial').children('Number').text()).to.equal(phoneNumber);
        })
        .expect(200, done);
      });
    });

    context('when connecting from an agent', function () {
      it('response noun CLIENT and the text support-agent', function (done) {

        var agent = supertest(app);
        agent
        .post('/call/connect')
        .expect(function (res) {
          var $ = cheerio.load(res.text);
          expect($('Dial').children('Client').length).to.equal(1);
          expect($('Dial').children('Client').text()).to.equal("support_agent");
        })
        .expect(200, done);
      });
    });
  });
});
