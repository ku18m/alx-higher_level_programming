#!/usr/bin/node

const request = require('request');

function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        reject(new Error(`Failed to fetch character: ${response.statusCode}`));
      }
    });
  });
}

(async function () {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode === 200) {
          resolve(body);
        } else {
          reject(new Error(`Failed to fetch film: ${response.statusCode}`));
        }
      });
    });

    const filmData = JSON.parse(filmResponse);
    const characters = filmData.characters;
    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  } catch (error) {
    console.error(error);
  }
})();
