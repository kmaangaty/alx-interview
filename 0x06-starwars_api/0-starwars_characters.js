#!/usr/bin/node

// Import the request module for making HTTP requests
const httpRequest = require('request');

// Retrieve the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint using the provided movie ID
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make an asynchronous HTTP GET request to the Star Wars API
httpRequest(apiUrl, async (error, response, body) => {
  // Handle errors, if any
  error && console.log(error);

  // Extract the array of character URLs from the response body
  const charactersArray = JSON.parse(response.body).characters;

  // Iterate over each character URL and make an asynchronous request for their details
  for (const characterUrl of charactersArray) {
    // Use Promise to handle asynchronous request
    await new Promise((resolve, reject) => {
      // Make a request for each character URL
      httpRequest(characterUrl, (error, response, body) => {
        // Handle errors, if any
        error && console.log(error);

        // Parse the response body to extract the character's name and log it
        console.log(JSON.parse(body).name);

        // Resolve the Promise to continue with the next iteration
        resolve();
      });
    });
  }
});
