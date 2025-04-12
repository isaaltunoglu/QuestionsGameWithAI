# Quiz Game with Gemini AI (CLI Version)

> ⚠️ **Note:** This is the command-line interface (CLI) version of the quiz game. A graphical user interface (GUI) is planned in future updates.

## Overview
This project is a simple yet dynamic quiz game powered by **Gemini AI**. It generates general knowledge questions using the Gemini 2.0 Flash model, interacts with the user via the terminal, and tracks the score based on correct answers.

## Features
- Fetches 10 general knowledge questions using the Gemini API.
- Parses questions, options, and correct answers from plain text.
- Awards points for correct answers.
- Shows the correct answer on failure and offers an option to restart the game.

## Requirements
- Python 3.x
- `google-generativeai` library
- Gemini API Key()

## Installation
```bash
pip install google-generativeai
