#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (let index = 0; index < list.length; index++) {
    const element = list[index];
    if (element === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
