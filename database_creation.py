import requests
import json
import random

# Code To Create a example database of 100 questions from each subject with different dificulties 😂😂😂

url = 'http://127.0.0.1:8000/create_question'

headers = {'Content-Type': 'application/json'}

topics = {
    'Physics': ['Mechanics', 'Thermodynamics', 'Electromagnetism', 'Optics', 'Quantum Physics'],
    'Chemistry': ['Organic Chemistry', 'Inorganic Chemistry', 'Physical Chemistry', 'Analytical Chemistry', 'Biochemistry'],
    'Maths': ['Algebra', 'Calculus', 'Geometry', 'Statistics', 'Number Theory']
}

difficulties = ['easy', 'medium', 'hard']

marks = {
    'easy': range(1, 6),
    'medium': range(6, 11),
    'hard': range(11, 16)
}

for subject, subject_topics in topics.items():
    for i in range(1, 101):
        difficulty = random.choice(difficulties)

        payload = {
            "question": f"{subject} Question {i}?",
            "subject": subject,
            "topic": random.choice(subject_topics),
            "difficulty": difficulty,
            "marks": random.choice(marks[difficulty])
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        print(f"{subject} Question {i}:", response.json())
