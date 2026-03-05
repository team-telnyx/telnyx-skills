db.dropDatabase();

const agents = [
  {extension: 'Brodo', phoneNumber: '+15552483591'},
  {extension: 'Dagobah', phoneNumber: '+15558675309'},
  {extension: 'Oober', phoneNumber: '+15553185602'},
];

db.agents.insert(agents);
