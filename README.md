# CS50 Quiz Game

Welcome to the CS50 Quiz Game! This simple quiz game allows users to answer random questions and test their knowledge.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Questions File Format](#questions-file-format)

## Features

- Load questions from a file (`questions.txt`).
- Shuffle questions to randomize the order.
- Run a quiz with a specified number of random questions.
- Provide feedback on the user's answers.
- Allow the user to exit the program at any time.

## Getting Started

### Prerequisites

Before running the CS50 Quiz Game, make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/KristofferEdstrom/cs50p-quiz-game
   cd cs50p-quiz-game
   pip install -r requirements.txt
   ```


## Usage

To play the CS50 Quiz Game, follow these steps:

1. **Navigate to the project directory:**

   ```
   cd cs50p-quiz-game
   python quiz_game.py
   ```
2. **Answering Questions:**
* You will be presented with random questions from the loaded file
* For each question, the program displays the question and options (labeled as A, B, C, D).
* Enter your answer by typing the corresponding letter (A, B, C, or D).
* Receive immediate feedback on the correctness of your answer.
* If you wish to exit the program at any time, simply type 'EXIT' when prompted for the number of questions.

3. **Exiting the Program:**
* If you want to exit the program at any time, type 'EXIT' (case insensitive) when prompted for the number of questions.

Example of gameplay:

    Welcome to the CS50 Quiz Game!

    Question 1:
    What is the capital of France?
    A. Paris
    B. Berlin
    C. London
    D. Madrid

    Your answer (A, B, C, or D): A
    Correct!

    Question 2:
    ...

    ...

    Quiz complete! Your final score is: X/Y (X correct out of Y questions).


## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
    ```bash
        git checkout -b feature-name
    ```
3. Make your changes and commit them
    ```bash
        git commit -m 'Description of changes'
    ```
4. Push to the branch:
    ```bash
        git push origin feature-name
    ```
5. Create a pull request. 
6. Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## Questions File Format
The program is exepecting a file named questions.txt formatted as below:

    Question A | Option AA | Option AB | Option AC | Option AD | AnswerA
    Question B | Option BA | Option BB | Option BC | Option BD | AnswerB
    Question C | Option CA | Option CB | Option CC | Option CD | AnswerC
Make sure to separate each component with the '|' (pipe) character, and that there are no empty rows between the questions.

Feel free to customize and contribute to the project to make it even better!

 The questions are generated using chatGPT-3.5. If the questions are not sorted from being duplicate, wrongly asked, incorrect, outdated - or if you have any of your own questions or feedback please open an issue.

Happy quizzing!

**Best regards, Kristoffer Edström**
