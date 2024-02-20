#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let presents = 0;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        presents++;
      }
    }
    console.log(presents);
  }
});
