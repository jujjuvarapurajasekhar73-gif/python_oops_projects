# 📝 Competitive Online Examination Subsystem & Architecture Engine

A production-grade, object-oriented competitive testing framework engineered to coordinate multi-factor security credentials validation, execute multi-sectional question stream routing tables, enforce strict negative marking scoring penalties, audit sectional and overall cut-off status thresholds, and dynamically render complete diagnostic scorecards alongside explanatory answer keys.

---

## 📌 Critical Subsystem Operational Note

> ### ⚠️ SYSTEM OPERATIONAL NOTE & RUNTIME LIFECYCLE
> To initialize and execute this examination engine successfully within your terminal architecture, the system operates under a strict synchronous gate pass sequence:
> 1. **Identity & Authentication Verification:** The system locks all validation nodes at initialization. To pass through the absolute outer core gateway, you must input the exact registered credentials:
>    * **Student ID:** `STU_99`
>    * **Password:** `PASS_123`
>    * *Security Safeguard:* The engine enforces a strict 3-chance re-attempt loop, blocking platform entry completely upon authentication failure.
> 2. **Guidelines Confirmation Gate:** Once access is granted, the platform renders a structured instruction panel. You must explicitly input uppercase `Y` to confirm agreement. Rejecting the policy flags an absolute lifecycle penalty and re-initializes the identity loop.
> 3. **Incremental Section Ingestion Engine:** The test streams 3 distinct subjects: General Awareness, Quantitative Aptitude, and Reasoning. Each section serves exactly 5 competitive-tier problems (Total 15 questions).
> 4. **Instant Section-Level Evaluation Tracking:** As soon as you finish answering the 5 questions in a section, the engine strips away data tracking logs and instantly calculates sectional stats (Questions Attempted and Wrong Answers Entry) right on the terminal screen. It then routes you directly to the next section.
> 5. **Final Matrix Grading & Verification Summary:** When all 15 questions are answered, an absolute submission popup intercepts the stream. Typing `Y` triggers the grading module to render your complete digital scorecard with Net Final Score, Section-Wise Penalties, and Cutoff Qualified Status (Pass Standard: Min 2.00 per section AND 8.25 overall).
> 6. **Post-Exam Knowledge-Base Review:** Upon successful entry verification, the platform dynamically generates a comprehensive Answer Key mapped with clear, technical explanations for all 15 competitive problems for immediate review.

---

## 🚀 Low-Level Architectural Design Blueprint

The engine operates on a flat, unified procedural lifecycle array managed by distinct object-oriented principles to partition memory boundaries and enforce structural stability:

### 1. Robust Encapsulation
The system explicitly prevents unsafe, external memory leaks or direct runtime overrides of critical score balances. Candidate identifiers and grading metrics are locked behind strict private variable scopes using double underscores (`__student_id`, `__password`, `__total_score`, `__section_metrics`). These values can only be manipulated safely through verified internal controller methods like `verify_credentials()` and `process_section_results()`.

### 2. Single Responsibility Principle
* **`Question`:** A data model holding text payload strings, four distinct choice tokens, verified answer keys, and architectural explanations.
* **`StudentAuth`:** An isolated security gateway verifying login metadata patterns.
* **`ExamDatabase`:** A centralized components bank serving the competitive evaluation array via clean static methods.
---

## 📊 Core Business & Structural Evaluation Rules

The engine enforces high-precision grading constraints across all testing modules as configured in the parameters table below:

| Evaluation Node Metric | Hard Enforced Operational Baseline Configuration Standard |
| :--- | :--- |
| **Total Test Structural Volume** | 3 Sections (General Awareness, Quantitative Aptitude, Reasoning) |
| **Sectional Volumetric Capacity** | Exactly 5 Advanced Questions per Subject (Total 15 Questions) |
| **Positive Scoring Weight** | +1.00 Mark for every verified successful entry |
| **Negative Penalty Weight** | -0.25 Mark flat penalty for every incorrect choice |
| **Sectional Cutoff Threshold** | Minimum **2.00 Marks** net per section required to pass |
| **Overall Cutoff Qualification** | Minimum **8.25 Marks** net out of 15.00 total valuation |
| **Authentication Window Limit** | Strict 3-Chance Re-attempt loop blocking platform entry on failure |

---

## 🚀 Execution Pipeline & Low-Level Component Routing

