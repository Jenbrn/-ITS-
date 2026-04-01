
import express from 'express';
import catalogoLibri from './model/catalogo.js';
import clienteFile from './model/clienti.js';
import bodyParser from 'body-parser';

const app = express();
app.use(bodyParser.json());
const PORT = 3000;
const BASE_PATH = "/api/v1";

 
//ar catalogo = catalogoLibri;
//var clienti = clienteFile;
var catalogo = [...catalogoLibri];
var clienti = [...clienteFile];
// creo una shallow copy dell'array clieni - libri per poterli modificare. prende 

// avvio il server
app.listen(PORT, () => {
    console.log ("server attivo sulla porta " + PORT);
});

//endpoint che restituisce un endpoint 
app.get("/", (req, res) => {
    res.send("Benvenuto nella tua libreria online");
});

// endpoint per recuperare l'elenco fdei cataloghi libri. basta mod il path, non serve aggiornare le variabili
//app.get(BASE_PATH + "/libri", (req, res) => {
//    res.json(catalogo);
//});
// di seguito versione ottimizzata: meglio perchè non concatena due comendi ma li rende un'unica str
// e lo rende un'unico path anche concatenando più req 
app.get(`${BASE_PATH}/libri`, (req, res) => {
    res.json(catalogo);
});


// endpoint per recuperare l'elenco dei clienti
app.get(BASE_PATH + "/clienti", (req, res) => {
    res.json(clienti);
}); 

//recupera libro per titolo: /v1/catalogo/search?titolo=restful
//il path search va posizionato prima
app.get(`${BASE_PATH}/libri/search`, (req, res) =>{
    //recupero il parametro dall'url + pulizia
    let titoloParam = (req.query.titolo || "").toString().trim().toLowerCase();

    //se non c'è il parametro, restituisco stato 400(Bad Req)
    if (!titoloParam) return res.status(400).json({ error: "Parametro 'titolo' errato"});

    let results = catalogo.findLast(libro => libro.titolo.toLocaleLowerCase().includes(titoloParam));

    return res.json(results);
}

);

//ricerca con id
// let indica una vaiabile con visibilità interna a funz corrente
app.get(`${BASE_PATH}/libri/:id`, (req, res) => {
    let idParam = parseInt(req.params.id);

    let libroTrovato = catalogo.find(libro => libro.id === idParam);

    if (!libroTrovato) {
        return res.status(404).json({ error: "Libro non trovato"});
    } else {
        return res.json(libroTrovato);
    }

});

//necessita npm install body-parser
app.post(`${BASE_PATH}/libri`, (req, res) => {
    const nuovoLibro = req.body;

    if (!nuovoLibro) {
        return res.status(400).json({ error: "Nessun dato fornito" });
    }

    catalogo.push(nuovoLibro);
    return res.status(201).json({ message: "Libro aggiuntocon successo" });


});



//app.get(`$`)
//app.get(`$`)