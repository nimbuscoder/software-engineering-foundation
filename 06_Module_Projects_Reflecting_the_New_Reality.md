# Module 06: Projects That Reflect the New Reality

## Module Overview

This module brings together the skills you have practised so far. You will work on small but realistic projects that require clear descriptions, real rules, agreements between parts, careful examination of results, and thoughtful decisions about trade-offs.

Each project is designed so that you can complete it using the ideas from earlier modules. The projects increase gradually in complexity.

**Python playground:** Use the [Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro) to try code examples from this module.

**Estimated total time:** 6–9 hours (spread across several sessions)

**Core objectives:**
- Apply systems thinking to problems that involve real rules and trade-offs.
- Write complete descriptions before building or generating any solution.
- Design simple agreements between parts of a system.
- Examine solutions carefully and improve them based on what you find.
- Record your decisions and the reasons behind them.

---

## Lesson 6.1 – Project A: A Simple Tracker with Rules

**Duration:** 60–90 minutes

**Goal:** Design and examine a small system that stores information and enforces clear rules.

**Expected outcomes**  
By the end of this project you should be able to:
- Write a complete description that includes purpose, information to store, allowed actions, rules, edge cases, and concrete checks.
- Design how the information is organised and the agreements between the main parts.
- Build or generate a solution only after the description is finished.
- Examine the solution against every rule and concrete check.
- Produce a short project note covering the most important rule, one trade-off, and the most useful discovery made during examination.

**Everyday starting point**  
Imagine you want to keep track of classroom supplies or personal books. You need to remember how many of each item you have, and you must never allow the number to go below zero.

**Project brief**  
Create a simple tracker for a limited set of items (for example: classroom supplies, personal books, or points in a game). The system must enforce at least two clear rules (examples: quantity cannot become negative; a maximum value cannot be exceeded; certain items cannot be removed once added).

**Suggested concrete example structure**  
- Items: pencils, notebooks, erasers
- Rules: quantity cannot go below 0; no item can have more than 20 units
- Actions: add stock, remove stock, show current amounts

**Simple code sketch (for illustration only)**

```python
inventory = {
    "pencils": 10,
    "notebooks": 5,
    "erasers": 8
}

def remove_item(item, amount):
    if item not in inventory:
        print("Item not found.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
    if inventory[item] - amount < 0:
        print("Not enough items.")
        return
    inventory[item] -= amount
    print("Updated:", inventory)
```

**Activity:**
1. Write a complete description that includes purpose, information to store, allowed actions, rules, edge cases, and concrete checks.
2. Design how the information is organised and the agreements between the main parts.
3. Build or generate a solution only after the description is finished.
4. Examine the solution against every rule and concrete check.
5. Refine if needed.
6. Produce a short project note that states:
   - The most important rule and why it mattered
   - One trade-off you considered
   - The most useful discovery made during examination

**Reflection:**
- How did the rules shape the description?
- What would have gone wrong if the rules had been left unstated?

---

## Lesson 6.2 – Project B: Two Parts Working Together

**Duration:** 60–90 minutes

**Goal:** Practise defining and respecting a clear agreement between two different parts of a system.

**Expected outcomes**  
By the end of this project you should be able to:
- Write a full description for the overall system and a separate, precise agreement between the two parts.
- Make sure the agreement states what information is passed, its form, and the responsibilities of each part.
- Build or generate the two parts so that they follow the agreement.
- Test each part as independently as possible, then test the combined system.
- Deliberately break the agreement in one part, observe the effect, then restore correct behaviour.
- Document why the clear agreement made examination and correction easier.

**Everyday starting point**  
Think of a simple order process: one person takes the order and checks it is valid, another person prepares the item. They can only work together if they share a clear agreement about what information is passed.

**Project brief**  
Design a small system that consists of two distinct parts. One part collects and checks input. The other part performs a calculation or transformation and produces a result. The two parts must communicate only through a clearly defined agreement.

**Concrete example idea**  
- Part A: Collects a temperature and checks it is a valid whole number in range.
- Part B: Receives only a valid temperature and produces clothing advice.
- Agreement: Part A only passes a valid integer; Part B assumes the number is already valid.

**Simple code sketch showing the agreement**

```python
def check_input(temp):
    if not isinstance(temp, int):
        print("Please enter a whole number.")
        return None
    if temp < -20 or temp > 50:
        print("Temperature out of range.")
        return None
    return temp

def give_advice(valid_temp):
    if valid_temp is None:
        return
    if valid_temp > 25:
        print("It is warm. Wear light clothes.")
    else:
        print("It is cool. Wear a jacket.")

# Using both parts
temperature = 28
valid = check_input(temperature)
give_advice(valid)
```

