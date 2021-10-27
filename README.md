# CuiBot

## Description
This is a discord bot programmed in python for my private server with my friends.

## Installation
For this code to work a discord application is needed just change the `TOKEN` variable to the token of you application and run the `commands.py` with python3.6 or higher.

## Usage
This bot contains various commands, this bot's prefix is "!".
### 1. !help, !h
This coommand send the user a direct message with the list of commands and their description.
### 2. !random
This command generates a random number between 0 and the given number, if the given number is 420 it will always return 69.
### 3. !roll
This command rolls any given dice (d4, d6, d8, d10, d12, d20 and d100).
### 4. !ciucui
This command types "Pees it's self" on the text channel that the command is sent.
### 5. !play, !p
This command uses the library youtube_dl to download video from any given link and ffmpeg to play it's audio in the voice channel the user is, if the bot is already playing audio adds the audio to a queue.
### 6. !stop, !st
This command disconnects the bot from the voice channel, clears the song queue and stops playing audio.
### 7. !skip, !s
Skips currently playing song.
### 8. !Joke
This command uses de JokeAPI to type a joke in chat. 
Get example:

`{
    "error": false,
    "category": "Programming",
    "type": "twopart",
    "setup": "What are bits?",
    "delivery": "Tiny things left when you drop your computer down the stairs.",
    "flags": {
        "nsfw": false,
        "religious": false,
        "political": false,
        "racist": false,
        "sexist": false,
        "explicit": false
    },
    "id": 211,
    "safe": true,
    "lang": "en"
}`

## License

MIT License

Copyright (c) 2021 Mikel Fuentes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
