import requests
import json
import os
from dotenv import load_dotenv
from tags import Tags
from difficulty import Dif

load_dotenv()

ans = {
    'a': 'answer_a',
    'b': 'answer_b',
    'c': 'answer_c',
    'd': 'answer_d',
    'e': 'answer_e'
}



# API endpoint
url = "https://quizapi.io/api/v1/questions"

ques_limit = int(input("Please enter your desired numbers of question: "))
user_tag = Tags(input("Enter your desired technologies: "))
dif = Dif(input("Please enter your desired difficulty: "))

# API parameters
params = {
    "apiKey": os.getenv("QUIZ_API_KEY"),
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
        print(ques['question'] + "\n" )
        for key, value in ques["answers"].items():
            print(f"{key}: {value}")
        correct_answer = ques["correct_answer"]
        valid = False
        try:
             while not valid:
                user_input = input("Your answer: ").lower()
                if user_input in ans:
                    answer = ans[user_input]
                    valid = True
                    if correct_answer is not None and answer.lower() == correct_answer.lower():
                        print("You are correct!")
                    else:
                        print("You are wrong. The correct answer is:", correct_answer)    
                else:
                    print("Invalid answer. Please choose a, b, c, d, or e.")        
        except KeyError:
            print("Please enter valid answer which includes a, b, c, d and e")    
               
else:
    # Request was not successful
    print("Error:", response.status_code)
