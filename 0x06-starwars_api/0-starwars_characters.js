#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as a command-line argument
if (process.argv.length < 3) {
  console.log('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Send a GET request to the Star Wars API films endpoint
const filmsUrl = `https://swapi.dev/api/films/${movieId}/`;
request(filmsUrl, function (error, response, body) {
  // Check for request errors
  if (error) {
    console.log(`Failed to retrieve movie information. Error: ${error.message}`);
    process.exit(1);
  }
  // Check if the request was successful
  if (response.statusCode !== 200) {
    console.log(`Failed to retrieve movie information. Error: ${response.statusCode}`);
    process.exit(1);
  }

  // Parse the response JSON
  const data = JSON.parse(body);

  // Retrieve the characters list from the film data
  const characters = data.characters;

  // Print the character names
  characters.forEach(function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      // Check for request errors
      if (error) {
        console.log(`Failed to retrieve character information. Error: ${error.message}`);
        return;
      }
      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      } else {
        console.log(`Failed to retrieve character information. Error: ${response.statusCode}`);
      }
    });
  });
});