**Activity:**
1. Write a full description for the overall system and a separate, precise agreement between the two parts.
2. Ensure the agreement states what information is passed, the expected form, and the responsibilities of each part.
3. Build or generate the two parts so that they follow the agreement.
4. Test each part independently as far as possible, then test the combined system.
5. Deliberately introduce a small violation of the agreement in one part and observe the effect; then restore correct behaviour.
6. Document why the clear agreement made examination and correction easier.

**Reflection:**
- Why does a clear agreement support independent examination of parts?
- What problems can appear if the agreement is vague?

---

## Lesson 6.3 – Project C: Making a Clear Trade-off

**Duration:** 70–100 minutes

**Goal:** Face a situation in which two desirable qualities cannot both be maximised, and make a reasoned choice.

**Expected outcomes**  
By the end of this project you should be able to:
- Write a description that clearly names two competing qualities and states which one will be preferred and why.
- Include concrete checks that reflect the chosen priority.
- Produce a solution that follows the stated priority.
- Examine the solution against the checks.
- Write a short analysis of what was gained and what was given up by the chosen priority.

**Everyday starting point**  
Sometimes you cannot have everything at once. For example, a message can be very short and quick, or it can be detailed and careful — but not both at the same time. You must choose which quality matters more for the situation.

**Project brief**  
Choose a small problem that involves a genuine trade-off. Examples:
- A scoring system that can be very strict or more forgiving
- A converter that prioritises speed of response or thoroughness of checking
- A simple advisor that gives short answers or more detailed explanations

The system must make the trade-off visible in its description and behaviour.

**Concrete example idea**  
Trade-off: short advice messages versus detailed advice messages.  
Decision: Prefer short messages so the system stays simple and quick to read.  
Consequence: Some helpful detail is left out.

**Activity:**
1. Write a description that explicitly names the two competing qualities and states which one will be preferred and why.
2. Include concrete checks that reflect the chosen priority.
3. Produce a solution that follows the stated priority.
4. Examine the solution against the checks.
5. Write a short analysis of what was gained and what was given up by the chosen priority.
6. Optionally, produce a second version that reverses the priority and compare the two.

**Reflection:**
- Why is it important to decide trade-offs consciously rather than by accident?
- How does stating the trade-off in the description improve the quality of examination?

---

## Lesson 6.4 – Project D: Full Cycle with Multiple Rules

**Duration:** 90–120 minutes

**Goal:** Combine clear description, agreements, generation or building, careful examination, and documentation in one complete project.

**Expected outcomes**  
By the end of this project you should be able to:
- Write a complete description for a practical mini-system that includes at least three rules and at least one clear agreement between parts.
- Define the agreements.
- Prepare a high-quality request (or build carefully).
- Examine the result against every part of the description and improve it at least once.
- Produce a final project summary covering purpose, key rules, most important examination finding, one improvement, and a short statement of what the project taught about systems thinking or precise description.

**Everyday starting point**  
Think of a tool a student of your age might actually use: a study-session timer with break rules, a simple reading log with weekly goals, or a points system for a classroom challenge with maximums and penalties.

**Project brief**  
Select a practical mini-system that a student of similar age might use. The system must include at least three rules and at least one clear agreement between parts.

**Examples of suitable projects**
- A study-session timer that enforces maximum work time and required breaks
- A reading log that tracks books and enforces a weekly goal
- A classroom points system with maximum scores and simple penalties

**Activity:**
1. Write a complete description.
2. Define the agreements between parts.
3. Prepare a high-quality request if using a generative tool, or build carefully if working manually.
4. Examine the result against every part of the description.
5. Improve the solution at least once based on what you found.
6. Produce a final project summary that includes:
   - The purpose of the system
   - The key rules and why they were chosen
   - The most important examination finding
   - One improvement made after the first solution
   - A short statement of what the project taught about systems thinking or precise description

**Reflection:**
- Which guiding principle proved most useful during this project?
- How did the habit of writing the description first affect the final quality?

---

## Module 06 Completion Check

Before moving to Module 07, confirm that you can:
- Complete a full cycle from precise description to examined solution under real rules.
- Define and respect a simple agreement between parts.
- Make and explain a conscious trade-off.
- Document the reasoning behind key decisions and examination findings.

Record a longer reflection (about one page) on how the projects changed your approach to defining and examining systems.
