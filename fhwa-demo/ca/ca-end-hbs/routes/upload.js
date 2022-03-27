const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');

const NavLinkService = require('../services/NavLinkService');
const navLinkService = new NavLinkService();

router.get('/', async function (req, res, next) {
    res.render('upload');
    //res.redirect('/revocation');
});

module.exports = router;