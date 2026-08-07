# Module 03: Core Computer Science Foundations

## Module Overview

This module helps you understand how to organise information, why some ways of doing things take more work than others, and how different parts of a system can work together.  

The ideas start from everyday situations you can easily picture. Only after you have tried the concrete activity do we give the idea a clear name.  

**Estimated total time:** 5–7 hours

**Core objectives:**
- Organise information in different ways and notice when each way is useful.
- See that two correct solutions can take different amounts of work.
- Make clear agreements between different parts of a system.
- Describe the information a small system needs to remember.
- Apply these ideas when writing descriptions and checking results.

---

## Lesson 3.1 – Keeping Things in Order (Lists)

**Duration:** 30–40 minutes

**Goal:** Learn when it is useful to keep items in a fixed order and how that order affects what you can do.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Choose a simple situation that needs items kept in order.
- [ ] Write a clear description of what the ordered list should do.
- [ ] Create and use a list in Python (add, remove, and look at items by position).
- [ ] Check what happens when you ask for a position that does not exist.
- [ ] Explain when keeping order is helpful and when it might cause problems.

**Everyday starting point**  
Imagine you are packing a school bag. The order of items can matter (books at the bottom, lunch on top). Or imagine a queue of people waiting for food — the first person in line should be served first.

**Activity:**
1. Choose a simple real situation that needs items kept in order (for example: three tasks you must do this afternoon in a certain order, or the scores of three players in a game).
2. Write a clear description of what the ordered collection should do.
3. Create a list in Python and practise:
   - Adding an item
   - Removing an item
   - Looking at an item by its position (first, second, third…)
4. Try to look at a position that does not exist. Write down what happens.
5. In your notebook, answer: When is keeping a fixed order useful? When could relying only on position cause a problem?

**Reflection:**
- Why does the position of an item matter in some situations?
- What can go wrong if the order gets mixed up?

**Principle focus:** Writing a clear description first; examining what happens when something goes wrong.

---

## Lesson 3.2 – Finding Things by Name (Dictionaries)

**Duration:** 30–40 minutes

**Goal:** Learn a different way to organise information — by giving each piece a clear name instead of a position number.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Choose a situation where looking up information by a name is more useful than by position.
- [ ] Write a clear description of what the named collection should do.
- [ ] Create and use a dictionary in Python (add, retrieve, and handle a missing name).
- [ ] Compare this way of organising with the ordered list from the previous lesson.
- [ ] Explain when using the wrong organisation would make things harder or more error-prone.

**Everyday starting point**  
Think about a contacts list on a phone. You do not look for “the third person.” You look for “Alex” or “Mum.” The name is the key that lets you find the information quickly.

**Activity:**
1. Choose a simple situation where you need to look up information by a name or label (for example: the ages of three friends, or the number of points each player has).
2. Write a clear description of what this named collection should do.
3. Create a dictionary in Python and practise:
   - Adding a new name and value
   - Looking up a value by its name
   - Trying to look up a name that does not exist
4. Compare this approach with the ordered list from Lesson 3.1. Write a short note: When is each way better?
5. Ask yourself: What problems could appear if you used a list when a named collection would be clearer, or the other way around?

**Reflection:**
- Why does looking things up by a clear name often reduce mistakes?
- When might a named collection become hard to manage?

**Principle focus:** Understanding the purpose of different structures; examining alternatives; noticing trade-offs.

---

## Lesson 3.3 – Some Ways Take More Work (Efficiency)

**Duration:** 30–40 minutes

**Goal:** Notice that two correct solutions can still be different in how much work they make the computer do.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Write a clear description of a small task that can be solved in more than one way.
- [ ] Create two different solutions that both give the correct answer.
- [ ] Roughly count the steps or comparisons each solution needs.
- [ ] Explain why one solution might be better even though both are correct.
- [ ] Think about what happens when the problem becomes larger.

**Everyday starting point**  
Imagine you need to find the tallest person in a group of five friends. You could compare them one by one in different orders. Both ways can give the right answer, but one way might need more comparisons than the other.

**Activity:**
1. Write a clear description of a small task that can be solved in more than one way (example: find the largest number among five numbers).
2. Create two different solutions in Python that both produce the correct answer.
3. Roughly count how many comparisons or steps each solution performs.
4. In your notebook, explain why one solution might be preferable even though both are correct.
5. Imagine the same problem with twenty numbers instead of five. How would the difference in steps change?

**Reflection:**
- Why does the number of steps matter?
- When might a slower but clearer solution still be a good choice?

**Principle focus:** Looking beyond simple correctness; examining trade-offs; asking about real constraints.

---

## Lesson 3.4 – Clear Agreements Between Parts (Interfaces)

**Duration:** 30–40 minutes

