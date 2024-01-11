# quiz_game.py
import random
import sys

def main():
    print("\nWelcome to the CS50 Quiz Game!")

    # Load the questions from questions.txt and store them in the questions variable
    questions = load_questions("questions.txt")

    # Shuffle the questions to randomize the order
    random.shuffle(questions)

    # Run the quiz and get the final score
    max_questions = get_max_questions(len(questions))  # Set max_questions to the total number of questions
    score = run_quiz(questions, max_questions)

    print(f"\nQuiz complete! Your final score is: {score}/{max_questions}")

def load_questions(filename):
    # Empty list to store the questions in
    questions = []
    # An empty set, to store all unique questions in
    original_questions = set()

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into components using the "|" delimiter
                components = line.strip().split('|')

                # Create a dictionary for each question
                question = {
                    'question': components[0],
                    'options': components[1:5],
                    'answer': components[5]
                }

                # Check if there are duplicate questions in the file
                if question['question'] not in original_questions:
                    # Add the question dictionary to the list
                    questions.append(question)
                    # Add the question text to the set of original questions
                    original_questions.add(question['question'])

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)  # Exit the program with a non-zero status code indicating an error

    return questions


def ask_question(question):
    # Print the question and its options
    print(question['question'])
    for option in question['options']:
        print(f"{option}")

    while True:
        # Get the user's answer and make it uppercased
        user_answer = input("Your answer (A, B, C or D): ").upper()

        try:
            # Check if the user's answer is A, B, C, or D
            if user_answer not in ['A', 'B', 'C', 'D']:
                raise ValueError("Invalid input. Please enter A, B, C, or D.")

            # Check if the user's answer is correct, take the first char of 'answer' which is A,B,C or D
            correct_answer = question['answer'][0]
            # is_correct is True if user_answer matches with correct_answer
            is_correct = user_answer == correct_answer

            if is_correct:
                print("Correct!\n")
            # Providing a way for the user to exit the program
            elif user_answer == 'EXIT':
                sys.exit(0)
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.\n")

            return is_correct

        except ValueError as e:
            print(f"Error: {e}")

def run_quiz(questions, max_questions):

    score = 0
    # Loop through the subset of questions and see if they match with correct answer
    for i, question in enumerate(questions[:max_questions], start=1):
        print(f"\nQuestion {i}:")
        user_answer_is_correct = ask_question(question)
        if user_answer_is_correct:
            score += 1

    return score

def get_max_questions(total_questions):
    # Make sure the user inputs a valid number 1-total_questions
    while True:
        try:
            max_questions = input(f"\nGet 1-{total_questions} random questions. Type 'exit' any time to quit the program\nHow many questions? ")

            if max_questions.upper() == "EXIT":
                sys.exit(0)

            max_questions = int(max_questions)

            if 1 <= max_questions <= total_questions:
                return max_questions
            else:
                print(f"Please enter a number between 1 and {total_questions}.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    
