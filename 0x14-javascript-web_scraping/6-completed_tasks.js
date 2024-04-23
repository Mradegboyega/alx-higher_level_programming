#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}

function countCompletedTasks(apiUrl) {
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to get data, status code:', response.statusCode);
      return;
    }

    const completedTasks = {};

    // Iterate through each task and count completed tasks for each user ID
    body.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    });

    console.log(completedTasks);
  });
}

countCompletedTasks(apiUrl);
