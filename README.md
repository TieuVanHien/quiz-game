# Quiz Game Python Project

This Python project utilizes the `quizapi.io` API to fetch quiz data and store it in a JSON file.

## Project Description

The Quiz Game Python Project allows you to retrieve quiz data from the `quizapi.io` API and save it locally in a JSON file for offline usage.

The project provides a script that interacts with the API, fetches quiz data based on user preferences, and stores the fetched data in a JSON file for future use.

## Features

- Fetch quiz data from `quizapi.io` API
- Store fetched quiz data in a JSON file
- Support for customizing quiz preferences (category, difficulty, tags and question limit)

## Technologies Used

- Python
- `requests` library (for making HTTP requests)
- JSON (for data storage)

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

1. Clone the repository: `git clone https://github.com/your-username/quiz-game.git`
2. Navigate to the project directory: `cd quiz-game`
3. Create a virtual environment: `python -m venv venv`. (Alternatively, you can run the `setup.bat` file as administrator, it will automatically create venv for you)
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

5. Install the required dependencies: `pip install -r requirements.txt`

### Usage

1. Set up an account and obtain an API key from `quizapi.io`
2. Open the `.env` file and replace the value of `API_KEY` with your actual API key
3. Run the script: `python app.py`
4. The script will retrieve quiz data from the API and store it in a JSON file named `quiz.json`. I put the data in json file for you to have an easier look

### Customization

You can customize the quiz preferences by modifying the values in the input I already created. Update the following variables according to your desired preferences:

- `tags`: The category of quizzes to fetch (e.g., "Linux", "Docker", "PHP")
- `difficulty`: The difficulty level of quizzes (e.g., "easy", "medium", "hard")
- `limit`: The number of quiz questions to fetch

### Data Storage

The fetched quiz data will be stored in a JSON file named `quiz.json`. You can use this file to load quiz data into your application or perform offline operations.
