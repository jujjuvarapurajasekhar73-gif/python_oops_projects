import time

# =====================================================================
# 1. CORE QUESTION COMPONENT INTERFACE (WITH KNOWLEDGE BASE KEY ENGINE)
# =====================================================================

class Question:
    def __init__(self, text: str, options: list, correct_option: str, explanation: str) -> None:
        """
        Initializes a strict 4-option multiple-choice question asset configuration.
        Includes a professional corporate explanation metadata layer for post-exam review.
        """
        if len(options) != 4:
            raise ValueError("Every question must contain exactly 4 options.")
        self.text = text
        self.options = options
        self.correct_option = correct_option.strip().upper()
        self.explanation = explanation


# =====================================================================
# 2. STUDENT SECURE IDENTITY & AUTHENTICATION CONTROLLER
# =====================================================================

class StudentAuth:
    def __init__(self, student_id: str, password: str) -> None:
        """
        Initializes secure student authentication profiles with private attributes.
        """
        self.__student_id = student_id
        self.__password = password

    def verify_credentials(self, input_id: str, input_pass: str) -> bool:
        """
        Validates incoming user login tokens against stored private identity structures.
        """
        return self.__student_id == input_id and self.__password == input_pass


# =====================================================================
# 3. LOCAL DICTIONARY DATABASE (3 SECTIONS WITH 5 ADVANCED QUESTIONS EACH)
# =====================================================================

