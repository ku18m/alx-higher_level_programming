#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const usersCompletedTasks = {};
    JSON.parse(body).forEach((task) => {
      if (task.completed === true) {
        if (usersCompletedTasks[task.userId]) {
          usersCompletedTasks[task.userId]++;
        } else {
          usersCompletedTasks[task.userId] = 1;
        }
      }
    });
    console.log(usersCompletedTasks);
  }
});
