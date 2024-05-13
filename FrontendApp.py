const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

let users = [];

app.use(bodyParser.json());

app.post('/add_user', (req, res) => {
    const { name, address } = req.body;

    if (name && address) {
        users.push({ name, address });
        res.status(201).json({ message: 'User added successfully!' });
    } else {
        res.status(400).json({ error: 'Invalid input' });
    }
});

app.get('/get_users', (req, res) => {
    res.status(200).json(users);
});

app.listen(port, () => {
    console.log(Server is running on http://localhost:${port});
});