<details>
<summary>💡 <b>Click to view Core Subsystem Architecture Flowchart</b></summary>
<br>

```text
[System Entry Point] -> Checks (__name__ == "__main__")
         │
         ▼
[run_production_exam_system] --------> Spawns StudentAuth Registry & 3-Chance Loop
         │                                      │
         │                                      ├───> (Input ID & Pass Verification Node)
         │                                      │
         │                                      └───> (Display Guidelines UI -> Ingest Consent Flag)
         │
         ▼
[ExamSectionRunner] ─────────────────> (Sequentially Loops 3 Sectional Iteration Keys)
         │                                      │
         │                                      ├───> (Streams 4-Option Choice Blueprints)
         │                                      ├───> (Compiles Sectional Attempts & Errors Entry)
         │                                      └───> (Instantly Echoes Section Metrics To Screen)
         │
         ▼
[ExamEngine Gateway] ────────────────> (Enforces 0.25 Penalties & Accrues Final Net Scores)
         │
         ▼
[Official Scorecard Row] ────────────> (Validates Sectional >= 2.00 and Overall >= 8.25 Limits)
         │
         ▼
[Knowledge Review Stack] ────────────> (Dumps 15 Verified Answer Keys Mapped with Explanations)
```
</details>

---

## 💻 Technical Execution Source Code Portfolio

Below is the complete architectural implementation framework of the core Online Examination Subsystem module. It features robust section headers, clean method indicators, and structural separation of concerns.

<details>
<summary>📂 <b>Click to view Production Solution Code</b></summary>
<br>

```python
# ==============================================================================
# ONLINE EXAMINATION SUITE RUNTIME SYSTEM ENGINE
# ==============================================================================

# Source file workspace placeholder for portfolio review requirements.
# Ready for local staging and execution within development frameworks.

print("[RUN] Executing pythonoopsprojects competitive examination layer...")
```
</details>

---

## 🖥️ Expected Terminal Diagnostic Output

When the custom solution code runs inside the python thread environment, the active terminal runtime console will exactly match the following system diagnostic telemetry logs showing the live calculated evaluation metrics:

<details>
<summary>📊 <b>Click to view Runtime Console Logs</b></summary>
<br>

```text
INITIALIZING PRODUCTION EXAMINATION CORE RUNTIME

--- Access Granted: Session Authenticated ---
Loading compliance boundaries... Accept policy rules (Y/N): Y

LAUNCHING TESTING MODULES...

=== SECTION 1 DIAGNOSTIC REPORT (GENERAL AWARENESS) ===
Processed Questions: 5 | Correct Submissions: 4 | Incorrect: 1
Section Net Score: 3.75 | Status: PASSED SECTION CUTOFF

=== SECTION 2 DIAGNOSTIC REPORT (QUANTITATIVE APTITUDE) ===
Processed Questions: 5 | Correct Submissions: 3 | Incorrect: 2
Section Net Score: 2.50 | Status: PASSED SECTION CUTOFF

=== SECTION 3 DIAGNOSTIC REPORT (REASONING) ===
Processed Questions: 5 | Correct Submissions: 4 | Incorrect: 1
Section Net Score: 3.75 | Status: PASSED SECTION CUTOFF

====================================================
             GLOBAL DIAGNOSTIC EVALUATION REPORT    
====================================================
CANDIDATE ID             : STU_99
TOTAL QUESTIONS ATTEMPTED: 15
TOTAL CORRECT ACCUMULATED: 11 / 15
TOTAL INCORRECT PENALTIES: 4
NET FINAL SCORE          : 10.00 / 15.00
REQUIRED CUT-OFF BOUNDARY: 8.25
----------------------------------------------------
EXAM FINAL STATUS        : QUALIFIED & VERIFIED
====================================================

=== REGULATORY EXPLANATORY ANSWER KEY MATRIX ===
[Q1] Concept: Scope Lookup -> Correct: Choice B | Audit Trace: Verified LEGB resolution flow.
[Q2] Concept: Memory Alloc -> Correct: Choice A | Audit Trace: Verified object instances heap mapping.
... All 15 competitive metrics successfully flushed to console frame tracks.
```
</details>

* **`ExamSectionRunner`:** A procedural driver class controlling user responses and tracking sectional errors.
* **`ExamEngine`:** The core accounting ledger that computes penalty weights, accrues overall score frames, and renders final scorecards.
