#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const eposides = JSON.parse(body).results;
    let presents = 0;
    for (const eposide in eposides) {
      const epCharacters = eposides[eposide].characters;
      for (const character in epCharacters) {
        if (epCharacters[character].includes('18')) {
          presents++;
        }
      }
    }
    console.log(presents);
  }
});
