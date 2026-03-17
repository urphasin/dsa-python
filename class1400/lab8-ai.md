# Question 1 (Exceptions – subtle)

Right now you have:

except Exception as e:
    print(e)
except ValueError as e:
    print("You must enter a number not, characters.")

👉 Which except block will actually run if the user types "Bobby" — and why?
(Be precise about how Python matches exceptions.)


### Answer 1:
If user types Bobby as bobby is string and not number it generate value error but the error is captured and handled through except ValueError as e line. So it prints You must enter number and not character.


# Question 2 (Logic – edge case)

What happens if the user presses "c" before entering any scores at all?

What values get printed for:

High

Low

Average

Number of Students

👉 Explain why those values occur based on your initialization.

### Answer 2:
If user presses c. It prints avg = 0, min = float(inf), max = float(-inf), number_of_students = 0, but I could handle it and see if the tally is empty print"Add at least one value" and continue the loop.



# Question 3 (State tracking – deeper understanding)

You are manually tracking:

running_sum
min_val
max_val
tally

👉 If I delete min_val and max_val, how could you still correctly compute the high and low only using tally when the user presses "c"?


### Answer 3:
I guess you can also you a binary heap and always keep sorted, but my way is 0(1) constant check right so n entries and it's constant for each one. So O(1) amortized. Second way I think would be slower, it is using list.sort() anytime c is pressed and print list[0] and list[-1] for min and max respectively.