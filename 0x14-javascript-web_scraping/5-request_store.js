#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const filename = process.argv[3];
    const fs = require('fs');
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
