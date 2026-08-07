# Module 04: Higher-Level Software Engineering Skills

## Module Overview

This module shifts attention to the skills that become central when artificial intelligence systems can generate implementations. The student learns to write precise specifications, define clear interfaces, state constraints, and evaluate results rigorously. Implementation remains secondary to the quality of the description and the thoroughness of examination.

**Estimated total time:** 5–7 hours.

**Core objectives:**
- Write complete and unambiguous specifications that include purpose, behaviour, constraints, and acceptance criteria.
- Define simple interfaces that allow independent parts to work together.
- Identify and state meaningful constraints and edge cases.
- Evaluate a solution systematically against its specification.

---

## Lesson 4.1 – Writing a Clear Specification

**Duration:** 30–40 minutes

**Goal:** Practise producing a specification that is precise enough for another person (or a generative system) to implement without further questions.

**Activity:**
1. Choose a small system (example: a tool that converts a temperature from Celsius to Fahrenheit and advises the user about clothing).
2. Write a specification that includes:
   - The purpose of the system.
   - Exactly what inputs it accepts.
   - Exactly what outputs or actions it produces.
   - How it should behave when given unexpected or invalid input.
   - At least two concrete examples of correct behaviour.
3. Review the specification and remove any remaining ambiguity.
4. Do not implement the system yet. The focus is solely on the quality of the description.

**Reflection:**
- Which parts of the specification were hardest to make precise?
- Why is it valuable to include examples of correct behaviour?

**Principle focus:** Precise description before implementation; prioritising understanding of the required behaviour.

---

## Lesson 4.2 – Adding Constraints and Edge Cases

**Duration:** 30–40 minutes

**Goal:** Extend a specification with explicit constraints and with situations that sit at the boundaries of normal use.

**Activity:**
1. Take the specification from Lesson 4.1 (or write a new one for a different small system).
2. Add at least three constraints (examples: the input must be a number within a certain range; the system must never display a negative temperature advice; the response must appear within a short time).
3. List at least four edge cases (examples: the lowest allowed value, the highest allowed value, an empty input, a non-numeric input).
4. For each edge case, state the required behaviour.
5. Review the completed specification for completeness.

**Reflection:**
- Why do constraints and edge cases belong in the specification rather than being discovered later?
- Under what conditions would omitting an edge case cause serious problems?

**Principle focus:** Seeking real constraints; writing precise descriptions; preparing for thorough examination.

---

## Lesson 4.3 – Defining Interfaces

**Duration:** 30–40 minutes

**Goal:** Practise describing the agreement that must exist between different parts of a system.

**Activity:**
1. Design a small system that has at least two distinct parts (example: one part that collects and validates user input, and another part that performs a calculation and produces a result).
2. Write a clear interface description for the communication between the parts. Include:
   - What information is passed.
   - The form of that information.
   - What each part may assume about the other.
   - What should happen if the agreement is broken.
3. Do not implement the parts yet. Focus only on the interface.
4. Ask a second person (or imagine explaining it to one) whether the interface is clear enough to implement independently.

**Reflection:**
- Why does a well-defined interface make later examination and modification easier?
- Under what conditions would a weak interface create hidden problems?

**Principle focus:** Precise description of interactions; systems thinking; preparing components for independent evaluation.

---

## Lesson 4.4 – Acceptance Criteria

**Duration:** 25–35 minutes

**Goal:** Learn to state concrete conditions that must be true for a solution to be considered acceptable.

**Activity:**
1. Return to a specification written earlier.
2. Convert the most important requirements into acceptance criteria. Each criterion should be written so that it is possible to test whether it has been met.
   Example form: “When the input is X, the system must produce Y.”
3. Write at least five acceptance criteria.
4. Review them to ensure they are specific and testable.
5. Note any part of the original specification that is still difficult to turn into a clear criterion.

**Reflection:**
- Why are testable criteria more useful than general statements of desire?
- How do acceptance criteria guide the later examination of a generated solution?

**Principle focus:** Precise formulation; preparing for rigorous evaluation.

---

## Lesson 4.5 – Systematic Evaluation of a Solution

**Duration:** 40–50 minutes

**Goal:** Practise examining an implementation against a complete specification rather than merely checking that it “seems to work”.

**Activity:**
1. Take a complete specification (including constraints, edge cases, and acceptance criteria).
2. Obtain an implementation (write a simple one yourself or, if available, request a generated version after providing the specification).
3. Create a simple test plan that covers:
   - Normal cases listed in the specification.
   - Every stated edge case.
   - Every constraint.
4. Execute the test plan and record the results carefully.
5. For any failure, decide whether the specification needs improvement or the implementation is incorrect.
6. Write a short evaluation report that states whether the solution meets the specification and why.

**Reflection:**
- What did careful examination reveal that a casual check would have missed?
- Why is it important to treat every solution as something that must be examined against the original description?

**Principle focus:** Treating every solution as something to be examined; maintaining the habit of asking why it works and when it fails.

---

## Lesson 4.6 – Mini Project: Specification and Evaluation Cycle

**Duration:** 50–70 minutes

**Goal:** Complete a full cycle of precise specification, interface definition, implementation (or generation), and rigorous evaluation under real constraints.

**Activity:**
1. Choose a small but non-trivial tool that involves at least one meaningful constraint (examples: a simple budget tracker that never allows a negative balance, a classroom point system that enforces maximum scores, or a unit converter that rejects impossible values).
2. Write a full specification including purpose, inputs, outputs, constraints, edge cases, interfaces between parts, and acceptance criteria.
3. Implement or generate the solution only after the specification is complete.
4. Evaluate the solution systematically against every part of the specification.
5. Revise either the specification or the solution until the acceptance criteria are met.
6. Document the most important change that resulted from the examination process.

**Reflection:**
- How did the presence of constraints change the way you wrote the specification?
- What was the most useful question you asked while examining the solution?

**Principle focus:** Full application of all guiding principles.

---

## Module 04 Completion Check

Before moving to Module 05, confirm that you can:
- Write a specification that includes purpose, behaviour, constraints, edge cases, and acceptance criteria.
- Define a clear interface between two parts of a system.
- Evaluate a solution systematically against its specification.
- Distinguish between a failure of the specification and a failure of the implementation.

Record a short reflection on how writing the specification first changes the quality of the final result.
