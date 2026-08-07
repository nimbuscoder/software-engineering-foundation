# Module 05: Collaborating with Generative Tools

## Module Overview

This module develops the practical skill of directing generative tools with precision and examining their outputs with discipline. The central idea is prompt engineering treated as system design.

Students begin with a clear, rigid structure. This structure reduces ambiguity and produces more reliable first results. Once the underlying principles are internalised, students are encouraged to evolve toward more fluid, high-quality expression when the task benefits from narrative clarity.

The same habits trained here—precise purpose, explicit rules, concrete examples, constraints, and verification—apply whether the student is requesting code, a requirements document, an explanation, or a design rationale.

**Python playground:** Use the [Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro) to try code examples from this module.

**Estimated total time:** 4–6 hours

### Core objectives
- Convert a clear description into a structured request containing Purpose, Rules, Examples, Constraints, and a Self-check.
- Examine every generated solution systematically against the original rules and examples.
- Improve results by refining the request design rather than by endlessly patching the output.
- Recognise when a more fluid, narrative style of prompting is appropriate and begin to practise it.
- Retain independent judgement at every step.

---

## Lesson 5.1 – Designing a Structured Request

**Duration:** 30–40 minutes

**Goal:** Practise converting a clear description into a structured request that controls the generative tool through purpose, rules, examples, constraints, and verification.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Rewrite a clear description as a structured request.
- Organise the request into the sections Purpose, Rules, Examples, Constraints, and Self-check.
- State explicit limits on what the solution is allowed and not allowed to do.
- Instruct the generative tool to verify its own work against the rules before finishing.
- Confirm that no important detail from the original description has been lost.
- Focus on the quality of the request design (do not send the request yet).

**Everyday starting point**  
When you ask a careful helper to perform a task, vague instructions often produce incomplete or incorrect results. Supplying a clear purpose, strict rules, concrete examples, and an instruction to double-check the work greatly improves the chance of success. The same principle applies to generative tools.

**Model structured request**  
(Using a simple temperature advisor)

```
Please create a simple Python program that follows these instructions exactly.

Purpose:
Give short clothing advice based on a temperature in Celsius.

Rules (these must never be broken):
- Accept only whole numbers between -20 and 50 inclusive.
- If the input is not a whole number or is outside the range, show a clear error message and stop.
- Do not give clothing advice for any invalid temperature.
- Keep the program simple and readable for a beginner.

Examples of correct behaviour:
- Input 28 → “It is warm. Wear light clothes.”
- Input 12 → “It is cool. Wear a jacket.”
- Input 51 → “Temperature out of range. Please enter a number between -20 and 50.”
- Input “abc” → “Please enter a whole number.”

Constraints:
- Use only basic Python (input, if-elif-else, print).
- Do not add features that were not requested.

Self-check (required before you finish):
Before presenting the final program, verify that every rule and every example is satisfied. If any rule is broken, correct the program and check again. Then present the final program together with a short explanation of how it works.
```

**Activity:**
1. Take a short, complete description written in an earlier module (or create a new simple one).
2. Rewrite it as a structured request containing the five sections shown above.
3. Compare the original description with the structured request and confirm completeness.
4. Do not send the request yet. Focus only on the quality of the design.

**Reflection:**
- Why does explicit structure improve the reliability of the first result?
- How does the Self-check section change the generative process?
- Which section do you consider most important for preventing common failures?

**Principle focus:** Treating the request as a deliberate system design.

---

## Lesson 5.2 – Examining a Generated Solution

**Duration:** 35–45 minutes

**Goal:** Develop the disciplined habit of comparing a generated solution against every rule and example before accepting it.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Submit a structured request and obtain a solution.
- Read the solution carefully and compare it with every rule and example before running it.
- List any omissions, ambiguities, or deviations.
- Test the solution against normal cases, boundary values, and invalid inputs.
- Record every discrepancy and identify the most important problem.

**Activity:**
1. Submit a carefully prepared structured request and obtain a solution.
2. Without running the code, compare it line by line with the Rules and Examples sections.
3. List every difference or omission.
4. Run and test the solution thoroughly.
5. Record the most significant discrepancy discovered.

**Reflection:**
- What did systematic examination reveal that a quick reading would have missed?
- Why must every generated solution be treated as a hypothesis rather than as finished work?

**Principle focus:** Examination before acceptance.

---

## Lesson 5.3 – Improving the Request Design

**Duration:** 35–45 minutes

