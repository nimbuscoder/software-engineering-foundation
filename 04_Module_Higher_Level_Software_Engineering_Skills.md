# Module 04: Higher-Level Software Engineering Skills

## Module Overview

This module teaches you how to describe clearly what a system should do, how to state the rules it must follow, and how to check carefully whether a solution actually works.  

The ideas begin with everyday situations you can picture. Formal names for the ideas are introduced only after you have practised the underlying action. Short code examples are included to make the ideas clearer.

**Python playground:** Use the [Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro) to try code examples from this module.

**Estimated total time:** 5–7 hours

**Core objectives:**
- Write clear descriptions of what a system should do.
- State rules the system must never break and situations that sit at the edge of normal use.
- Make clear agreements between different parts of a system.
- Turn requirements into concrete checks that can be tested.
- Examine a solution carefully against its description instead of accepting it quickly.

---

## Lesson 4.1 – Writing a Clear Description of What a System Should Do

**Duration:** 30–40 minutes

**Goal:** Practise writing a description that is clear enough for another person (or a computer helper) to follow without needing to ask extra questions.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Choose a small system and write a description that includes its purpose, what it accepts, what it produces, and how it should behave with unexpected input.
- Include at least two concrete examples of correct behaviour.
- Review the description and remove any remaining unclear parts.
- Stop at the description stage (do not build the system yet).

**Everyday starting point**  
Imagine you are explaining to a younger sibling exactly how to make a simple snack. If your instructions are vague, they will get stuck or do the wrong thing. The same problem happens when describing a computer system.

**Concrete example of a clear description**  
Here is a complete example for a simple temperature advisor (you should choose a different system for your own work):

- **Purpose:** Give simple clothing advice based on a temperature in Celsius.
- **Input:** A whole number representing degrees Celsius.
- **Output:** A short advice message.
- **Behaviour with unexpected input:** If the input is not a number, or is empty, the system must say “Please enter a whole number.”
- **Concrete examples of correct behaviour:**
  - When the input is 28, the system must say “It is warm. Wear light clothes.”
  - When the input is 12, the system must say “It is cool. Wear a jacket.”

**Simple code example that follows the description**  
(This is only an illustration. You do not need to write code in this lesson.)

```python
temperature = 28

if temperature > 25:
    print("It is warm. Wear light clothes.")
else:
    print("It is cool. Wear a jacket.")
```

**Activity:**
1. Choose a small system different from the example above (suggestions: a tool that converts temperature and gives clothing advice, a simple points calculator, or a tool that checks whether a number is even or odd and gives a message).
2. Write a description that includes:
   - The purpose of the system
   - Exactly what inputs it accepts
   - Exactly what outputs or actions it produces
   - How it should behave when given unexpected or invalid input
   - At least two concrete examples of correct behaviour
3. Review the description and remove any remaining ambiguity.
4. Do not build the system yet. The focus is only on the quality of the description.

**Reflection:**
- Which parts of the description were hardest to make precise?
- Why is it useful to include concrete examples of correct behaviour?

**Principle focus:** Writing a precise description before any implementation; focusing on understanding the required behaviour.

---

## Lesson 4.2 – Adding Rules and Edge Cases

**Duration:** 30–40 minutes

**Goal:** Extend a description with clear rules the system must never break and with situations that sit at the edge of normal use.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Add at least three clear rules (constraints) to a description.
- List at least four edge cases and state the required behaviour for each.
- Review the completed description for completeness.

**Everyday starting point**  
Think about a simple rule at home: “You may use the kitchen, but you must never leave the stove on unattended.” Or think about what should happen if someone tries to enter a number that is far too high or leaves a field empty. These boundary situations must be decided in advance.

**Concrete example (continuing the temperature advisor)**  
Rules:
1. The temperature must be a whole number between –20 and 50 inclusive.
2. The system must never give clothing advice for a temperature outside this range.
3. The advice message must be short (one or two sentences).

Edge cases and required behaviour:
- Input is –20 → Give the cold-weather advice.
- Input is 50 → Give the hot-weather advice.
- Input is –21 → Say “Temperature out of range. Please enter a number between –20 and 50.”
- Input is empty or not a number → Say “Please enter a whole number.”

**Simple code example that respects the rules**

```python
temperature = 28

if not isinstance(temperature, int):
    print("Please enter a whole number.")
elif temperature < -20 or temperature > 50:
    print("Temperature out of range. Please enter a number between -20 and 50.")
elif temperature > 25:
    print("It is warm. Wear light clothes.")
else:
    print("It is cool. Wear a jacket.")
```

