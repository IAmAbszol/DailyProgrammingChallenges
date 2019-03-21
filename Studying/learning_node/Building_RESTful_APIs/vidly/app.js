const Joi = require('joi');
const express = require('express');
const app = express();

app.use(express.json());

const genres = [
    {id: 1, genre: 'Action'}
];

function validateGenres(genre) {
    const schema = {
        genre: Joi.string().min(3).required()
    };
    return Joi.validate(genre, schema);
}

app.get('/api/genres', (req, res) => {
    res.send(genres);
});

app.post('/api/genres', (req, res) => {
    const {error}  = validateGenres(req.body);
    if (error) {
        res.status(400).send(error.details[0].message);
        return;
    }
    const genre = {
        id : genres.length + 1,
        genre : req.body.genre
    };
    genres.push(genre);
    res.send(genre);
});

app.put('/api/genres/:id', (req, res) => {
    const genre = genres.find(g => g.id == parseInt(req.params.id));
    if (!genre) {
        res.status(404).send('Genre not available.');
        return;
    }
    const {error}  = validateGenres(req.body);
    if (error) {
        res.status(400).send(error.details[0].message);
        return;
    }
    genre.genre = req.body.genre;
    res.send(genre);
});

app.delete('/api/genres/:id', (req, res) => {
    const genre = genres.find(g => g.id == parseInt(req.params.id));
    if (!genre) {
        res.status(404).send('Genre not available.');
        return;
    }
    const index = genres.indexOf(genre);
    genres.splice(index, 1);
    res.send(genre);
});

app.get('/api/genres/:id', (req, res) => {
    const genre = genres.find(g => g.id == parseInt(req.params.id));
    if (!genre) {
        res.status(404).send('Genre not available.');
        return;
    }
    res.send(genre);
});

// Setup basic port
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Listening on port ${port}.`);
});