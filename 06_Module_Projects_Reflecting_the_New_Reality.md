# Module 06: Projects That Reflect the New Reality

## Module Overview

This module brings together the skills you have practised so far. You will work on small but realistic projects that require clear descriptions, real rules, agreements between parts, careful examination of results, and thoughtful decisions about trade-offs.

Each project is designed so that you can complete it using the ideas from earlier modules. The projects increase gradually in complexity.


**Estimated total time:** 6–9 hours (spread across several sessions)

### Core objectives
- Apply systems thinking to problems that involve real rules and trade-offs.
- Write complete descriptions before building or generating any solution.
- When using a generative tool, convert the description into a structured request (Purpose, Rules, Examples, Constraints, Self-check) and examine the result systematically.
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

**Concrete worked example (Classroom Supply Tracker)**  

You may use this example as a model or choose a different set of items. The important elements are the complete description, the explicit rules, and the careful examination.

**Description**
- Purpose: Keep track of three classroom supplies (pencils, notebooks, erasers) so that quantities never become negative and never exceed a maximum of 20 units each.
- Information stored: current quantity of each item.
- Allowed actions: add stock, remove stock, show current amounts.
- Rules that must never be broken:
  1. Quantity of any item cannot go below 0.
  2. Quantity of any item cannot exceed 20.
  3. Only the three named items are allowed.
- Edge cases and required behaviour:
  - Trying to remove more than the current quantity → refuse the action and show a clear message.
  - Trying to add an amount that would exceed 20 → refuse the action and show a clear message.
  - Using an unknown item name → show “Item not found.”
  - Using a non-positive amount → show “Amount must be positive.”

**Model structured request** (for use with a generative tool)

```
Please create a simple Python program for a classroom supply tracker.

Purpose:
Track quantities of pencils, notebooks and erasers. Quantities must never go below 0 and never exceed 20.

Rules (these must never be broken):
- Only the three items “pencils”, “notebooks” and “erasers” are allowed.
- Quantity of any item cannot become negative.
- Quantity of any item cannot exceed 20.
- Amounts must be positive whole numbers.

Examples of correct behaviour:
- Starting quantities: pencils=10, notebooks=5, erasers=8
- remove(“pencils”, 3) → pencils becomes 7
- remove(“pencils”, 20) when only 7 remain → “Not enough items.”
- add(“notebooks”, 20) when already 5 → “Would exceed maximum of 20.”
- show() → display all current quantities

Constraints:
- Use a dictionary to store the quantities.
- Keep the program simple and readable for a beginner.
- Do not add extra features.

Self-check (required before you finish):
Verify that every rule and every example is satisfied. Correct any problem and re-check before presenting the final program and a short explanation.
```

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
3. Build or generate a solution only after the description is finished. If you use a generative tool, first convert the description into a structured request (Purpose, Rules, Examples, Constraints, Self-check).
4. Examine the solution against every rule and concrete check.
5. Refine if needed (by improving the request design or the implementation).
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

**Concrete worked example (Study Session Timer)**  

You may follow this example or design a different system. The important elements are multiple real rules, at least one clear agreement between parts, a structured request, and careful examination.

**Description**
- Purpose: Help a student manage focused study sessions with mandatory short breaks.
- Information stored: current session length in minutes, whether the student is in a work period or a break period.
- Parts of the system:
  - Part A (Session Controller): accepts the desired work length and checks that it is valid.
  - Part B (Timer Display): receives only a valid work length and manages the work/break cycle.
- Agreement between parts:
  - Part A may pass only a whole number between 15 and 50 inclusive.
  - Part B assumes the number it receives is already valid and never re-checks the range.
  - If Part A cannot obtain a valid number, it must not call Part B.
- Rules that must never be broken:
  1. Work sessions must be between 15 and 50 minutes inclusive.
  2. After every work session a break of exactly 5 minutes is required before another work session can start.
  3. The system must never allow a work session longer than 50 minutes.
- Edge cases and required behaviour:
  - Input 10 → “Work session must be between 15 and 50 minutes.”
  - Input 60 → “Work session must be between 15 and 50 minutes.”
  - Input 25 → start a 25-minute work period, then enforce a 5-minute break.
  - Empty or non-numeric input → “Please enter a whole number.”

**Model structured request** (for use with a generative tool)

```
Please create a simple Python program for a study-session timer.

Purpose:
Help a student manage focused study sessions. Work sessions must be between 15 and 50 minutes. After every work session a 5-minute break is required.

Rules (these must never be broken):
- Accept only whole numbers between 15 and 50 inclusive for the work length.
- After every completed work session, enforce a 5-minute break before another work session can begin.
- Never allow a work session longer than 50 minutes.
- Keep the program simple and readable for a beginner.

Examples of correct behaviour:
- Input 25 → begin a 25-minute work period, then require a 5-minute break.
- Input 10 → “Work session must be between 15 and 50 minutes.”
- Input 60 → “Work session must be between 15 and 50 minutes.”
- Input “abc” → “Please enter a whole number.”

Constraints:
- Use two clear parts (functions): one that checks and accepts the work length, and one that runs the work/break cycle.
- The checking part must never pass an invalid value to the timer part.
- Do not add extra features such as sound or graphics.

Self-check (required before you finish):
Verify that every rule and every example is satisfied. Confirm that an invalid length is rejected before the timer part is called. Correct any problem and re-check before presenting the final program and a short explanation.
```

**Activity:**
1. Write a complete description.
2. Define the agreements between parts.
3. Prepare a high-quality structured request (Purpose, Rules, Examples, Constraints, Self-check) if using a generative tool, or build carefully if working manually.
4. Examine the result against every part of the description.
5. Improve the solution at least once based on what you found (preferably by refining the request design).
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
- When using generative tools, convert descriptions into structured requests and examine the results systematically.
- Define and respect a simple agreement between parts.
- Make and explain a conscious trade-off.
- Document the reasoning behind key decisions and examination findings.

Record a longer reflection (about one page) on how the projects changed your approach to defining and examining systems.
