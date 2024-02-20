#!/usr/bin/node

const fs = require('fs/promises');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8')
  .then()
  .catch((err) => { console.log(err); });
