# Module 06: Projects That Reflect the New Reality

## Module Overview

This module consolidates all previous skills through projects that require precise specification, meaningful constraints, interface design, generation or implementation, and rigorous evaluation. The projects are intentionally small yet realistic. Each forces the student to confront trade-offs and to practise the full cycle of description, creation, and examination.

**Estimated total time:** 6–9 hours (distributed across several sessions).

**Core objectives:**
- Apply systems thinking to problems that involve real constraints and trade-offs.
- Produce complete specifications before any implementation or generation occurs.
- Design simple interfaces between parts of a system.
- Evaluate solutions thoroughly and iterate on the basis of evidence.
- Document decisions and the reasons for them.

---

## Lesson 6.1 – Project A: Constrained Information Tracker

**Duration:** 60–90 minutes

**Goal:** Design and evaluate a small system that must enforce clear rules about the information it stores.

**Project brief:**
Create a simple tracker for a limited set of items (for example, classroom supplies, personal books, or points in a game). The system must enforce at least two constraints (examples: quantity cannot become negative; a maximum value cannot be exceeded; certain items may not be removed once added).

**Required steps:**
1. Write a complete specification that includes purpose, data to be stored, allowed actions, constraints, edge cases, interfaces between parts, and acceptance criteria.
2. Design the organisation of information and the interfaces.
3. Obtain or create a solution only after the specification is finished.
4. Evaluate the solution against every criterion and constraint.
5. Refine as needed.
6. Produce a short project report that states:
   - The most important constraint and why it mattered.
   - One trade-off you considered.
   - The most useful discovery made during examination.

**Reflection focus:**
- How did the constraints shape the specification?
- What would have gone wrong if the constraints had been left unstated?

---

## Lesson 6.2 – Project B: Two-Part System with a Clear Interface

**Duration:** 60–90 minutes

**Goal:** Practise defining and respecting an interface between two independently understandable parts.

**Project brief:**
Design a small system that consists of two distinct parts. One part collects and validates input. The other part performs a calculation or transformation and produces a result. The two parts must communicate only through a clearly defined interface.

**Required steps:**
1. Write a full specification for the overall system and a separate, precise description of the interface.
2. Ensure the interface states what information is passed, the expected form of that information, and the responsibilities of each part.
3. Implement or generate the two parts so that they follow the interface.
4. Test each part independently as far as possible, then test the combined system.
5. Deliberately introduce a small violation of the interface in one part and observe the effect; then restore correct behaviour.
6. Document why the interface made examination and correction easier.

**Reflection focus:**
- Why does a clear interface support independent examination of parts?
- Under what conditions would a poorly defined interface create hidden failures?

---

## Lesson 6.3 – Project C: Handling Trade-offs Explicitly

**Duration:** 70–100 minutes

**Goal:** Confront a situation in which two desirable qualities cannot be maximised at the same time, and make a reasoned choice.

**Project brief:**
Choose a small problem that involves a genuine trade-off (examples: a scoring system that can be either very strict or more forgiving; a converter that can prioritise speed of response or thoroughness of validation; a simple advisor that can give short answers or more detailed explanations). The system must make the trade-off visible in its specification and behaviour.

**Required steps:**
1. Write a specification that explicitly names the two competing qualities and states which one will be preferred and why.
2. Include acceptance criteria that reflect the chosen priority.
3. Produce a solution that follows the stated priority.
4. Evaluate the solution against the criteria.
5. Write a short analysis of what was gained and what was given up by the chosen priority.
6. Optionally, produce a second version that reverses the priority and compare the two.

**Reflection focus:**
- Why is it important to decide trade-offs consciously rather than accidentally?
- How does stating the trade-off in the specification improve the quality of examination?

---

## Lesson 6.4 – Project D: Full Cycle under Multiple Constraints

**Duration:** 90–120 minutes

**Goal:** Integrate specification, interface design, generation or implementation, rigorous evaluation, and documentation in one sustained project.

**Project brief:**
Select a practical mini-system that a student of similar age might actually use (examples: a study-session timer with rules about breaks, a simple reading log that enforces weekly goals, a points system for a classroom challenge with maximums and penalties). The system must include at least three constraints and at least one clear interface between parts.

**Required steps:**
1. Write a complete specification.
2. Define interfaces.
3. Prepare a high-quality request if using a generative tool, or implement carefully if working manually.
4. Examine the result against every part of the specification.
5. Iterate at least once on the basis of examination findings.
6. Produce a final project summary that includes:
   - The purpose of the system.
   - The key constraints and why they were chosen.
   - The most important examination finding.
   - One improvement made after the first solution.
   - A short statement of what the project taught about systems thinking or precise problem formulation.

**Reflection focus:**
- Which guiding principle proved most useful during this project?
- How did the habit of writing the description first affect the final quality?

---

## Module 06 Completion Check

Before moving to Module 07, confirm that you can:
- Complete a full cycle from precise specification to examined solution under real constraints.
- Define and respect a simple interface between parts.
- Make and explain a conscious trade-off.
- Document the reasoning behind key decisions and examination findings.

Record a longer reflection (one page or equivalent) on how the projects changed your approach to defining and evaluating systems.
