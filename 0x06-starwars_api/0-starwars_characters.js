#!/usr/bin/node

// Import the request module to make HTTP requests
const request = require('request');

// Parse command-line arguments to get the movie ID
const movieID = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

// Make an HTTP GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('HTTP Error:', response.statusCode);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Print each character name
    characters.forEach((characterUrl) => {
      // Make a request for each character URL
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('Error fetching character:', error);
        }
      });
    });
  }
});