**Goal:** Improve results by strengthening the structure, rules, examples, or self-check of the request rather than by manually correcting every detail of the output.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Identify the precise cause of each failure in a generated solution.
- Locate the corresponding weakness in the original structured request.
- Write an improved structured request that addresses the weakness.
- Obtain and examine a new solution.
- Document how changes to the request design improved the result.

**Activity:**
1. Take a generated solution that failed one or more checks.
2. Identify the exact reason for each failure and the corresponding weakness in the request.
3. Strengthen the relevant section(s) of the structured request.
4. Obtain a new solution and examine it with the same care.
5. Repeat once more if needed and record the improvements that resulted from better request design.

**Reflection:**
- Why is refining the request often more effective than repeatedly patching the output?
- How did strengthening the Self-check section affect later results?

**Principle focus:** The request is an improvable design artefact.

---

## Lesson 5.4 – Explanations, Alternatives, and Judgement

**Duration:** 30–40 minutes

**Goal:** Use the generative tool to gain insight and to explore alternatives while retaining final judgement.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Ask for an explanation of the main decisions in a solution.
- Request at least one alternative that still satisfies the same rules and examples.
- Compare the original and the alternative against the original requirements and against clarity.
- Decide which version is preferable and justify the decision.
- Note any new understanding gained.

**Activity:**
1. After obtaining a working solution, ask for an explanation of the main design decisions.
2. Request one alternative approach that still obeys the same structured rules.
3. Compare both versions and decide which better meets the goals.
4. Record the decision and the reasons.

**Reflection:**
- How does requesting an explanation support the habit of asking “why does this work?”
- When is examining an alternative useful even if the first solution already passes the checks?

**Principle focus:** Insight and independent judgement.

---

## Lesson 5.5 – Recognising Limits

**Duration:** 25–35 minutes

**Goal:** Develop the ability to recognise when a generated solution remains insufficient even after refinement.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Identify a limitation that appears only under certain conditions or edge cases.
- Analyse what the solution does correctly, what it fails to do, and the likely source of the failure.
- Decide whether further request refinement is warranted or whether the current result should be rejected.

**Activity:**
1. Obtain or construct a solution that works for normal cases but fails a rule or edge case.
2. Write a short analysis covering correctness, failure, probable cause, and possible next steps.
3. Decide whether to continue iterating or to treat the result as insufficient.

**Reflection:**
- Why is the ability to recognise limits essential?
- Under what conditions should a generated solution be rejected even if it appears mostly correct?

**Principle focus:** Independent judgement and recognition of limits.

---

## Lesson 5.6 – Mini-Project: Structured Generation under Real Constraints

**Duration:** 50–70 minutes

**Goal:** Apply the full cycle of structured request design, examination, and refinement to a small tool that enforces meaningful rules. Begin to notice when a more fluid expression of the same principles might be useful.

**Expected outcomes**  
By the end of this lesson you should be able to:
- Write a complete description of a small tool that enforces at least two real rules.
- Convert the description into a high-quality structured request (Purpose, Rules, Examples, Constraints, Self-check).
- Obtain, examine, and refine the solution at least once through improved request design.
- Produce a final evaluation of acceptability.
- Reflect on one place where a more narrative or fluid style of prompting might have been equally or more effective.

**Project brief**  
Design a small tool that enforces at least two genuine rules. Suitable examples include a scoring system with maximum values, a converter that rejects impossible inputs, or a tracker that never allows negative quantities.

**Activity:**
1. Write a complete description of the tool.
2. Convert it into a structured request using the five sections practised earlier.
3. Obtain a solution and examine it systematically.
4. Refine the request design at least once and obtain an improved solution.
5. Write a final evaluation stating whether the solution is acceptable and why.
6. Note one insight about when rigid structure helps most and when a more fluid style might serve better.

**Reflection:**
- How did the quality of the initial structured request affect the number of iterations required?
- What durable habit from this module will you carry into every future use of generative tools?

**Principle focus:** Full application of prompt engineering as system design, with awareness that the same principles can later be expressed more fluidly.

---

## Module 05 Completion Check

Before moving to Module 06, confirm that you can:

- Convert a clear description into a structured request containing Purpose, Rules, Examples, Constraints, and Self-check.
- Examine a generated solution systematically against every rule and example.
- Improve results by refining the request design rather than by manually correcting every detail.
- Recognise limits and retain independent judgement.
- Begin to see how the same principles can be expressed more fluidly for tasks that benefit from narrative clarity.

Record a short reflection on the difference between a casual request and a deliberately designed request.
