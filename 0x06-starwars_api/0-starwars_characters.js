#!/usr/bin/node

const httpRequest = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  httpRequest(`${API_URL}/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const charactersURLs = JSON.parse(body).characters;
    const charactersPromises = charactersURLs.map(
      url => new Promise((resolve, reject) => {
        httpRequest(url, (promiseError, __, charactersResponseBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charactersResponseBody).name);
        });
      }));

    Promise.all(charactersPromises)
      .then(names => console.log(names.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