**Activity:**
1. Take the description from Lesson 4.1 (or write a new one for a different small system).
2. Add at least three clear rules.
3. List at least four edge cases and state the required behaviour for each.
4. Review the completed description for completeness.

**Reflection:**
- Why should rules and edge cases be written into the description instead of being discovered later?
- What problems can appear if an edge case is left out?

**Principle focus:** Seeking real constraints; writing precise descriptions; preparing for careful examination.

---

## Lesson 4.3 – Clear Agreements Between Parts

**Duration:** 30–40 minutes

**Goal:** Practise writing a clear agreement that lets two different parts of a system work together reliably.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Design a small system that has at least two distinct parts.
- Write a clear agreement that states what information is passed, in what form, what each part can expect, and what should happen if the agreement is broken.
- Keep the focus on the agreement only (do not build the parts yet).
- Check whether the agreement is clear enough for someone else to understand.

**Everyday starting point**  
Remember the food-counter example. You give a clear order to the cashier. The cashier passes a clear message to the kitchen. If either message is unclear, the order fails. The same idea applies when one part of a computer system talks to another part.

**Concrete example**  
System: A simple temperature advisor split into two parts.

- Part A: Collects and checks the temperature input.
- Part B: Produces the clothing advice.

**Agreement between Part A and Part B:**
- Part A must pass a whole number between –20 and 50 inclusive.
- Part A must pass the number as a normal integer (not text).
- Part B can assume the number it receives is already valid.
- If Part A cannot get a valid number, it must not call Part B. Instead it must show an error message itself.
- If Part B ever receives a value outside the range, it must return the message “Invalid temperature received.”

**Simple code example that follows the agreement**

```python
def check_temperature(temp):
    """Part A: checks the input and only returns a valid temperature."""
    if not isinstance(temp, int):
        print("Please enter a whole number.")
        return None
    if temp < -20 or temp > 50:
        print("Temperature out of range. Please enter a number between -20 and 50.")
        return None
    return temp

def give_advice(valid_temp):
    """Part B: assumes it receives a valid temperature."""
    if valid_temp is None:
        return
    if valid_temp > 25:
        print("It is warm. Wear light clothes.")
    else:
        print("It is cool. Wear a jacket.")

# Using the two parts together
temperature = 28
valid = check_temperature(temperature)
give_advice(valid)
```

**Activity:**
1. Design a small system that has at least two distinct parts (example: one part that collects and checks user input, and another part that performs a calculation or produces advice).
2. Write a clear agreement for the communication between the parts. Include:
   - What information is passed
   - The form of that information
   - What each part may assume about the other
   - What should happen if the agreement is broken
3. Do not build the parts yet. Focus only on the agreement.
4. Ask yourself (or ask another person) whether the agreement is clear enough to follow independently.

**Reflection:**
- Why does a well-defined agreement make later checking and modification easier?
- What problems can appear if the agreement is vague?

**Principle focus:** Writing precise descriptions of interactions; systems thinking; preparing parts for independent examination.

---

## Lesson 4.4 – Turning Requirements into Concrete Checks

**Duration:** 25–35 minutes

**Goal:** Learn to turn important requirements into concrete statements that can be tested.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Convert the most important requirements into concrete checks that can be tested.
- Write at least five checks in a clear form such as “When the input is X, the system must produce Y.”
- Review the checks to make sure they are specific and testable.
- Note any part of the original description that is still difficult to turn into a clear check.

**Everyday starting point**  
Instead of saying “the system should work well,” we need statements we can actually test: “When the temperature is 35, the system must advise drinking water.” These concrete statements become the standard we use later to examine any solution.

**Concrete example (temperature advisor)**  
1. When the input is 28, the system must say “It is warm. Wear light clothes.”
2. When the input is 12, the system must say “It is cool. Wear a jacket.”
3. When the input is –20, the system must give the cold-weather advice.
4. When the input is 51, the system must say “Temperature out of range…”
5. When the input is empty, the system must say “Please enter a whole number.”

**Simple code example of checking one case**

```python
def get_advice(temperature):
    if not isinstance(temperature, int):
        return "Please enter a whole number."
    if temperature < -20 or temperature > 50:
        return "Temperature out of range. Please enter a number between -20 and 50."
    if temperature > 25:
        return "It is warm. Wear light clothes."
    else:
        return "It is cool. Wear a jacket."

# Concrete check
result = get_advice(28)
print(result)
# Expected: "It is warm. Wear light clothes."
```