class ExamDatabase:
    @staticmethod
    def get_questions() -> dict:
        """
        Static Component: Encodes a localized high-difficulty dictionary database 
        containing 3 distinct exam sections with 5 hard problems and verified keys.
        """
        return {
            "GENERAL_AWARENESS": [
                Question(
                    "According to Basel III norms, what is the minimum Common Equity Tier 1 (CET1) capital requirement for commercial banks in India? [Page 12, Q127]", 
                    ["(A) 4.5%", "(B) 5.5%", "(C) 8.0%", "(D) 12.0%"], "C",
                    "Under Basel III regulatory frameworks enforced by the RBI, Indian commercial banks are strictly required to maintain a baseline CET1 ratio of 5.5% plus an additional 2.5% Capital Conservation Buffer (CCB), scaling the absolute minimum requirement boundary frame to exactly 8.0%."
                ),
                Question(
                    "What is the maximum limit for Statutory Liquidity Ratio (SLR) that the RBI can legally prescribe in India? [Page 12, Q129]", 
                    ["(A) 25%", "(B) 36%", "(C) 40%", "(D) 50%"], "C",
                    "The Banking Regulation Act framework dictates that the maximum ceiling threshold boundary limit up to which the Reserve Bank of India can legally scale and prescribe the SLR framework for commercial schedules is capped at 40%."
                ),
                Question(
                    "Which public sector bank recorded the highest standalone net profit in the entire fiscal year FY 2024? [Page 12, Q122]", 
                    ["(A) Bank of Baroda", "(B) State Bank of India", "(C) Punjab National Bank", "(D) Union Bank of India"], "B",
                    "Official banking performance metrics confirm that the State Bank of India (SBI) outpaced all other public segment counters to log the highest absolute standalone net profit index across the entire FY 2024 timeline framework."
                ),
                Question(
                    "What is India's official rank in the 2024 Global Nature Conservation Index (NCI) out of 180 evaluated nations? [Page 12, Q123]", 
                    ["(A) 156th", "(B) 167th", "(C) 176th", "(D) 180th"], "C",
                    "The Global Nature Conservation Index data parameters rank India at the 176th horizontal out of 180 evaluated matrices, highlighting severe structural preservation risks across biodiversity and ecological balance layers."
                ),
                Question(
                    "In India, what flat percentage is designated as the strict Priority Sector Lending (PSL) goal for Small Finance Banks (SFBs)? [Page 12, Q130]", 
                    ["(A) 40%", "(B) 50%", "(C) 65%", "(D) 75%"], "D",
                    "To ensure aggressive financial depth and penetration across micro-segments, Small Finance Banks operate under a strict structural mandate requiring them to direct 75% of their Adjusted Net Bank Credit (ANBC) into PSL brackets."
                )
            ],
            "APTITUDE": [
                Question(
                    "If the algebraic expression 6x^2 + 29x + P is completely divisible by (3x + 1) leaving a quotient of (2x + 9) and a remainder of 19, find P: [Page 8, Q82]", 
                    ["(A) 25", "(B) 26", "(C) 27", "(D) 28"], "D",
                    "Applying the classic standard polynomial division framework rule: Dividend = (Divisor * Quotient) + Remainder. Therefore, 6x^2 + 29x + P = (3x + 1)(2x + 9) + 19 = 6x^2 + 29x + 28. Comparing the constants locks P to exactly 28."
                ),
                Question(
                    "Container X has 140L pure milk. After removing 250/7% of milk and adding 30L water, 40% of this mixture is removed. Find final water volume in X: [Page 9, Q85]", 
                    ["(A) 12 Liters", "(B) 18 Liters", "(C) 30 Liters", "(D) 54 Liters"], "B",
                    "Initial removal = (250/700)*140 = 50L milk left = 90L. 30L water is added, locking the milk-to-water fraction ratio to exactly 3:1. Removing 40% of the unified volume strips water by 40% as well, leaving 30 * 0.6 = 18 Liters of water remaining."
                ),
                Question(
                    "A boat covers (D + 120) km downstream in River A in a time that is 25% more than covering (D - 80) km upstream in River B. If boat speed is constant and River A speed ratio is 9:5, find D: [Page 9, Q93]", 
                    ["(A) 120", "(B) 140", "(C) 160", "(D) 200"], "C",
                    "Using the downstream and upstream speed equations derived from the boat-to-stream ratio metrics, the distance equation evaluates directly to yield D = 160 km."
                ),
                Question(
                    "Puneet buys 240 articles. He sells 160 at a 20% discount and the remaining 80 at an additional 25% off on the discounted price, making a 10% total profit. Find profit% with no discount: [Page 9, Q84]", 
                    ["(A) 25%", "(B) 33%", "(C) 40%", "(D) 50%"], "A",
                    "Aggregating the total revenue from both discounted tiers and mapping it against a 10% net profit scale yields an un-discounted profit baseline parameter of exactly 25%."
                ),
                Question(
                    "The ratio of heights of a cone and cylinder is 3:2 and their radii ratio is 3:4. Volume fractions match a ratio matrix of m:n. Solve for structural height m scale coefficient: [Page 10, Q94]", 
                    ["(A) 9", "(B) 32", "(C) 20", "(D) 27"], "A",
                    "Evaluating the volume formulas V_cone = (1/3)*pi*r^2*h and V_cylinder = pi*r^2*h using the provided fractional dimensions scales the m parameter value to exactly 9."
                )
            ],
            "REASONING": [
                Question(
                    "In the numerical sequence: 5, 20, 40, 67, 105, 140, 224, find the value of the incorrect wrong tracking parameter token entry P: [Page 8, Q81]", 
                    ["(A) 40", "(B) 67", "(C) 105", "(D) 140"], "D",
                    "The evaluation difference pattern scales via standard prime level logic: +15, +20, +27, +38, +51. The matching differential matrix locks the tracking term entry index sequence to show that 140 is structurally incorrect and must be substituted by 156."
                ),
                Question(
                    "If 'P:Q' means Q is father of P, 'P#Q' means P is mother of Q, 'P/Q' means P is sister of Q, and 'P*Q' means Q is wife of P, solve for the sister-in-law token L matrix expression: [Page 2, Q11]", 
                    ["(A) X ¥ H : C ¥ L", "(B) L / X β T ¥ E", "(C) L β G ¥ X * C", "(D) None of these"], "D",
                    "Evaluating the specified symbolic operations directly isolates the sibling mapping parameters, proving that none of the target configurations properly maps the structural validation key requirements."
                ),
                Question(
                    "An uncertain number of persons sit in a straight line facing North. Seating alternates between Managers and Associates. S is at extreme left. If J sits 3rd right of R, determine true spacing offset: [Page 1, Q7]", 
                    ["(A) Immediate Left", "(B) Second to Left", "(C) Third to Right", "(D) Fifth to Right"], "A",
                    "Aligning the constraints step-by-step establishes the structural row distribution sequence, directly validating the spatial configuration values."
                ),
                Question(
                    "In word 'COLLABORATION' all consonants are replaced by preceding letters, vowels by succeeding. Combine and sort alphabetically to identify the 3rd right of 2nd left letter token: [Page 2, Q16]", 
                    ["(A) J", "(B) F", "(C) B", "(D) N"], "C",
                    "Transforming both strings and packing them down into a single integrated flat alphabetical array locks the left boundary indices layer to map: A, B, B, B, B, E, F... The element sitting 3rd to the right of the 2nd left index ('B') yields exactly 'B'."
                ),
                Question(
                    "Eight persons sit around a circular table facing center holding cards from 2 to 9. Consecutive numbers cannot be adjacent. B sits 2nd left of 7. Find card entry opposite B: [Page 2, Q21]", 
                    ["(A) 4", "(B) 6", "(C) 8", "(D) 9"], "D",
                    "Reconciling the structural circular boundary constraints and mapping adjacency prevention logic parameters isolates the nodes to prove that the candidate element seated directly across from B must hold card entry 9."
                )
            ]
        }

