"""
.... question format
1. What is the capital of France?
A. London
B. Paris
C. Madrid
D. Rome
B 

2. Which planet is known as the Red Planet?
A. Jupiter
B. Mars
C. Saturn
D. Venus
B

After the user input questions in the above format. The following code will return each question as a dictonary in a list with its own stem, options and answer key.
The list will also include the title of the quiz

The value that will be returned will look like this 

{
    'stem': '1. What is the capital of France?',
    'options': [' London', ' Paris', ' Madrid', ' Rome'],
    'answer': 'B'
},
{
    'stem': '2. Which planet is known as the Red Planet?',
    'options': [' Jupiter', ' Mars', ' Saturn', ' Venus'],
    'answer': 'B'
}


"""

class MultipleChoiceParser:
    def __init__(self, quiz, title):
        self.questions = []  # List to store the parsed questions( the list that will be returned)
        self.questions = self.parse_input(quiz, title)  # Call the parse_input method to parse the quiz input(for it to start working a soon as the class is called)
    
    def parse_input(self, quiz_input, title_input):
        self.question_num = 1  # Initialize the question number
        self.set_title(title_input)  # Set the quiz title
        self.question_data = self.set_quiz(quiz_input)  # Set the quiz questions and options
        
    def set_title(self, text):
        self.questions.append({"title": text})  # Add the quiz title to the questions list, as a dictonary at the first index
        
    def set_quiz(self, qtext):
        each_lines = qtext.strip().splitlines()  # Split the input into separate lines
        improved_lines = [line for line in each_lines if line.strip()]  # Remove any empty lines
        num_lines = len(improved_lines)  # Count the number of non-empty lines
        
        for i in range(0, num_lines):
            if improved_lines[i][0].isdigit():  # If the line starts with a digit, it is a question stem
                num_digit = len(str(self.question_num))  # Get the number of digits in the question number
                self.questions.append({"stem": improved_lines[i]})  # Add the question stem to the questions list, at a new index postion in the question list
                self.questions[self.question_num]["options"] = []  # Create an empty list to store the options, this will created for each question
                
                for j in range(i, num_lines):
                    if improved_lines[j].replace(" ", "").startswith(("A.", "B.", "C.", "D.")) and len(self.questions[self.question_num]["options"]) <= 4 and len(improved_lines[j]) >= 2:
                        # If the line starts with "A.", "B.", "C.", or "D.", and the number of options is less than or equal to 4, add the option to the options list
                        self.questions[self.question_num]["options"].append(improved_lines[j][num_digit+1:])

                    elif improved_lines[j].startswith(("A", "B", "C", "D")) and len(improved_lines[j]) == 1:
                        # If the line starts with "A", "B", "C", or "D", and the length is 1, it is the answer line
                        self.questions[self.question_num]["answer"] = improved_lines[j]  # Set the answer for the current question
                        self.question_num += 1  # Increment the question number
                        break

                    elif not improved_lines[j].startswith(("1", "2", "3", "4")) and not improved_lines[j].replace(" ", "").startswith(("A.", "B.", "C.", "D.")):
                        # If the line does not start with a digit or "A.", "B.", "C.", or "D.", it is a continuation of the current question stem
                        self.questions[self.question_num]["stem"] += improved_lines[j]  # Append the line to the current question stem
        return self.questions

      
                
        
#uncomment the code below for testing

# input_text = """
# 1. What is the capital of France?
# A. London
# B. Paris
# C. Madrid
# D. Rome
# B

# 2. Which planet is known as the Red Planet?
# A. Jupiter
# B. Mars
# C. Saturn
# D. Venus
# B

# """

# a = MultipleChoiceParser(input_text, "Test Quiz Title")
# print(a.question_data)