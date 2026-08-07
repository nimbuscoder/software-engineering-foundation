# Module 01: Building Computational Thinking and Basic Programming Intuition

## Module Overview

This module helps you learn to think in clear, ordered steps and to describe simple behaviour with precision. You will use Python because its wording is easy to read. This lets you focus on ideas instead of complicated rules. The main goal is to understand why a set of instructions produces a particular result.

**Python playground:** Use the [Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro) to try code examples from this module.

**Estimated total time:** 4–6 hours (short lessons)

**Core objectives:**
- Break everyday tasks into precise, ordered steps.
- Express simple behaviour using variables, decisions, repetition, and functions.
- Write a clear description of what should happen before you create any instructions.
- Examine every result and ask why it works and when it might fail.

---

## Lesson 1.1 – Thinking in Steps

**Duration:** 20–30 minutes

**Goal:** Practise breaking a familiar task into exact, ordered instructions that leave no room for guessing.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Choose a simple everyday task.
- [ ] Write a numbered list of steps that another person could follow without asking questions.
- [ ] Find and rewrite any step that is unclear or assumes hidden knowledge.
- [ ] State at least one condition under which your instructions would fail or give the wrong result.

**Model example of precise steps**  
Task: Making a cup of instant noodles (this is only an example — choose a different task for your own work).

1. Take one packet of instant noodles and one heat-proof bowl.
2. Open the noodle packet and empty the noodles into the bowl.
3. Open the seasoning packet and empty the seasoning into the same bowl.
4. Boil water in a kettle until it reaches a full rolling boil.
5. Carefully pour enough boiling water into the bowl to cover the noodles completely.
6. Cover the bowl with a plate and leave it undisturbed for three full minutes.
7. Remove the plate, stir the noodles thoroughly with a fork, and serve.

Every step says exactly what to do, with what, and (when needed) how long or how much. No step assumes the reader already knows the process.

**Activity:**
1. Choose a simple everyday task different from the example (for example: packing a school bag, watering a plant, or preparing a glass of milk).
2. In your notebook, write a precise numbered list of steps that another person could follow without asking any questions.
3. Check your list against the checklist above. Find any step that is still unclear or that assumes knowledge the other person might not have. Rewrite those steps until they match the standard in the model example.
4. Ask yourself: Under what conditions would these instructions fail or produce the wrong result? Write your answer under the steps.

**Reflection:**
- Why does the order of steps matter?
- What happens if a step is missing or written vaguely?

**Principle focus:** Writing precise descriptions before any implementation; asking when something would fail.

---

## Lesson 1.2 – Variables as Named Containers

**Duration:** 25–35 minutes

**Goal:** Understand that a variable is a named place that holds a value, and that the name should clearly describe the purpose of the value.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Create three variables with clear, meaningful names.
- [ ] Display the values of those variables with explanatory text.
- [ ] Change one value and observe the effect.
- [ ] Write a precise description of the program’s intended behaviour *before* running it.
- [ ] Compare the description with the actual result.

**Model example**

```python
student_age = 12
favourite_subject = "Mathematics"
books_read_last_month = 4

print("Age:", student_age)
print("Favourite subject:", favourite_subject)
print("Books read last month:", books_read_last_month)
```

**Activity:**
1. Open a Python environment.
2. Create three variables with clear names that store information about yourself (for example: your age, your favourite subject, and the number of books you read last month).
3. Write a short sequence that displays these values with explanatory text.
4. Change one value and observe the effect.
5. In your notebook, write a precise description of what the short program is intended to do *before* you run it. Then compare the description with what actually happened.

**Reflection:**
- Why is a clear variable name more useful than a short or cryptic name?
- Under what conditions would using the wrong variable name cause a problem?

**Principle focus:** Understanding over memorisation; examining results; asking why and when it fails.

---

## Lesson 1.3 – Decisions (Conditionals)

**Duration:** 30–40 minutes

**Goal:** Learn how a program can choose different actions based on a condition, and practise stating the condition precisely.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of a decision the program should make.
- [ ] Implement the decision using an if-else structure.
- [ ] Test the program with normal values and with a boundary value.
- [ ] Improve the original description if the boundary case shows an ambiguity.

**Model example of a precise description**  
“If the temperature is above 30 degrees, advise the user to drink water. Otherwise, advise the user that the temperature is comfortable.”

