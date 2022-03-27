var createError = require('http-errors');
const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const { engine } = require('express-handlebars');
const helpers = require('handlebars-helpers');
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');
const fs = require('fs');



//enable CORS requests
const cors = require('cors');

//import ipfs-http-client
const { create } = require('ipfs-http-client');

const indexRouter = require('./routes/index');
const connectionRouter = require('./routes/connection');
const proofRouter = require('./routes/proof');
const revocationRouter = require('./routes/revocation');
const uploadRouter = require('./routes/upload');
const app = express();


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');
app.engine('hbs', engine({
  extname: 'hbs',
  defaultView: 'default',
  layoutsDir: path.join(__dirname, '/views/layouts/'),
  partialsDir: [
    path.join(__dirname, '/views/partials'),
    path.join(__dirname, '/views/partials/connection'),
    path.join(__dirname, '/views/partials/home'),
    path.join(__dirname, '/views/partials/proof'),
    path.join(__dirname, '/views/partials/revocation')

  ],
  helpers: helpers(['array', 'comparison'])
}));

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({extended:true}));
app.use(fileUpload());


app.use('/', indexRouter);
app.use('/connections', connectionRouter);
app.use('/proofs', proofRouter);
app.use('/revocation', revocationRouter);
app.use('/upload', uploadRouter);

//initialize cors
app.use(cors({
  origin: '*',
  optionsSuccessStatus: 200
}));
var allowCrossDomain = function(req, res, next) {
  res.header('Access-Control-Allow-Origin', "*");
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
}

app.use(allowCrossDomain);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
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

async function saveText(){
  let ipfs = await ipfsClient();

  let result = await ipfs.add("hello");
  console.log(result);
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

//saveFile();


// app.post('/upload', (req,res) => {
//   const file = req.files.file;
//   const fileName = req.body.fileName;
//   const filePath = 'files/' + fileName;

//   //upload file onto server
//   file.mv(filePath, async (err) => {
//     if (err) {
//       console.log('Error: failed to upload');
//       return res.status(500).send(err);
//     }

//     const fileHash = await addFile(fileName, filePath);
//     fs.unlink(filePath, (err) => {
//       if (err) console.log(err);
//     });
//     //res.redirect('/revocation');
//     console.log('fileName: '+ fileName);
//     console.log('fileHash: '+fileHash);
//     res.render('/upload/', {fileName, fileHash});
//   })
// });

const addFile = async (fileName, filePath) => {
  //file buffer
  const file = fs.readFileSync(filepath);

  const fileAdded = await ipfs.add({path: fileName, content: file});
  const fileHash = fileAdded[0].hash;

  return fileHash;
}


module.exports = app;
