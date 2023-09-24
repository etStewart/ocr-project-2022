const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
app.use(bodyParser.json());

app.post('/submit', (req, res) => {
  const jsonContent = JSON.stringify(req.body);

  fs.writeFile('data.json', jsonContent, 'utf8', function (err) {
    if (err) {
      console.log("An error occurred while writing JSON Object to File.");
      return res.status(500).send(err);
    }
 
    console.log("JSON file has been saved.");
    res.send('Form data has been saved to output.json');
  });
});

app.listen(3000, () => console.log('Server is running on port 3000'));