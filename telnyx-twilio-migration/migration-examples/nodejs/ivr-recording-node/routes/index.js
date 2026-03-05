'use strict';

const express = require('express');
const router = new express.Router();

// GET: /
router.get('/', function(req, res, next) {
  res.redirect('/agents');
});

module.exports = router;
