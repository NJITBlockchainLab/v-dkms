var sdk = require('indy-sdk');


const express = require('express');
const router = express.Router();
const { body, validationResult } = require('express-validator');

const NavLinkService = require('../services/NavLinkService');
const navLinkService = new NavLinkService();
navLinkService.registerCustomLinks([
    // { "label": "My Schemas", "url": "/issuing/my-schemas"},
    // { "label": "Create Schema", "url": "/issuing/create-schema" },
    // { "label": "Create Credential Definition", "url": "/issuing/create-credential-definition" },
    // { "label": "Issue Credential", "url": "/issuing/issue-credential" },
]);

router.use(function (req, res, next) {
    navLinkService.clearLinkClasses();
    navLinkService.setNavLinkActive('/issuing');
    next();
});

router.get('/', async function (req, res, next) {
    res.redirect('/issuing');
})

router.get('/createdSchemas', async function (req, res, next) {
    const agentService = require('../services/AgentService');
    const allMySchemas = await agentService.getMyCreatedSchemas();

    navLinkService.setCustomNavLinkActive('/issuing/');
    res.render('issuing', {
        navLinks: navLinkService.getNavLinks(),
        customNavLinks: navLinkService.getCustomNavLinks(),
        allMySchemas
    });
});



// async function handleNewSchema(req, res, next) {
//     const agentService = require('../services/AgentService');
    
//     const schema = await agentService.sendNewSchema();
//     if (schema) {
//         schema.shema = JSON.stringify(schema.schema);
//     }
//     req.schema = schema
//     next();
// }

module.exports = router;