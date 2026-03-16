"""
In this assignment, you will use exceptions to ensure the user enters the valid amounts for a series of test scores.

The program will gather stats for a teacher's most recent quiz.  The score must be between 0 and 100.  The score must be a numeric value. If the value entered does not meet that criteria, it should print out an appropriate message.

After the user has chosen to calculate the results, the program should display the lowest score, highest score, the average and the number of students entered.

Sample Run
Enter a score: -82
Sorry, the scores must be positive.
Enter a score: Bobby
Sorry, the scores must be a number.
Enter a score:  82

Press s to enter another score or press c to calculate: s

Enter a score: 90

Press s to enter another score or press c to calculate: s

Enter a score: 100

#continue looping and adding scores

Press s to enter another score or press c to calculate: c

#Add more scores, at least 5, as they are added create a list for example these numbers would be appended to a list
#82, 90, 100, 100, 98, 88, 80
#Then find the following from the list:

High: 100
Low: 82
Average: 91
Number of Students: 7

"""