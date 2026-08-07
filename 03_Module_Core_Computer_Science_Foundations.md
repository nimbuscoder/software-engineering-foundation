# Module 03: Core Computer Science Foundations

## Module Overview

This module introduces fundamental ideas that remain useful no matter how software is produced. The focus is on structure, efficiency, communication between parts of a system, and the basic organisation of data. These concepts help you write better specifications and examine generated solutions with greater insight.

**Estimated total time:** 5–7 hours

**Core objectives:**
- Recognise common ways of organising information and when each is appropriate.
- Understand the basic idea of efficiency (why some solutions take more steps than others).
- Explain simple principles of how independent parts of a system can work together.
- Apply these ideas when writing specifications and examining results.

---

## Lesson 3.1 – Organising Information: Lists and Ordered Collections

**Duration:** 30–40 minutes

**Goal:** Understand when information should be kept in an ordered sequence and how that organisation affects behaviour.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of a small task that needs items kept in order.
- [ ] Implement the task using a list in Python.
- [ ] Add, remove, and retrieve items by position.
- [ ] Examine what happens when you try to retrieve an item that does not exist.
- [ ] Explain why order matters for the task and when a different organisation might be better.

**Activity:**
1. Write a precise description of a small task that requires keeping several items in order (example: a list of three tasks for the afternoon, or the scores of three players).
2. Implement the task using a list in Python.
3. Perform simple operations: add an item, remove an item, and retrieve an item by position.
4. Examine what happens when you try to retrieve an item that does not exist.
5. In your notebook, explain why order matters for this particular task and under what conditions a different organisation might be better.

**Reflection:**
- Why is an ordered collection useful?
- Under what conditions would relying on position (the place of an item) become unreliable?

**Principle focus:** Precise description; examining behaviour; identifying failure conditions.

---

## Lesson 3.2 – Organising Information by Name (Maps / Dictionaries)

**Duration:** 30–40 minutes

**Goal:** Understand the value of associating information with clear names rather than positions.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of a task that requires looking up information by a name or label.
- [ ] Implement the task using a dictionary.
- [ ] Retrieve values, add a new entry, and attempt to retrieve a name that does not exist.
- [ ] Compare this approach with the ordered list from the previous lesson.
- [ ] State when using the wrong kind of organisation would make a program harder to understand or more likely to fail.

**Activity:**
1. Write a precise description of a task that requires looking up information by a name or label (example: storing the ages of three friends and retrieving one friend’s age by name).
2. Implement the task using a dictionary.
3. Retrieve values, add a new entry, and attempt to retrieve a name that does not exist.
4. Compare this approach with the ordered list from the previous lesson. Write a short note on the advantages of each for different situations.
5. Ask: When would using the wrong kind of organisation make a program harder to understand or more likely to fail?

**Reflection:**
- Why does looking up information by a clear name often reduce mistakes?
- Under what conditions might a dictionary become difficult to manage?

**Principle focus:** Understanding purpose of structure; trade-offs; examining alternatives.

---

## Lesson 3.3 – The Idea of Efficiency

**Duration:** 30–40 minutes

**Goal:** Develop an initial sense that different correct solutions can require different amounts of work from the computer.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of a task that can be solved in more than one way.
- [ ] Implement two different solutions.
- [ ] Count, in rough terms, how many comparisons or steps each solution performs.
- [ ] Explain why one solution might be preferable even though both produce the correct answer.
- [ ] Consider how the difference in steps would grow with a larger version of the problem.

**Activity:**
1. Write a precise description of a task that can be solved in more than one way (example: find the largest number among five numbers).
2. Implement two different solutions.
3. Count, in rough terms, how many comparisons or steps each solution performs.
4. In your notebook, explain why one solution might be preferable even though both produce the correct answer.
5. Consider a larger version of the same problem (twenty numbers instead of five). Ask how the difference in steps would grow.

**Reflection:**
- Why does the number of steps matter?
- Under what conditions would a slower but clearer solution still be acceptable?

**Principle focus:** Understanding trade-offs; examining solutions beyond mere correctness; asking about real constraints.

---

## Lesson 3.4 – Interfaces as Agreements Between Parts

