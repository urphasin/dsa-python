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

def main():

    tally = []
    avg = 0
    running_sum = 0

    min_val = float("inf")
    max_val = float("-inf")
    while True:
        ui = input("press s to enter (s)core or press c to (c)alculate Avg, High, and Min , or q to (q)uit: ")
        if ui == "s":
            try:
                num = int(input("Enter a score: "))

                if num < 0 or num > 100:
                    raise Exception("Number must satisfy 0 <= num <= 100")

                elif 0 <= num <= 100:
                    if num <= min_val:
                        min_val = num
                    if num >= max_val:
                        max_val = num

                    running_sum += num
                    tally.append(num)
                    print(f"\x1b[95m{num}\x1b[0m entered into tally.")
                    avg = running_sum / len(tally)

            except ValueError as e:
                print("You must enter a number not, characters.")
            except Exception as e:
                print(e)
        elif ui == "q":
            print("Goodbye!")
            break
        elif ui == "c":
            print("\n\n")
            print(f"\x1b[44mHigh\x1b[0m: {max_val}")
            print(f"\x1b[41mLow\x1b[0m: {min_val}")
            print(f"\x1b[42mAverage\x1b[0m: {avg}")
            print(f"\x1b[30;47mNumber of Students\x1b[0m: {len(tally)}")
            print("\n\n")


if __name__ == "__main__":
    main()






