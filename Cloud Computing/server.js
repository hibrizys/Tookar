const express = require('express');
const userHandler = require('./controller/search');

const bodyParser = require('body-parser');
const session = require('express-session');

const app = express();
const port = 8080;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Define your API endpoints using the router
app.get('/', (req, res) => {
    const response = {
        message: 'Hello from the API!'
    };
    res.json(response);
});
// ADD ALL DATA
app.post('/api/add', userHandler.addAll);

// SEE ALL DATA
app.get('/api/allData', userHandler.seeAll);

// POST
app.post('/api/search/id', userHandler.searchID);
app.post('/api/search/kota', userHandler.searchKota);
app.post('/api/search/barang', userHandler.searchBarang);

// GET
app.get('/api/getID', userHandler.getID);
app.get('/api/getKota/:kota', userHandler.getKota);
app.get('/api/getBarang', userHandler.getBarang);

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});