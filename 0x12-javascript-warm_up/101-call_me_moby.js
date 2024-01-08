#!/usr/bin/node

function repeater (x, theFunction) {
  for (let repeat = 0; repeat < x; repeat++) {
    theFunction();
  }
}

exports.callMeMoby = repeater;
