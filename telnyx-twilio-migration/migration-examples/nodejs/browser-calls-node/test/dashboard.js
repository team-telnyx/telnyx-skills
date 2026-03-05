const connectionHelper = require('./connectionHelper');

const expect = require('chai').expect
const supertest = require('supertest')
const app = require('../app.js')
const Ticket = require('../models/ticket');

describe('dashboard', function () {
  before(async () => {
    await connectionHelper.connect();

    await Ticket.create(
      { 
        name: 'Ticket',
        phoneNumber: '+567899043',
        description: 'A simple ticket',
        createdAt : new Date()
      }
    );
  });

  after(async () => await connectionHelper.clearDatabase());

  describe('GET /dashboard', function () {
    it('list all tickets', function (done) {
      var agent = supertest(app);
      agent
        .get('/dashboard')
        .expect(function (response) {
          expect(response.text).to.contain('Tickets');
          expect(response.text).to.contain('+567899043');
          expect(response.text).to.contain('A simple ticket');
        })
        .expect(200, done);
    });
  });
});
