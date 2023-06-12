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

function fetchCharacters (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Failed to retrieve character information. Error: ${response.statusCode}`));
      } else {
        const filmData = JSON.parse(body);
        resolve(filmData.characters);
      }
    });
  });
}

function fetchCharacterData (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Failed to retrieve character information. Error: ${response.statusCode}`));
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

async function printCharacterNames () {
  try {
    const characterUrls = await fetchCharacters(filmsUrl);
    const characterPromises = characterUrls.map(url => fetchCharacterData(url));
    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error.message);
  }
}

printCharacterNames();
