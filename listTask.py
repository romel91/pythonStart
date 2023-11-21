# List of dictionaries representing questions and options
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A. Paris', 'B. Berlin', 'C. Madrid', 'D. Rome'],
        'correct_option': 'A'
    },
    {
        'question': 'Which programming language is this chatbot written in?',
        'options': ['A. Java', 'B. Python', 'C. JavaScript', 'D. Ruby'],
        'correct_option': 'B'
    },
    {
        'question': 'What is the largest mammal?',
        'options': ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Lion'],
        'correct_option': 'B'
    },
    # Add more questions as needed
]

# Display the questions and options
for index, question in enumerate(questions, start=1):
    print(f"{index}. {question['question']}")
    for option in question['options']:
        print(f"   {option}")
    print()
