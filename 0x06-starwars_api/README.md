# Star Wars Movie Characters

This script retrieves and prints the names of the characters from a specific Star Wars movie using the Star Wars API.

## Requirements

- Node.js (version 10 or above)
- `request` module

## Usage

1. Clone the repository or download the script file.

2. Open a terminal and navigate to the directory containing the script.

3. Install the required `request` module by running the following command:

   ```shell
   npm install request
4. Run the script with the movie ID as a command-line argument. For example, to print the character names from "Return of the Jedi" (movie ID 3), use the following command:
    ```shell
    ./star_wars_characters.js 3
  The script will fetch the movie information from the Star Wars API, retrieve the character URLs, and print the names of the characters on separate lines.