**Activity:**
1. Return to a description written earlier.
2. Convert the most important requirements into concrete checks. Each check should be written so that it is possible to test whether it has been met.  
   Example form: “When the input is X, the system must produce Y.”
3. Write at least five concrete checks.
4. Review them to ensure they are specific and testable.
5. Note any part of the original description that is still difficult to turn into a clear check.

**Reflection:**
- Why are testable checks more useful than general statements of desire?
- How do these checks help later when examining a solution?

**Principle focus:** Precise formulation; preparing for careful evaluation.

---

## Lesson 4.5 – Examining a Solution Carefully

**Duration:** 40–50 minutes

**Goal:** Practise examining a solution against its description instead of simply checking that it “seems to work.”

**Expected outcomes**  
By the end of this lesson you should be able to:
- Create a simple test plan that covers normal cases, every stated edge case, and every rule.
- Carry out the test plan and record the results carefully.
- For any failure, decide whether the description needs improvement or the solution is incorrect.
- Write a short evaluation note that states whether the solution meets the description and why.

**Everyday starting point**  
Imagine you have written clear instructions for making a snack and someone follows them. You do not just taste the final snack. You check each step against the original instructions, especially the difficult or unusual cases. The same careful comparison is needed with computer solutions.

**Concrete example of a short evaluation note**  
“I tested the five concrete checks. Checks 1, 2, 3 and 5 passed. Check 4 failed: when the input was 51 the system still gave clothing advice instead of the out-of-range message. The description is clear, so the solution needs to be fixed.”

**Simple code example for testing several cases**

```python
def get_advice(temperature):
    if not isinstance(temperature, int):
        return "Please enter a whole number."
    if temperature < -20 or temperature > 50:
        return "Temperature out of range. Please enter a number between -20 and 50."
    if temperature > 25:
        return "It is warm. Wear light clothes."
    else:
        return "It is cool. Wear a jacket."

# Test plan
test_cases = [28, 12, -20, 51, "hello"]
for value in test_cases:
    print(value, "→", get_advice(value))
```

**Activity:**
1. Take a complete description (including rules, edge cases, and concrete checks).
2. Obtain a solution (write a simple one yourself or, if available, request a generated version after providing the description).
3. Create a simple test plan that covers:
   - Normal cases listed in the description
   - Every stated edge case
   - Every rule
4. Carry out the test plan and record the results carefully.
5. For any failure, decide whether the description needs improvement or the solution is incorrect.
6. Write a short evaluation note that states whether the solution meets the description and why.

**Reflection:**
- What did careful examination reveal that a quick check would have missed?
- Why is it important to treat every solution as something that must be examined against the original description?

**Principle focus:** Treating every solution as something to be examined; maintaining the habit of asking why it works and when it fails.

---

## Lesson 4.6 – Mini Project: Description and Examination Cycle

**Duration:** 50–70 minutes

**Goal:** Complete a full cycle of clear description, rules, agreements, concrete checks, building or generating a solution, and careful examination.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Choose a small but non-trivial tool that involves at least one meaningful rule.
- Write a full description including purpose, inputs, outputs, rules, edge cases, agreements between parts, and concrete checks.
- Build or generate the solution only after the description is complete.
- Examine the solution systematically against every part of the description.
- Revise either the description or the solution until the concrete checks are met.
- Record the most important change that resulted from the examination process.

**Project brief**  
Create a small tool that involves at least one meaningful rule. Suitable examples:
- A simple budget tracker that never allows a negative balance
- A classroom point system that enforces maximum scores
- A unit converter that rejects impossible values

**Activity:**
1. Write a full description including purpose, inputs, outputs, rules, edge cases, agreements between parts, and concrete checks.
2. Build or generate the solution only after the description is complete.
3. Examine the solution systematically against every part of the description.
4. Revise either the description or the solution until the concrete checks are met.
5. Record the most important change that resulted from the examination process.

**Reflection:**
- How did the presence of rules change the way you wrote the description?
- What was the most useful question you asked while examining the solution?

**Principle focus:** Full application of all guiding principles.

---

## Module 04 Completion Check

Before moving to Module 05, confirm that you can:
- Write a clear description that includes purpose, behaviour, rules, edge cases, and concrete checks.
- Define a clear agreement between two parts of a system.
- Examine a solution systematically against its description.
- Distinguish between a problem in the description and a problem in the solution.

Record a short reflection on how writing the description first changes the quality of the final result.
