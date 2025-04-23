const express = require('express');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 15000;

app.use(express.json());

app.get('/status', (req, res) => {
  res.json({ status: 'ok', service: 'dcore' });
});

app.listen(port, () => {
  console.log(`🚀 dcore running at http://localhost:${port}`);
});