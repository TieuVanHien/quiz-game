import requests

# API endpoint
url = "https://quizapi.io/api/v1/questions"

# API parameters
params = {
    "apiKey": "aPDvB6Yp4dqaASO4AKHyvyIcGrrQ0KOrPB1v9KRB",
    "limit": 10,
    "category": "Linux",
    "difficulty": "easy"
}

# Request headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Make the API request
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response data
    data = response.json()
else:
    # Request was not successful
    print("Error:", response.status_code)
