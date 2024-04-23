#!/usr/bin/node
// number of movies where the character “Wedge Antilles” is present.

const req = require('request');
let cont = 0;

req.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          cont += 1;
        }
      });
    });
    console.log(cont);
  }
});