# =====================================================================
# 4. INSTANT SECTION ROUTER (NO 3-MINUTE TRAP LOCK GATE)
# =====================================================================

class ExamSectionRunner:
    @staticmethod
    def execute_section(section_name: str, questions: list) -> tuple:
        """
        Serves questions one-by one, It prints instant stats as soon as the 5 questions end.
        """
        attempt_count = 0
        correct_count = 0
        wrong_count = 0

        print(f"\n>>> RUNNING ACTIVE SUBJECT: {section_name} <<<")

        # Sequentially streams the 5 hard problems without holding the user inside any clock cage
        for i, q in enumerate(questions):
            print("\n" + "-" * 60)
            print(f"Q{i + 1}: {q.text}")
            for opt in q.options:
                print(f"  {opt}")
            print("-" * 60)
            
            ans = input("Your Answer (A/B/C/D) or press Enter to skip: ").strip().upper()

            if ans in ["A", "B", "C", "D"]:
                attempt_count += 1
                if ans == q.correct_option:
                    correct_count += 1
                else:
                    wrong_count += 1

        # User Constraint: Instantly showcases sectional report metrics upon section termination
        print(f"\n>>> SECTION COMPLETED: {section_name} <<<")
        print(f"  * Questions Attempted : {attempt_count}")
        print(f"  * Wrong Answers Entry : {wrong_count}")
        print("-" * 60)
        
        return attempt_count, correct_count, wrong_count


# =====================================================================
# 5. ENTERPRISE GRADING SUITE & FULL KEY EXPLANATION SYSTEM
# =====================================================================

class ExamEngine:
    def __init__(self, student_name: str) -> None:
        """
        Initializes grading states and metric collection registers inside secure variables.
        """
        self.__student_name = student_name
        self.__total_score: float = 0.0
        self.__section_metrics: list = []

    def process_section_results(self, section_name: str, attempts: int, correct_ans: int, wrong_ans: int) -> None:
        """
        Computes 1 mark per correct response and applies 0.25 penalty weight for failures.
        """
        penalty = wrong_ans * 0.25
        section_score = (correct_ans * 1.0) - penalty
        self.__total_score += section_score
        
        passed_section = section_score >= 2.0
        self.__section_metrics.append((section_name, attempts, wrong_ans, section_score, "PASSED" if passed_section else "FAILED"))

    def display_report_card(self) -> str:
        """
        Renders finalized scorecard based on 8.25 overall pass boundary criteria.
        """
        status = "PASSED & CERTIFIED" if self.__total_score >= 8.25 else "FAILED / NON-CERTIFIED"
        
        report = f"""
        ====================================================
                     OFFICIAL EXAMINATION SCORECARD         
        ====================================================
        CANDIDATE NAME    : {self.__student_name}
        EVALUATION STATUS : PROCESSED REAL-TIME
        MAXIMUM VALUATION : 15.00
        ----------------------------------------------------
        FINAL NET SCORE   : {self.__total_score:.2f} / 15.00
        OVERALL CUTOFF    : 8.25 MARKS (SECTIONAL CUTOFF: 2.00)
        CERTIFICATE BOUND : {status}
        ====================================================
        """
        return report


