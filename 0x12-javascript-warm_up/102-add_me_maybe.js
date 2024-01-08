#!/usr/bin/node

function increamenter (number, theFunction) {
  number++;
  theFunction(number);
}

exports.addMeMaybe = increamenter;
