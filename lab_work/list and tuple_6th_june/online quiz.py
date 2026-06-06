"""
Program: Student Answer Evaluation

This program performs the following tasks:
1. Calculate score.
2. Display incorrectly answered question numbers.
3. Count correct and wrong answers.
4. Determine pass/fail (minimum 60%).
"""

# Correct answers and student answers
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# --------------------------------------------------
# Task 1: Calculate score + count correct/wrong

score = 0
correct_count = 0
wrong_count = 0

for i in range(len(correct)):
    if student[i] == correct[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1

print("Score :", score, "/", len(correct))

# --------------------------------------------------
# Task 2: Display incorrectly answered question numbers

print("\nIncorrectly Answered Questions:")

for i in range(len(correct)):
    if student[i] != correct[i]:
        print("Question", i + 1)

# --------------------------------------------------
# Task 3: Count correct and wrong answers

print("\nCorrect Answers :", correct_count)
print("Wrong Answers :", wrong_count)

# --------------------------------------------------
# Task 4: Determine pass/fail (60% minimum)

percentage = (score / len(correct)) * 100

print("\nPercentage :", percentage)

if percentage >= 60:
    print("Result : PASS")
else:
    print("Result : FAIL")