**Duration:** 30–40 minutes

**Goal:** Introduce the idea that separate parts of a system can work together only if they share a clear agreement about how they communicate.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a precise description of the agreement (interface) between two parts of a system.
- [ ] Implement the two parts as separate functions that follow the agreement.
- [ ] Deliberately break the agreement in one part and observe the result.
- [ ] Restore the agreement and confirm correct behaviour.
- [ ] Explain why a clear interface makes it easier to examine or replace one part without damaging the other.

**Activity:**
1. Imagine two simple parts of a system: one part that collects a number from a user, and another part that doubles that number and displays the result.
2. Write a precise description of the agreement (the interface) between the two parts: what information is passed, in what form, and what each part can expect.
3. Implement the two parts as separate functions that follow the agreement.
4. Deliberately break the agreement in one part and observe the result.
5. Restore the agreement and confirm correct behaviour.
6. In your notebook, explain why a clear interface makes it easier to examine or replace one part without damaging the other.

**Reflection:**
- Why is an explicit agreement between parts valuable?
- Under what conditions would a vague interface cause problems later?

**Principle focus:** Precise description of interactions; examining the consequences of broken agreements; systems thinking.

---

## Lesson 3.5 – Simple Data Modelling

**Duration:** 30–40 minutes

**Goal:** Practise describing the information a system needs to remember and how the pieces of information relate to one another.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Choose a small real-world situation and write a precise description of the information that must be stored.
- [ ] Decide on suitable structures (lists, dictionaries, or combinations) to represent that information.
- [ ] Implement a minimal version that can store and retrieve the information.
- [ ] Test with normal data and with missing or unexpected data.
- [ ] Revise the original description if testing shows that important information was omitted.

**Activity:**
1. Choose a small real-world situation (example: tracking books borrowed from a classroom library, or recording scores for a simple game).
2. Write a precise description of the information that must be stored and the relationships between the pieces of information.
3. Decide on suitable structures (lists, dictionaries, or combinations) to represent that information.
4. Implement a minimal version that can store and retrieve the information.
5. Test with normal data and with missing or unexpected data.
6. Revise the original description if testing reveals that important information was omitted.

**Reflection:**
- Why does thinking carefully about the information first lead to better systems?
- Under what conditions would an incomplete model of the data cause the system to fail?

**Principle focus:** Precise problem formulation; examining completeness; identifying missing constraints.

---

## Lesson 3.6 – Mini Project: A Small Information System

**Duration:** 45–60 minutes

**Goal:** Combine organisation of data, efficiency awareness, and clear interfaces in a constrained project.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Define a small system that must store and retrieve information under at least one real constraint.
- [ ] Write a complete specification that includes purpose, information, actions, constraint, and response to invalid input.
- [ ] Design the data organisation and the interfaces between the main parts.
- [ ] Implement the system.
- [ ] Test thoroughly against the specification, paying special attention to the constraint and invalid inputs.
- [ ] Record any changes made to the specification after examining the first implementation.

**Activity:**
1. Define a small system that must store and retrieve information under at least one real constraint (example: a simple inventory of five items that must not allow negative quantities, or a list of tasks that must keep track of whether each task is finished).
2. Write a complete specification that includes:
   - The purpose of the system.
   - The information it must remember.
   - The actions a user can perform.
   - At least one constraint that must never be violated.
   - How the system should respond when given invalid input.
3. Design the data organisation and the interfaces between the main parts.
4. Implement the system.
5. Test thoroughly against the specification, paying special attention to the constraint and to invalid inputs.
6. Record any changes you made to the specification after examining the first implementation.

**Reflection:**
- Which part of the specification proved most important during testing?
- What trade-off did you have to consider (for example, simplicity versus strict enforcement of a constraint)?

**Principle focus:** All guiding principles applied in a single project.

---

## Module 03 Completion Check

Before moving to Module 04, confirm that you can:
- Choose appropriate ways to organise information for a given task.
- Explain in simple terms why one correct solution may be preferable to another.
- Describe a clear interface between two parts of a system.
- Write a data description that includes necessary relationships and constraints.

Record a short reflection on how the ideas in this module change the way you write specifications.
