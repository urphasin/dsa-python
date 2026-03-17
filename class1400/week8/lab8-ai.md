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




## REMARKS
This is actually a strong attempt—you’re thinking like a programmer. Let’s tighten your understanding.

✅ Question 1 — Exception Handling (Important Fix)

Your answer is not quite correct, and this is a big concept.

You said:

it will go to ValueError

❌ That’s wrong in your current code

👉 Python reads except blocks top to bottom

Your code:

except Exception as e:
    print(e)
except ValueError as e:
    print("You must enter a number not, characters.")
What actually happens:

"Bobby" → int("Bobby") → raises ValueError

BUT ValueError is a subclass of Exception

So Python catches it in except Exception FIRST

👉 That means:

Your "You must enter a number..." message will NEVER run

✅ Fix:
except ValueError:
    print("You must enter a number, not characters.")
except Exception as e:
    print(e)
🔥 Key concept:

Always catch specific exceptions first, then general ones.

✅ Question 2 — Edge Case (You got this ✔️)

You said:

avg = 0

min = inf

max = -inf

len = 0

✔️ That is exactly correct

Why:

avg initialized to 0 → never updated

min_val = inf → never replaced

max_val = -inf → never replaced

tally = [] → length = 0

🔥 Good thinking:

Your fix idea:

if not tally:
    print("Add at least one value")
    continue

✔️ That’s exactly what a real dev would do

⚠️ Question 3 — Your Answer (Half Right, Half Overthinking)

You gave two ideas, let’s break them:

❌ Binary heap idea

This is overkill for this problem.

You don’t need sorting structure

You don’t need priority queues

This is not a real-time min/max streaming system

👉 Good thinking, but unnecessary here

⚠️ Sorting idea

You said:

sort the list and use list[0] and list[-1]

✔️ Correct BUT:

Sorting = O(n log n)

Your current method = O(1) per insert

👉 So your current approach is better

✅ What I was really looking for:

The simplest answer:

min(tally)
max(tally)

👉 Python already gives you this

min(tally) → O(n)

max(tally) → O(n)

Tradeoff:
Approach	Time
Your method (tracking)	O(1) per insert
Using min/max later	O(n) when needed

👉 Both are valid depending on use case

🧠 Final Assessment
You’re doing well in:

Thinking about edge cases ✔️

Understanding state tracking ✔️

Beginning to think about time complexity ✔️

You need to sharpen:

⚠️ Exception hierarchy (VERY important in Python)

⚠️ Knowing when you're overengineering (heap idea)

🔥 One bonus question (quick check)

Why is this line unnecessary?

elif 0 <= num <= 100:

What happens if you remove it?

Answer that and you’re leveling up fast.