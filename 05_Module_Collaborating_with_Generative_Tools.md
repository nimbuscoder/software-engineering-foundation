# Module 05: Collaborating with Generative Tools

## Module Overview

This module develops the practical habits required to work effectively with systems that generate solutions from descriptions. The student learns to provide precise instructions, to request useful intermediate explanations, to examine outputs critically, and to iterate on constraints when the first result is unsatisfactory. The generative tool is treated as a powerful but imperfect collaborator.

**Estimated total time:** 4–6 hours.

**Core objectives:**
- Formulate clear and complete requests for a generative system.
- Examine generated solutions against the original specification without accepting them uncritically.
- Improve results by refining constraints and descriptions rather than by manual rewriting of every detail.
- Maintain independent judgement while using generative assistance.

---

## Lesson 5.1 – Preparing a High-Quality Request

**Duration:** 25–35 minutes

**Goal:** Practise turning a specification into a request that gives a generative system the best chance of producing a useful result.

**Activity:**
1. Take a short, complete specification written in an earlier module.
2. Rewrite the specification as a clear request addressed to a generative assistant. Include:
   - The purpose of the system.
   - The required behaviour.
   - Explicit constraints.
   - Expected handling of invalid input.
   - A request for the assistant to explain its approach briefly.
3. Compare the original specification with the request. Ensure that no important detail has been lost.
4. Do not yet send the request. Focus on the quality of the prepared text.

**Reflection:**
- Why does the quality of the request strongly influence the quality of the generated result?
- What details are most important to include?

**Principle focus:** Precise description before asking for an implementation.

---

## Lesson 5.2 – Examining a Generated Solution

**Duration:** 35–45 minutes

**Goal:** Develop a disciplined process for inspecting a generated solution rather than assuming it is correct.

**Activity:**
1. Submit a carefully prepared request to a generative assistant and obtain a solution.
2. Without running the solution yet, read it carefully and compare it with the original specification.
3. List any parts that appear incomplete, unclear, or different from what was requested.
4. Run the solution and test it against the acceptance criteria and edge cases.
5. Record every discrepancy between the requested behaviour and the observed behaviour.
6. Write a short note on the most important difference you discovered through examination.

**Reflection:**
- What did careful examination reveal that a quick glance would have missed?
- Why must every generated solution be treated as something to be examined?

**Principle focus:** Treating every generated solution as something to be examined, not merely accepted.

---

## Lesson 5.3 – Iterating Through Improved Constraints

**Duration:** 35–45 minutes

**Goal:** Learn to improve a result by refining the description and constraints rather than by discarding the generative process.

**Activity:**
1. Take a generated solution that failed one or more acceptance criteria.
2. Identify the precise reason for each failure.
3. Write an improved request that adds or clarifies the necessary constraints and examples.
4. Obtain a new solution.
5. Examine the new solution with the same care as before.
6. Repeat the cycle once more if needed.
7. Document how the successive refinements improved the result.

**Reflection:**
- Why is refining the request often more effective than trying to repair every detail by hand?
- Under what conditions would further iteration still be necessary?

**Principle focus:** Practising precise description; examining each new result; understanding the effect of constraints.

---

## Lesson 5.4 – Requesting Explanations and Alternatives

**Duration:** 30–40 minutes

**Goal:** Use the generative system not only to produce a solution but also to gain insight into its reasoning and to explore alternatives.

**Activity:**
1. After obtaining a working solution, ask the generative assistant to explain the main decisions it made.
2. Request at least one alternative approach that satisfies the same specification.
3. Compare the original solution and the alternative against the specification and against the idea of efficiency or clarity.
4. Decide which version better meets the stated goals and explain why in your notebook.
5. Note any new understanding you gained from the explanation.

**Reflection:**
- How does requesting an explanation support the habit of asking “why does this work?”
- When is it useful to examine an alternative solution even if the first one already meets the criteria?

**Principle focus:** Maintaining the habit of asking why; examining alternatives; understanding trade-offs.

---

## Lesson 5.5 – Recognising the Limits of Generation

**Duration:** 25–35 minutes

**Goal:** Develop judgement about situations in which a generated solution should be questioned or rejected.

**Activity:**
1. Create or obtain a generated solution that appears to work for normal cases but violates a constraint or fails an edge case.
2. Identify the limitation clearly.
3. Write a short analysis that answers:
   - What the solution does correctly.
   - What it fails to do.
   - Whether the failure comes from an incomplete request or from a limitation of the generative process.
   - What additional information or constraint would be required to address the failure.
4. Decide whether to continue iterating or to treat the current result as insufficient.

**Reflection:**
- Why is the ability to recognise limits an essential part of collaboration with generative tools?
- Under what conditions should a generated solution be rejected even if it appears mostly correct?

**Principle focus:** Critical examination; identifying failure conditions; independent judgement.

---

## Lesson 5.6 – Mini Project: Directed Generation under Constraints

**Duration:** 50–70 minutes

**Goal:** Apply the full cycle of precise request, generation, examination, and refinement to a small system that includes meaningful constraints.

**Activity:**
1. Write a complete specification for a small tool that enforces at least two real constraints (examples: a simple scoring system with maximum values, a converter that rejects impossible inputs, or a tracker that never allows negative quantities).
2. Prepare a high-quality request from the specification.
3. Obtain a generated solution.
4. Examine it systematically against every acceptance criterion and constraint.
5. Refine the request at least once and obtain an improved solution.
6. Produce a final evaluation that states whether the solution is acceptable and why.
7. Record the most valuable improvement that came from examination and iteration.

**Reflection:**
- How did the quality of your initial request affect the number of iterations required?
- What habit from this module will you carry forward into every future use of generative tools?

**Principle focus:** Full application of the guiding principles in collaboration with a generative system.

---

## Module 05 Completion Check

Before moving to Module 06, confirm that you can:
- Prepare a clear and complete request from a specification.
- Examine a generated solution systematically against requirements and constraints.
- Improve results by refining descriptions and constraints.
- Recognise and articulate the limits of a generated solution.

Record a short reflection on the difference between accepting a generated solution and examining it.
