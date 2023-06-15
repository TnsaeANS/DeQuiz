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

After the user input questions in the above format.
 The following code will return each question as a dictonary in a list with its own stem, options and answer key.
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