**Activity:**
1. Write a precise description in your notebook of a simple decision a program should make. Use the model above as a guide for clarity, but choose your own decision.
2. Only after the description is clear, implement it in Python using an if-else structure.
3. Test the program with different values.
4. Deliberately give the program a value that sits exactly on the boundary of your condition. Observe and record what happens.
5. Improve the original description if the boundary case reveals an ambiguity.

**Reflection:**
- Why must the condition be stated without ambiguity?
- What would happen if the condition were written incorrectly?

**Principle focus:** Precise description first; examining solutions; identifying failure conditions.

---

## Lesson 1.4 – Repetition (Loops)

**Duration:** 30–40 minutes

**Goal:** Understand when and why a sequence of instructions should be repeated, and how to control the repetition clearly.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of a repetitive task, including when the repetition should stop.
- [ ] Implement the behaviour using a loop.
- [ ] Modify the stopping condition and observe the effect.
- [ ] Explain what would happen if the stopping condition were never met.

**Activity:**
1. Choose a simple repetitive task (for example: printing the numbers from 1 to 10, or counting how many times a particular letter appears in a short word).
2. Write a precise description of the intended behaviour, including when the repetition should stop.
3. Implement the behaviour using a loop.
4. Modify the stopping condition and observe the effect.
5. Ask: What would happen if the stopping condition were never met?

**Reflection:**
- Why is it important to define the end of a repetition clearly?
- Under what conditions could a loop continue forever or finish too early?

**Principle focus:** Understanding the “why”; examining behaviour under different conditions; precise control of constraints.

---

## Lesson 1.5 – Functions as Reusable Units of Behaviour

**Duration:** 30–40 minutes

**Goal:** Learn to package a clear piece of behaviour into a named function so that it can be reused and understood independently.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of a small piece of behaviour, including what information it needs and what result it should produce.
- [ ] Turn the behaviour into a function with a clear name.
- [ ] Call the function several times with different inputs and examine the outputs.
- [ ] Change the internal steps of the function and check whether the original description still holds.

**Activity:**
1. Identify a small piece of behaviour you have already written (for example, displaying a greeting or calculating a simple total).
2. Write a precise description of what that behaviour should achieve, including what information it needs and what result it should produce.
3. Turn the behaviour into a function with a clear name.
4. Call the function several times with different inputs and examine the outputs.
5. Change the internal steps of the function and observe whether the original description still holds.

**Reflection:**
- Why does giving a clear name and a clear description to a function improve understanding?
- Under what conditions would a function produce an incorrect or unexpected result?

**Principle focus:** Precise description before implementation; treating the function as something to be examined; understanding purpose over syntax.

---

## Lesson 1.6 – Mini Project: A Simple Interactive Tool

**Duration:** 40–50 minutes

**Goal:** Combine the ideas from previous lessons into a small program that requires a clear specification and careful examination.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a complete and precise description of a simple interactive tool.
- [ ] Include how the tool should respond to different inputs and to unexpected input.
- [ ] Implement the tool only after the description is finished.
- [ ] Test the tool with normal inputs, boundary values, and incorrect inputs.
- [ ] Revise the description or the implementation until the behaviour matches the description.
- [ ] Record one improvement made after examining the first version.

**Activity:**
1. Decide on a simple interactive tool (examples: a basic quiz that asks two or three questions, a temperature advisor, or a tool that calculates the total of a few numbers).
2. Write a complete and precise description of what the tool must do, including how it should respond to different inputs and what it should do if the input is unexpected.
3. Only after the description is finished, implement the tool.
4. Test it thoroughly with normal inputs, boundary values, and incorrect inputs.
5. Revise either the description or the implementation until the behaviour matches the description under all tested conditions.
6. In your notebook, record one improvement you made after examining the first version.

**Reflection:**
- Did writing the description first make the implementation clearer?
- What failure cases did you discover only after testing?

**Principle focus:** All five guiding principles applied together.

---

## Module 01 Completion Check

Before moving to Module 02, confirm that you can:
- Write a precise, ordered list of steps for a simple task.
- Use variables, decisions, loops, and functions with understanding of their purpose.
- Produce a clear written description before creating any instructions.
- Examine a result and explain both why it works and under what conditions it would fail.

Record a short reflection in your notebook about the most important idea you learned in this module.