**Goal:** Learn that different parts of a system can work together only when they share a clear agreement about how they communicate.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Describe a simple system that has two distinct parts.
- [ ] Write a clear agreement (what information is passed, in what form, and what each part can expect).
- [ ] Build the two parts so they follow the agreement.
- [ ] Break the agreement on purpose and observe what happens.
- [ ] Restore the agreement and confirm that the system works again.
- [ ] Explain why a clear agreement makes it easier to check or change one part without breaking the other.

**Everyday starting point**  
Think about ordering food at a counter. You tell the cashier what you want (the agreement). The cashier tells the kitchen. If you speak unclearly or the cashier passes the wrong message, the order fails. The agreement between you and the cashier (and between the cashier and the kitchen) must be clear.

**Activity:**
1. Imagine a small system with two parts:
   - Part A collects a number from the user.
   - Part B doubles that number and shows the result.
2. Write a clear agreement between the two parts:
   - What information is passed?
   - In what form?
   - What can each part expect from the other?
   - What should happen if the agreement is broken?
3. Build the two parts as separate functions that follow the agreement.
4. Deliberately break the agreement in one part and observe the result.
5. Fix the agreement and confirm the system works correctly again.
6. In your notebook, explain why a clear agreement makes it easier to examine or change one part without damaging the other.

**Reflection:**
- Why is an explicit agreement between parts valuable?
- What problems can appear later if the agreement is vague?

**Principle focus:** Writing precise descriptions of how parts interact; examining what happens when agreements are broken; systems thinking.

---

## Lesson 3.5 – Describing the Information a System Needs

**Duration:** 30–40 minutes

**Goal:** Practise describing clearly what information a small system must remember and how the pieces of information relate to each other.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Choose a small real situation and write a clear description of the information it needs to store.
- [ ] Decide on simple structures (lists, dictionaries, or a combination) to hold that information.
- [ ] Build a minimal version that can store and retrieve the information.
- [ ] Test with normal data and with missing or unexpected data.
- [ ] Improve the original description if testing shows that something important was missing.

**Everyday starting point**  
Imagine a simple classroom library. You need to remember which books exist, who has borrowed them, and when they are due. If you forget to record one of these pieces, the system cannot answer basic questions.

**Activity:**
1. Choose a small real-world situation (example: tracking books borrowed from a classroom library, or recording scores for a simple game).
2. Write a clear description of:
   - The information that must be stored
   - How the pieces of information relate to each other
3. Decide on suitable structures (lists, dictionaries, or a combination).
4. Build a minimal version that can store and retrieve the information.
5. Test with normal data and with missing or unexpected data.
6. Revise the original description if testing reveals that important information was left out.

**Reflection:**
- Why does thinking carefully about the information first lead to better systems?
- What can go wrong if the description of the data is incomplete?

**Principle focus:** Precise problem formulation; examining completeness; noticing missing pieces.

---

## Lesson 3.6 – Mini Project: A Small Information System

**Duration:** 45–60 minutes

**Goal:** Combine organising information, noticing work differences, and making clear agreements inside one small system that has real rules.

**Expected outcomes (checklist)**  
By the end of this lesson you should be able to:
- [ ] Define a small system that must store and retrieve information under at least one real rule (constraint).
- [ ] Write a complete description that includes purpose, information needed, actions, the rule that must never be broken, and what to do with invalid input.
- [ ] Design how the information is organised and the agreements between the main parts.
- [ ] Build the system.
- [ ] Test it carefully against the description, especially the rule and invalid inputs.
- [ ] Record any changes you made to the description after testing the first version.

**Project brief**  
Create a simple tracker for a limited set of items (for example: classroom supplies, personal books, or points in a game). The system must enforce at least one clear rule (examples: quantity cannot become negative, a maximum value cannot be exceeded, or certain items cannot be removed once added).

**Activity:**
1. Write a complete description that includes:
   - The purpose of the system
   - The information it must remember
   - The actions a user can perform
   - At least one rule that must never be broken
   - How the system should respond when given invalid input
2. Design how the information will be organised and the agreements between the main parts.
3. Build the system.
4. Test it thoroughly against the description, paying special attention to the rule and to invalid inputs.
5. Record any changes you made to the description after examining the first version.

**Reflection:**
- Which part of the description proved most important during testing?
- What trade-off did you have to consider (for example, simplicity versus strict enforcement of a rule)?

**Principle focus:** All guiding principles applied together in one small system.

---

## Module 03 Completion Check

Before moving to Module 04, confirm that you can:
- Organise information using both ordered lists and named collections, and explain when each is useful.
- Notice that two correct solutions can still differ in the amount of work they require.
- Write a clear agreement between two parts of a system and test what happens when the agreement is broken.
- Describe the information a small system needs and improve that description after testing.

Record a short reflection on how the ideas in this module change the way you write descriptions of systems.
