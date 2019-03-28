const config = require('config');
const helmet = require('helmet');
const morgan = require('morgan');
const Joi = require('joi');
const logger = require('./logger');
const auth = require('./auth');
const express = require('express');
const app = express();

// Internally loads pug module
app.set('view engine', 'pug');
app.set('views', './views'); // default is views directory, should be in root.

// Parses body of request --> populates req.body property.
app.use(express.json());
// Can parse url of kv pairs
app.use(express.urlencoded({ extended: true })); // Key=value&key=value
// Served by the root of the webpage/site
app.use(express.static('public'));
app.use(helmet());

// Configuration
console.log('Application name: ' + config.get('name'));
console.log('Application mail server: ' + config.get('mail.host'));
console.log('Application mail server password: ' + config.get('mail.password'));

// Default is development --> export NODE_ENV=PRODUCTION to set other.
if (app.get('env') == 'development') {
    app.use(morgan('tiny'));
    console.log('Morgan has been enabled.');
}

app.use(logger);
app.use(auth.auth);

const courses = [
    { id: 1, name: 'course1' },
    { id: 2, name: 'course2' },
    { id: 3, name: 'course3' }
];

// Request and response to lambda
app.get('/', (req, res) => {
    res.render('index', {title: 'Hello', message: 'Pug is cool.'});
});

app.get('/api/courses', (req, res) => {
    res.send(courses);
});

app.post('/api/courses', (req, res) => {

    const { error } = validateCourse(req.body);
    if (error) {
        res.status(400).send(error.details[0].message);
        return;
    }

    const course = {
        id: courses.length + 1,
        name: req.body.name
    };
    courses.push(course);
    res.send(course);
});

app.put('/api/courses/:id', (req, res) => {
    // Look up the course
    // If not existing, return 404
    const course = courses.find(c => c.id == parseInt(req.params.id));
    if (!course) {
        res.status(404).send('Not here my guy.');
        return;
    }
    // Validate
    // If invalid, return 400 - Bad request
    const { error } = validateCourse(req.body);
    if (error) {
        res.status(400).send(error.details[0].message);
        return;
    }
    // Update course
    course.name = req.body.name;
    // Return the updated course
    res.send(course);
});

app.delete('/api/courses/:id', (req, res) => {
    // Look up
    // If DNE, return 404
    const course = courses.find(c => c.id == parseInt(req.params.id));
    if (!course) {
        res.status(404).send('Not here my guy.');
        return;
    }
    // Delete
    const index = courses.indexOf(course);
    courses.splice(index, 1);
    // Return that course
    res.send(course);
});

function validateCourse(course) {
    const schema = {
        name: Joi.string().min(3).required()
    }

    return Joi.validate(course, schema);
}

// /api/courses/1
app.get('/api/courses/:id', (req, res) => {
    const course = courses.find(c => c.id == parseInt(req.params.id));
    if (!course) {
        res.status(404).send('Not here my guy.');
    } else {
        res.send(course);
    }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Listening on port ${port}.`);
});