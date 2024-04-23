#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasksCompleted = {};

    body.forEach((todo) => {
      if (todo.completed) {
        if (!tasksCompleted[todo.userId]) {
          tasksCompleted[todo.userId] = 1;
        } else {
          tasksCompleted[todo.userId] += 1;
        }
      }
    });
    console.log(tasksCompleted);
  }
});
