const util = require('util');
const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');
const NavLinkService = require('../services/NavLinkService');
const navLinkService = new NavLinkService();
const cors = require('cors');
const path = require('path');
const bodyParser = require('body-parser');
const multiparty = require('multiparty');
const { create } = require('ipfs-http-client');
const indy = require('indy-sdk');
const utils = require("./utils");
const os = require('os');
const alert = require('alert');

navLinkService.registerCustomLinks([
    // { "label": "Revocation", "url": "/revocation" },
]);

const fileUpload = require('express-fileupload');
const fs = require('fs');
const mv = require('mv');
const { jar } = require('request');

router.use(express.urlencoded({extended:true}));
router.use(fileUpload());
router.use(bodyParser.json());
router.use(bodyParser.urlencoded({ extended: true }));


router.use(function (req, res, next) {
    navLinkService.clearLinkClasses();
    navLinkService.setNavLinkActive('/revocation');
    next();
});

router.get('/', async function (req, res, next) {
    res.render('revocation', {
      navLinks: navLinkService.getNavLinks(),
    });
 });

//connect to ipfs node
//const ipfs = new ipfsClient({host: 'localhost', port:'5001',protocol:'http'});
async function ipfsClient() {
    const ipfs = await create(
      {
      host: "ipfs.infura.io",
      port: 5001,
      protocol: "https"
      }
    );
    return ipfs
}
  

//saveText();
let data = {
name: "test",
version: "1.0"
}

async function saveFile(formData){


let ipfs = await ipfsClient();

let result = await ipfs.add({path: "crl.json",content:JSON.stringify(data)});
console.log(result);
}

//get pool handle
const poolName = 'sandbox';
async function getPoolHandle(poolName){
    //create pool ledger config
    const genesisFilePath = "/home/nico/von-network/genesis/iiw_demo_genesis.txt"
    const poolConfig = JSON.stringify({'genesis_txn': genesisFilePath})
    await indy.createPoolLedgerConfig(poolName, null)

    //get pool handle
    const poolHandle = await indy.openPoolLedger(poolName,null);
    console.log(poolHandle);
}
//getPoolHandle(poolName);


//get wallet handle
const walletName = {"id": "CAEnd"};
const walletCredentials = {"key":"walletkey1"};
async function getWalletHandle(walletName, walletCredentials){
    const walletHandle = await indy.openWallet(walletName, walletCredentials);
    //console.log(walletHandle);
    return walletHandle;
}
//getWalletHandle(walletName, walletCredentials);

router.post('/upload', (req,res) => {
    //req in JSON
    //console.log(req.body);
    
    sendNewCrl = req.body;
    //console.log(sendNewCRL);

    const uploadNewCrl = async () => {
        try
        {
            const ipfs = await ipfsClient();
            const result = await ipfs.add(JSON.stringify(sendNewCrl));
            //console.log(result);
            alert(result["path"]);
        } catch {
            console.log("upload failed");
        }

    };

    
    async function getNewCrlHash(){
        //var crlHash = await uploadNewCrl();
        uploadNewCrl().then(data => {
            return data;
        }).catch(err => {
            console.log(err);
        })
    };
    newCRLIpfsHash = getNewCrlHash();
    //console.log(newCRLIpfsHash);

    //need my DID to build transaction

    // Open wallet and get handle from libindy
    // const walletHandle = await indy.openWallet(walletName, walletCredentials)

    // Building NYM request to add Trust Anchor to the ledger
    // const attribRequest = buildAttribRequest ( 'W1nqK2fiZn3KUivUuVSQjA', 'W1nqK2fiZn3KUivUuVSQjA', {"CRL":newCRLIpfsHash});

});

const addFile = async (fileName, filePath) => {
//file buffer
    const file = fs.readFileSync(filePath);

    const fileAdded = await ipfs.add({path: fileName, content: file});
    const fileHash = fileAdded[0].hash;

    return fileHash;
}

module.exports = router;