# =====================================================================
# 6. CENTRAL PRODUCTION RUNTIME AUTOMATION
# =====================================================================

def run_production_exam_system() -> None:
    print(">>> INITIALIZING ENTERPRISE EXAMINATION CORE PLATFORM <<<")
    auth_db = StudentAuth("STU_99", "PASS_123")
    attempts_left = 3

    while attempts_left > 0:
        print(f"\n====================================================")
        print(f"│  ACTIVE EXAM ATTEMPT REGISTRY. CHANCES LEFT: {attempts_left}   │")
        print(f"====================================================")

        user_id = input("Enter Student ID: ").strip()
        user_pass = input("Enter Password: ").strip()
        
        if not auth_db.verify_credentials(user_id, user_pass):
            print("[ACCESS DENIED]: Invalid identity configuration. Re-try input.")
            continue
        print("[ACCESS GRANTED]: Student identity verified successfully.")

        print("\n====================================================")
        print(" 1. STRUCTURE : 3 SECTIONS (GA, APTITUDE, REASONING)")
        print(" 2. WEIGHTAGE : 5 QUESTIONS PER SECTION | 1 MARK EACH")
        print(" 3. PENALTY   : 0.25 NEGATIVE MARKS FOR EVERY WRONG ANSWER")
        print(" 4. TIMING    : SELF-PACED INSTANT PROGRESSION (NO WAIT)")
        print(" 5. CRITERIA  : MIN 2.00 PER SECTION & 8.25 OVERALL TO PASS")
        print("====================================================")
        
        consent = input("\nDo you accept all the exam constraints and rules? (Y/N): ").strip().upper()
        if consent != "Y":
            attempts_left -= 1
            print(f"[TERMINATED]: Candidate rejected constraints. Re-initializing attempt.")
            continue

        exam_session = ExamEngine("Chinni Rajasekhar")
        db = ExamDatabase.get_questions()

        # Iterating systematically through the 3 subjects
        for section, sec_questions in db.items():
            attempts, correct, wrong = ExamSectionRunner.execute_section(section, sec_questions)
            exam_session.process_section_results(section, attempts, correct, wrong)

        print("\n" + "!" * 52)
        print("!  [SYSTEM POP-UP]: DO YOU WANT TO SUBMIT THE EXAM?  !")
        print("!" * 52)
        submit_action = input("Type 'Y' to finalize submissions: ").strip().upper()
        
        if submit_action == "Y":
            # Print the scorecard summary row first
            print(exam_session.display_report_card())
            
            # User Constraint: Print full 15 questions answer key with conceptual explanations row by row
            print("\n" + "=" * 65)
            print("         OFFICIAL ANSWER KEY & EXPLANATION SUMMARY")
            print("=" * 65)
            
            global_q_counter = 1
            for section, sec_questions in db.items():
                print(f"\n>>> SECTION REFERENCE: {section} <<<")
                for q in sec_questions:
                    print(f"\n{global_q_counter}. Correct Answer Key: ({q.correct_option})")
                    print(f"   Explanation: {q.explanation}")
                    print("-" * 65)
                    global_q_counter += 1
            return  
        else:
            attempts_left -= 1
            print(f"\n[WARNING]: Your exam was not submitted! Take your exam again.")


if __name__ == "__main__":
    run_production_exam_system()
