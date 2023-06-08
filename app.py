import requests
import json

# API endpoint
url = "https://quizapi.io/api/v1/questions"


ques_limit = int(input("Please enter your desired numbers of question: "))
user_tag = input("Enter your desired technologies: ")
dif = input("Please enter your desired difficulty: ")

# API parameters
params = {
    "apiKey": "aPDvB6Yp4dqaASO4AKHyvyIcGrrQ0KOrPB1v9KRB",
    "tags": user_tag,
    "limit": ques_limit,
    "difficulty": dif
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
    with open("quiz.json", "w") as file:
        file.write(json.dumps(data))
    for ques in data:
        print(ques['question'])
        answer = input("Your answer: ")
        if answer == ques["correct_answer"]:
            print("You are correct!")
        else:
            print("You are wrong")    
                
else:
    # Request was not successful
    print("Error:", response.status_code)
