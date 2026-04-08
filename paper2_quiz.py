#!/usr/bin/env python3
"""
OCR J277/02 — Infinite Theory Question Bank
Built from 2022-2025 past paper analysis and custom priority specification.
Tier 1 topics (guaranteed every year) are weighted 3x more likely to appear.
"""

import random
import os

# ── Colours ───────────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# ── Question Bank ─────────────────────────────────────────────────────────────
# type: "mc"        — multiple choice (A/B/C/D)
# type: "self_mark" — open-ended, user self-marks against model answer
# tier: 1 = guaranteed every year, 2 = very likely, 3 = rotates
# ─────────────────────────────────────────────────────────────────────────────

QUESTIONS = [

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — SELECTION VS ITERATION
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "Which of the following is an example of SELECTION?",
        "options": ["for i = 1 to 10", "while x < 5", "if score > 50 then", "do ... until done"],
        "answer": 2,
        "explanation": "if/then/else/endif is selection — it chooses a path. for, while, and do-until are all iteration (repetition)."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "Which of the following is an example of ITERATION?",
        "options": ["if x == 0 then", "switch name ... endswitch", "while total < 100", "elseif score > 50"],
        "answer": 2,
        "explanation": "while is a condition-controlled loop — it repeats while the condition is true. if/switch/elseif are selection."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "What does the MOD operator return?",
        "options": ["The result of multiplication", "The remainder after integer division", "The rounded-down result of division", "The absolute value"],
        "answer": 1,
        "explanation": "MOD returns the remainder after division. e.g. 10 MOD 3 = 1. Used to check odd/even: num MOD 2 == 0 means even."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "In OCR pseudocode, what operator raises a number to a power?",
        "options": ["**", "^", "POW", "^^"],
        "answer": 1,
        "explanation": "OCR ERL uses ^ for exponentiation. e.g. 2^8 = 256. Python uses ** but OCR pseudocode always uses ^."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "A `do...until` loop is which type of programming construct?",
        "options": ["Selection", "Sequence", "Iteration", "Declaration"],
        "answer": 2,
        "explanation": "do...until is a post-condition loop (iteration). It always executes at least once, then checks the condition at the end."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "Which keyword creates a COUNT-CONTROLLED loop in OCR pseudocode?",
        "options": ["while", "if", "for", "do"],
        "answer": 2,
        "explanation": "for...next is count-controlled — repeats a fixed number of times. while and do-until are condition-controlled."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "A `switch...endswitch` statement is which type of construct?",
        "options": ["Iteration", "Selection", "Sequence", "Subroutine"],
        "answer": 1,
        "explanation": "switch/case is selection — it selects one branch to execute based on the value of a variable."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "What is the correct OCR pseudocode to increment a variable called `score` by 1?",
        "options": ["score == score + 1", "score = score + 1", "score + 1", "increment score"],
        "answer": 1,
        "explanation": "score = score + 1 assigns the new value. == is comparison, not assignment. You could also write score += 1."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "In OCR pseudocode, what does DIV do?",
        "options": ["Returns the remainder", "Returns the result of integer division (no decimal)", "Divides two Real numbers", "Declares a variable as integer"],
        "answer": 1,
        "explanation": "DIV performs integer division and discards the remainder. e.g. 17 DIV 5 = 3. MOD gives the remainder (17 MOD 5 = 2)."
    },
    {
        "topic": "Selection vs Iteration",
        "tier": 1,
        "type": "mc",
        "q": "Tick which construct: `while NOT endOfFile()`",
        "options": ["Selection", "Iteration", "Sequence", "Assignment"],
        "answer": 1,
        "explanation": "while is iteration — it loops while the condition is true (i.e. while the file still has lines to read)."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — LOGIC GATES & BOOLEAN LOGIC
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "What does an AND gate output when inputs are A=1, B=1?",
        "options": ["0", "1", "Undefined", "Depends on a third input"],
        "answer": 1,
        "explanation": "AND: output is 1 ONLY when ALL inputs are 1. 1 AND 1 = 1."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "What does an AND gate output when inputs are A=1, B=0?",
        "options": ["0", "1", "A", "B"],
        "answer": 0,
        "explanation": "AND: output is 1 only when BOTH inputs are 1. Since B=0, output is 0."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "What does a NOT gate output when the input is 0?",
        "options": ["0", "1", "Null", "Error"],
        "answer": 1,
        "explanation": "NOT inverts the input. NOT 0 = 1, NOT 1 = 0."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "For P = A OR B, what is the output when A=0 and B=0?",
        "options": ["0", "1", "A", "Undefined"],
        "answer": 0,
        "explanation": "OR outputs 1 if AT LEAST ONE input is 1. Both are 0, so output is 0."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "For P = A OR B, what is the output when A=0 and B=1?",
        "options": ["0", "1", "B", "Undefined"],
        "answer": 1,
        "explanation": "OR outputs 1 if at least one input is 1. B=1, so output is 1."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "How many rows are needed in a truth table for a Boolean expression with 3 inputs?",
        "options": ["3", "6", "8", "16"],
        "answer": 2,
        "explanation": "Rows = 2^n where n = number of inputs. 2^3 = 8 rows."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "How many rows are needed in a truth table with 2 inputs?",
        "options": ["2", "4", "8", "16"],
        "answer": 1,
        "explanation": "2^2 = 4 rows. The combinations are: 00, 01, 10, 11."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "A XOR gate outputs 1 when...",
        "options": ["Both inputs are 1", "Both inputs are 0", "The inputs are DIFFERENT", "At least one input is 1"],
        "answer": 2,
        "explanation": "XOR (Exclusive OR) outputs 1 only when inputs are DIFFERENT (one 0 and one 1). Same inputs → output 0."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "What is the output of a NAND gate when both inputs are 1?",
        "options": ["0", "1", "Same as AND", "Error"],
        "answer": 0,
        "explanation": "NAND = NOT AND. AND(1,1) = 1, so NAND(1,1) = NOT 1 = 0."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "Which gate produces the OPPOSITE output to an OR gate?",
        "options": ["XOR", "NAND", "NOR", "NOT"],
        "answer": 2,
        "explanation": "NOR = NOT OR. It outputs the complement of what OR would give."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "For P = (A OR B) AND NOT C, what is P when A=1, B=0, C=1?",
        "options": ["0", "1", "Cannot determine", "Depends on D"],
        "answer": 0,
        "explanation": "A OR B = 1. NOT C = NOT 1 = 0. 1 AND 0 = 0. P = 0."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "For P = A AND NOT B, what is P when A=1 and B=0?",
        "options": ["0", "1", "Undefined", "Same as B"],
        "answer": 1,
        "explanation": "NOT B = NOT 0 = 1. A AND 1 = 1 AND 1 = 1. P = 1."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "For P = NOT A AND (B OR C), what is P when A=0, B=1, C=0?",
        "options": ["0", "1", "Undefined", "Error"],
        "answer": 1,
        "explanation": "NOT A = NOT 0 = 1. B OR C = 1 OR 0 = 1. 1 AND 1 = 1. P = 1."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "self_mark",
        "q": "Describe the purpose of a truth table. [2 marks]",
        "answer": "A truth table shows every possible combination of input values and the resulting output(s) for a Boolean/logic expression or circuit.\nIt is used to determine what output a logic gate or circuit produces for all possible input combinations.",
        "explanation": "1 mark: shows all possible input combinations. 1 mark: shows the corresponding output for each combination."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "How many rows would a truth table for the expression P = A AND B AND C need?",
        "options": ["3", "6", "8", "9"],
        "answer": 2,
        "explanation": "3 inputs → 2^3 = 8 rows. Always 2^n for n inputs."
    },
    {
        "topic": "Logic Gates",
        "tier": 1,
        "type": "mc",
        "q": "A NOR gate with inputs A=0 and B=0 outputs...",
        "options": ["0", "1", "Same as OR", "Error"],
        "answer": 1,
        "explanation": "NOR = NOT OR. OR(0,0) = 0. NOT 0 = 1. NOR(0,0) = 1."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — TRACE TABLES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Trace Tables",
        "tier": 1,
        "type": "mc",
        "q": "In a trace table, when do you write a value in a variable's column?",
        "options": ["Every line", "Only on the first line", "Only when the variable's value changes", "At the end of each loop"],
        "answer": 2,
        "explanation": "Only fill a cell when the variable's value changes. Blank means it's unchanged from the last entry."
    },
    {
        "topic": "Trace Tables",
        "tier": 1,
        "type": "mc",
        "q": "What is the final value of `total` after this runs?\ntotal = 0\nfor i = 1 to 3\n    total = total + i\nnext i",
        "options": ["3", "6", "9", "0"],
        "answer": 1,
        "explanation": "i=1: total=1. i=2: total=3. i=3: total=6. Final total = 6."
    },
    {
        "topic": "Trace Tables",
        "tier": 1,
        "type": "mc",
        "q": "A variable `total = 0` is placed INSIDE a loop that runs 5 times, adding scores each iteration. What is the problem?",
        "options": ["The loop never terminates", "total resets to 0 at the start of each iteration — it never accumulates", "total will be negative", "The loop runs one extra time"],
        "answer": 1,
        "explanation": "This is a classic logic error tested in 2022 and 2023. total = 0 inside the loop resets the running total every iteration."
    },
    {
        "topic": "Trace Tables",
        "tier": 1,
        "type": "mc",
        "q": "A loop is `for count = 1 to scores.length`. The array has 5 elements (indexes 0–4). What element is missed?",
        "options": ["scores[5]", "scores[0]", "scores[4]", "No element is missed"],
        "answer": 1,
        "explanation": "Arrays are 0-indexed. Starting at count=1 skips scores[0] (the first element). Should be `for count = 0 to scores.length - 1`."
    },
    {
        "topic": "Trace Tables",
        "tier": 1,
        "type": "self_mark",
        "q": "Trace through this algorithm when x = 5:\n\nresult = 1\nwhile x > 0\n    result = result * x\n    x = x - 1\nendwhile\nprint(result)\n\nWrite the values of x and result for each iteration, and state the final output.",
        "answer": "Start: result=1, x=5\nIter 1: result=5, x=4\nIter 2: result=20, x=3\nIter 3: result=60, x=2\nIter 4: result=120, x=1\nIter 5: result=120, x=0  ← loop ends (x=0, NOT > 0)\nOutput: 120",
        "explanation": "This computes 5! (5 factorial) = 120. Track each variable in separate columns. Only write when value changes."
    },
    {
        "topic": "Trace Tables",
        "tier": 1,
        "type": "mc",
        "q": "What is the output of this algorithm?\n\ncount = 0\ndo\n    count = count + 1\nuntil count == 3\nprint(count)",
        "options": ["0", "2", "3", "4"],
        "answer": 2,
        "explanation": "do-until runs at least once. count goes: 1 (check: 1==3? No), 2 (check: 2==3? No), 3 (check: 3==3? Yes → stop). Output: 3."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — LOGIC ERRORS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Logic Errors",
        "tier": 1,
        "type": "mc",
        "q": "What is a LOGIC error?",
        "options": [
            "An error in the spelling of a keyword",
            "An error where the program crashes while running",
            "An error where the program runs but produces incorrect results",
            "An error that prevents the code from compiling"
        ],
        "answer": 2,
        "explanation": "A logic error means the code runs without crashing but gives wrong output. The syntax is correct but the logic is flawed."
    },
    {
        "topic": "Logic Errors",
        "tier": 1,
        "type": "mc",
        "q": "What is a SYNTAX error?",
        "options": [
            "The program runs but gives wrong output",
            "The program breaks a rule of the programming language",
            "The program runs out of memory",
            "The program enters an infinite loop"
        ],
        "answer": 1,
        "explanation": "A syntax error breaks the grammar rules of the language (e.g. missing bracket, misspelled keyword). The code cannot be run."
    },
    {
        "topic": "Logic Errors",
        "tier": 1,
        "type": "mc",
        "q": "What is a RUNTIME error?",
        "options": [
            "Prevents the code from being compiled",
            "Produces wrong output silently",
            "Causes the program to crash during execution",
            "Makes the program run slower"
        ],
        "answer": 2,
        "explanation": "A runtime error occurs during execution — the program starts but crashes (e.g. dividing by zero, index out of range)."
    },
    {
        "topic": "Logic Errors",
        "tier": 1,
        "type": "mc",
        "q": "Which of the following is a LOGIC error?",
        "options": [
            "Writing `pint` instead of `print`",
            "Missing a closing bracket",
            "Using `total = num1 + num1` instead of `total = num1 + num2`",
            "Forgetting to close a string with a quote"
        ],
        "answer": 2,
        "explanation": "Using num1+num1 runs without error but produces the wrong result. That's a logic error."
    },
    {
        "topic": "Logic Errors",
        "tier": 1,
        "type": "mc",
        "q": "In an array-totalling algorithm, the loop is `for count = 1 to scores.length` (0-indexed array). What type of error is this?",
        "options": ["Syntax error", "Runtime error", "Logic error", "Compilation error"],
        "answer": 2,
        "explanation": "The code runs without crashing but skips scores[0] — the result is wrong. This is a logic error."
    },
    {
        "topic": "Logic Errors",
        "tier": 1,
        "type": "self_mark",
        "q": "Identify the TWO logic errors in this algorithm and write the corrected lines:\n\nLine 01: total = 0\nLine 02: for count = 0 to scores.length - 1\nLine 03:     total = 0\nLine 04:     total = total + scores[count]\nLine 05: next count\nLine 06: print(total / scores.length)",
        "answer": "Error 1: Line 03 — total = 0 is inside the loop, resetting the total every iteration.\nCorrected line 03: (delete it — total = 0 should only be on line 01, before the loop)\n\nThere is only one clear logic error here. The second error would depend on the specific question context.",
        "explanation": "The OCR mark scheme always expects: line number + corrected code. 1 mark per error identified, 1 mark per correction = 4 marks total for this question type."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — DATA TYPES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "What is the most appropriate data type for a variable storing a price (e.g. £4.99)?",
        "options": ["Integer", "Boolean", "String", "Real"],
        "answer": 3,
        "explanation": "Real (Float) is used for decimal numbers. Prices involve pence so Real is correct. Integer would lose the decimal part."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "What is the most appropriate data type for storing a phone number?",
        "options": ["Integer", "Real", "String", "Boolean"],
        "answer": 2,
        "explanation": "Phone numbers are String. They can start with 0 (which would be lost as Integer), and may contain +, spaces, or brackets."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "What data type stores only True or False?",
        "options": ["Integer", "Boolean", "Char", "String"],
        "answer": 1,
        "explanation": "Boolean stores exactly two values: True or False (also 1/0, Yes/No, on/off)."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "What is the most appropriate data type for the number of students in a class (e.g. 28)?",
        "options": ["Real", "Boolean", "Integer", "String"],
        "answer": 2,
        "explanation": "A count is a whole number — Integer. Real would allow 28.5 students which makes no sense."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "A sensor records whether it is armed or disarmed. What data type for the `armed` variable?",
        "options": ["Integer", "String", "Boolean", "Real"],
        "answer": 2,
        "explanation": "Armed/disarmed is a binary state (True/False) — Boolean."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "A student's test score is recorded to 1 decimal place (e.g. 87.5). What data type?",
        "options": ["Integer", "Boolean", "Char", "Real"],
        "answer": 3,
        "explanation": "Decimal numbers use Real (Float). Integer cannot store the .5 part."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "What data type stores a single character such as 'A' or '?'?",
        "options": ["String", "Char", "Boolean", "Integer"],
        "answer": 1,
        "explanation": "Char stores exactly one character. String stores a sequence of zero or more characters."
    },
    {
        "topic": "Data Types",
        "tier": 1,
        "type": "mc",
        "q": "A program stores a username like 'alice123'. What data type?",
        "options": ["Integer", "Char", "String", "Boolean"],
        "answer": 2,
        "explanation": "A username is text (sequence of characters) — String, even if it contains digits."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — SQL
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "SQL",
        "tier": 1,
        "type": "mc",
        "q": "Which SQL keyword filters records based on a condition?",
        "options": ["FROM", "SELECT", "WHERE", "FILTER"],
        "answer": 2,
        "explanation": "WHERE filters records. e.g. WHERE Nights > 1 returns only records where Nights exceeds 1."
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "mc",
        "q": "Which SQL keyword specifies the table to query?",
        "options": ["SELECT", "FROM", "WHERE", "TABLE"],
        "answer": 1,
        "explanation": "FROM specifies the table. e.g. FROM TblBookings."
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "mc",
        "q": 'In SQL, how must a STRING value appear in a WHERE condition?',
        "options": ['WHERE type = Door', 'WHERE type = "Door"', "WHERE type = (Door)", "WHERE type IS Door"],
        "answer": 1,
        "explanation": 'String values need quotes: WHERE type = "Door". Numeric values do NOT use quotes.'
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "mc",
        "q": "What is the correct order of clauses in a SQL SELECT statement?",
        "options": ["FROM → SELECT → WHERE", "SELECT → WHERE → FROM", "SELECT → FROM → WHERE", "WHERE → FROM → SELECT"],
        "answer": 2,
        "explanation": "Always: SELECT (fields) → FROM (table) → WHERE (condition). This order is fixed."
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "mc",
        "q": "What does `SELECT *` mean?",
        "options": ["Select nothing", "Select the first record only", "Select all fields", "Select all tables"],
        "answer": 2,
        "explanation": "SELECT * selects ALL columns/fields from the table."
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "mc",
        "q": "Which of the following SQL statements is CORRECT?",
        "options": [
            "SELECT * WHERE Nights > 1 FROM TblBookings",
            "SELECT * FROM TblBookings WHERE Nights > 1",
            "FROM TblBookings SELECT * WHERE Nights > 1",
            'SELECT * FROM TblBookings WHERE Nights = "more than 1"'
        ],
        "answer": 1,
        "explanation": "Correct order: SELECT → FROM → WHERE. Numeric conditions don't use quotes."
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "self_mark",
        "q": "Write an SQL statement to select StudentID and TeamName from a table called TblResult, where the YearGroup equals 11. [3 marks]",
        "answer": "SELECT StudentID, TeamName\nFROM TblResult\nWHERE YearGroup = 11",
        "explanation": "1 mark: SELECT StudentID, TeamName\n1 mark: FROM TblResult\n1 mark: WHERE YearGroup = 11 (no quotes — numeric value)"
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "self_mark",
        "q": 'Write an SQL statement to show all fields from TblActs where the Genre is "Rock". [3 marks]',
        "answer": 'SELECT *\nFROM TblActs\nWHERE Genre = "Rock"',
        "explanation": '1 mark: SELECT *\n1 mark: FROM TblActs\n1 mark: WHERE Genre = "Rock" (quotes needed — string value)'
    },
    {
        "topic": "SQL",
        "tier": 1,
        "type": "self_mark",
        "q": "Write an SQL statement to select SensorID from a table called Events, where SensorType is \"Door\" AND Length is greater than 20. [4 marks]",
        "answer": 'SELECT SensorID\nFROM Events\nWHERE SensorType = "Door" AND Length > 20',
        "explanation": '1 mark: SELECT SensorID\n1 mark: FROM Events\n1 mark: WHERE SensorType = "Door"\n1 mark: AND Length > 20'
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — TESTING
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "A program validates age must be between 11 and 18. Which is BOUNDARY test data?",
        "options": ["15", "11 and 18", "10 and 19", "0"],
        "answer": 1,
        "explanation": "Boundary test data tests the exact limits: 11 (lower boundary) and 18 (upper boundary). 15 is normal, 10/19 are erroneous."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "A program accepts scores from 0 to 100. Which is ERRONEOUS (invalid) test data?",
        "options": ["0", "50", "100", "150"],
        "answer": 3,
        "explanation": "Erroneous data should be rejected. 150 is outside the valid range (0–100)."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "What is NORMAL test data?",
        "options": [
            "Data at the exact boundaries of the valid range",
            "Data outside the valid range that should be rejected",
            "Typical valid data within the acceptable range",
            "Data entered by a normal user"
        ],
        "answer": 2,
        "explanation": "Normal test data is typical valid data the program should accept. e.g. for age 11–18, a normal value is 14."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "A field accepts number of nights (1 to 5). Which is BOUNDARY test data?",
        "options": ["3", "0", "5", "10"],
        "answer": 2,
        "explanation": "5 is the upper boundary. 1 is the lower boundary. 3 is normal. 0 and 10 are erroneous."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "A field accepts integers 1–100. Classify the test data '\"Hello\"':",
        "options": ["Normal", "Boundary", "Erroneous/Invalid", "Extreme"],
        "answer": 2,
        "explanation": "'Hello' is a string — completely wrong data type for an integer field. This is erroneous/invalid test data."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "Why should a program be tested before release?",
        "options": [
            "To make it run faster",
            "To find and fix errors so the program works correctly and doesn't cause problems for users",
            "To make the code shorter",
            "Testing is only needed for large programs"
        ],
        "answer": 1,
        "explanation": "Testing finds bugs before deployment. Errors in live software can cause data loss, security breaches, or financial loss."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "What does a BREAKPOINT do in an IDE?",
        "options": [
            "Permanently stops the program",
            "Pauses execution at a specific line so the developer can inspect variable values",
            "Deletes the line of code",
            "Highlights syntax errors in red"
        ],
        "answer": 1,
        "explanation": "A breakpoint pauses execution at that line. The developer can then inspect variable values and step through code one line at a time."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "What is ITERATIVE testing?",
        "options": [
            "Testing the whole program only at the end of development",
            "Testing individual modules during development as each is completed",
            "Testing with boundary values only",
            "Having end-users test the program"
        ],
        "answer": 1,
        "explanation": "Iterative (incremental) testing happens during development — each module or component is tested as it's built."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "What is FINAL (terminal) testing?",
        "options": [
            "Testing each module as it is written",
            "Testing the complete program at the end of development before release",
            "Testing using boundary values",
            "Automatically generated tests"
        ],
        "answer": 1,
        "explanation": "Final/terminal testing tests the whole finished program at the end of development to verify it meets all requirements before release."
    },
    {
        "topic": "Testing",
        "tier": 1,
        "type": "mc",
        "q": "What is a VARIABLE WATCH feature in an IDE?",
        "options": [
            "A timer tracking how long variables exist",
            "A panel displaying current values of selected variables during execution",
            "A warning when a variable is declared but unused",
            "An automatic type-checker"
        ],
        "answer": 1,
        "explanation": "Variable watch monitors specific variables in real-time as the program runs, helping spot where incorrect values arise."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 1 — FUNCTIONS & PROCEDURES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Functions & Procedures",
        "tier": 1,
        "type": "mc",
        "q": "What is the key difference between a FUNCTION and a PROCEDURE?",
        "options": [
            "Functions use loops, procedures don't",
            "A function returns a value; a procedure does not",
            "Procedures can have parameters, functions cannot",
            "Functions are Python-only"
        ],
        "answer": 1,
        "explanation": "A function returns a value with `return`. A procedure performs actions but does not return a value."
    },
    {
        "topic": "Functions & Procedures",
        "tier": 1,
        "type": "mc",
        "q": "What is a PARAMETER in a subroutine?",
        "options": [
            "The name of the subroutine",
            "A value passed into the subroutine when it is called",
            "A variable declared inside the subroutine",
            "The value returned by the function"
        ],
        "answer": 1,
        "explanation": "A parameter is a variable that receives a value (argument) passed in when the subroutine is called."
    },
    {
        "topic": "Functions & Procedures",
        "tier": 1,
        "type": "mc",
        "q": "In OCR pseudocode, which keyword closes a function definition?",
        "options": ["endif", "return", "endfunction", "next"],
        "answer": 2,
        "explanation": "Functions in OCR ERL use: `function name(params) ... return value ... endfunction`."
    },
    {
        "topic": "Functions & Procedures",
        "tier": 1,
        "type": "self_mark",
        "q": "Write a function in OCR pseudocode called `calcArea` that takes parameters `width` and `height` and returns their product. [3 marks]",
        "answer": "function calcArea(width, height)\n    area = width * height\n    return area\nendfunction",
        "explanation": "1 mark: function keyword with correct name and parameters\n1 mark: correct calculation\n1 mark: return statement and endfunction"
    },
    {
        "topic": "Functions & Procedures",
        "tier": 1,
        "type": "self_mark",
        "q": "A function `newPrice(nights, room)` exists. Write the OCR pseudocode to call it for a Premium room for 5 nights, and output the result. [2 marks]",
        "answer": "price = newPrice(5, \"Premium\")\nprint(price)",
        "explanation": "1 mark: calling newPrice with correct arguments (5 and \"Premium\")\n1 mark: storing the result and printing it"
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — SORTING ALGORITHMS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "In a BUBBLE SORT, what happens in each pass?",
        "options": [
            "The smallest element is moved to the front",
            "Adjacent elements are compared and swapped if in the wrong order",
            "The list is split in half and merged",
            "Elements are inserted into the correct position one at a time"
        ],
        "answer": 1,
        "explanation": "Bubble sort compares adjacent pairs and swaps if out of order. Each pass 'bubbles' the largest unsorted element to the end."
    },
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What is the purpose of the `temp` variable in a swap operation during sorting?",
        "options": [
            "To store the array length",
            "To track the loop counter",
            "To temporarily hold a value so it isn't overwritten during the swap",
            "To store the sorted portion"
        ],
        "answer": 2,
        "explanation": "Without temp, one value would be lost. e.g. temp=a, a=b, b=temp. This swaps a and b safely."
    },
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "Which algorithm builds a sorted section by taking one element at a time and placing it correctly within the sorted part?",
        "options": ["Bubble sort", "Merge sort", "Insertion sort", "Linear sort"],
        "answer": 2,
        "explanation": "Insertion sort takes each element and inserts it into its correct position in the already-sorted left portion."
    },
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What does MERGE SORT do as its first step?",
        "options": [
            "Compares adjacent elements",
            "Repeatedly splits the list until each sub-list has one element",
            "Finds the middle element and pivots",
            "Inserts elements one at a time"
        ],
        "answer": 1,
        "explanation": "Merge sort divides the list in half repeatedly until each piece has one element (trivially sorted), then merges them back in order."
    },
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "Why does the inner loop of insertion sort need to be CONDITION-CONTROLLED (while) rather than count-controlled (for)?",
        "options": [
            "Because the list length is unknown",
            "Because the number of shifts varies — it stops when the element reaches its correct position",
            "Because insertion sort can only use while loops",
            "Because for loops would sort in the wrong direction"
        ],
        "answer": 1,
        "explanation": "The element may need 0, 1, or many shifts to reach its correct position — we don't know in advance, so a condition-controlled loop is needed."
    },
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "self_mark",
        "q": "Give ONE similarity and ONE difference between bubble sort and insertion sort. [4 marks]",
        "answer": "Similarity: Both compare elements and perform swaps/shifts; both sort in-place without extra storage; both use nested loops.\nDifference: Bubble sort compares adjacent pairs across the whole unsorted portion each pass. Insertion sort takes one element and finds its correct position in the already-sorted portion.",
        "explanation": "1 mark per similarity point + expansion. 1 mark per difference point + expansion."
    },
    {
        "topic": "Sorting Algorithms",
        "tier": 2,
        "type": "self_mark",
        "q": "Show all steps of a MERGE SORT on the list: [45, 12, -99, 100, -13]",
        "answer": "Split: [45, 12] [-99, 100, -13]\nSplit: [45] [12] | [-99] [100, -13]\nSplit: [45] [12] | [-99] [100] [-13]\nMerge: [12, 45] | [-99] [-13, 100]\nMerge: [12, 45] | [-99, -13, 100]  ← actually: [-99, -13, 100]\nFinal merge: [-99, -13, 12, 45, 100]",
        "explanation": "Show each split step and each merge step. Marks awarded for showing the process clearly even if minor errors."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — SEARCHING ALGORITHMS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Searching Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What is required before a BINARY SEARCH can be used?",
        "options": ["An even number of elements", "The list must be SORTED", "No duplicate values", "The list must be in an array"],
        "answer": 1,
        "explanation": "Binary search requires a sorted list. It works by halving the search space each time."
    },
    {
        "topic": "Searching Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What does binary search do when the middle element is GREATER than the target?",
        "options": [
            "Stop — target not found",
            "Search the right half",
            "Search the left half",
            "Start over from the beginning"
        ],
        "answer": 2,
        "explanation": "If middle > target, the target must be in the left half (smaller values). Discard the right half and repeat."
    },
    {
        "topic": "Searching Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What is the maximum number of comparisons for a binary search on 16 items?",
        "options": ["4", "8", "16", "5"],
        "answer": 0,
        "explanation": "Binary search is O(log₂n). log₂(16) = 4. At most 4 comparisons are needed."
    },
    {
        "topic": "Searching Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What does a LINEAR SEARCH do when the target is NOT in the list?",
        "options": [
            "Returns the middle element",
            "Checks every element from first to last and reports not found",
            "Crashes",
            "Restarts from the beginning"
        ],
        "answer": 1,
        "explanation": "Linear search checks each element one by one. If it reaches the end without a match, it reports not found."
    },
    {
        "topic": "Searching Algorithms",
        "tier": 2,
        "type": "mc",
        "q": "What is a benefit of BINARY SEARCH over LINEAR SEARCH?",
        "options": [
            "Binary search works on unsorted lists",
            "Binary search is much faster on large sorted lists",
            "Binary search uses less memory",
            "Binary search is simpler to code"
        ],
        "answer": 1,
        "explanation": "Binary search is O(log n) vs linear's O(n). On 1000 items: binary needs ~10 checks, linear needs up to 1000."
    },
    {
        "topic": "Searching Algorithms",
        "tier": 2,
        "type": "self_mark",
        "q": "Describe the steps a binary search follows to find 42 in the sorted list: [5, 12, 23, 42, 67, 81, 95]. [4 marks]",
        "answer": "1. Find middle element: index 3, value 42.\n2. Compare 42 to target (42) — they are equal.\n3. Target found at index 3.",
        "explanation": "Full mark scheme: 1) Find middle. 2) Compare to target. 3) If equal → found. If target smaller → discard right half. If target larger → discard left half. 4) Repeat on remaining half. 4) If list empty → not found."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — VALIDATION & AUTHENTICATION
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Validation",
        "tier": 2,
        "type": "mc",
        "q": "What is the purpose of INPUT VALIDATION?",
        "options": [
            "To make the program run faster",
            "To check data is reasonable and within expected range before processing",
            "To encrypt user input",
            "To format output data neatly"
        ],
        "answer": 1,
        "explanation": "Validation checks that input is sensible, complete, and within acceptable limits. Prevents garbage-in, garbage-out."
    },
    {
        "topic": "Validation",
        "tier": 2,
        "type": "mc",
        "q": "A password must be at least 8 characters. Which loop is most appropriate for validation?",
        "options": [
            "for loop — count-controlled",
            "while loop — keep asking until password is long enough",
            "if statement — check once only",
            "do-until — always ask twice"
        ],
        "answer": 1,
        "explanation": "while is ideal: keep asking until the condition is met. A for loop has a fixed count — not appropriate for validation."
    },
    {
        "topic": "Validation",
        "tier": 2,
        "type": "mc",
        "q": "Which of the following is a RANGE CHECK?",
        "options": [
            "Checking a name contains only letters",
            "Checking an age is between 0 and 120",
            "Checking a field is not empty",
            "Checking an email contains @"
        ],
        "answer": 1,
        "explanation": "A range check verifies a numeric value falls within an acceptable min–max range."
    },
    {
        "topic": "Validation",
        "tier": 2,
        "type": "mc",
        "q": "Which of the following is a PRESENCE CHECK?",
        "options": [
            "Checking a number is between 1 and 10",
            "Checking a field is not left empty",
            "Checking a string contains only digits",
            "Checking input matches one of a list of allowed values"
        ],
        "answer": 1,
        "explanation": "A presence check ensures a required field is not left blank/empty."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — ARRAYS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Arrays",
        "tier": 2,
        "type": "mc",
        "q": "In OCR pseudocode, what index does the FIRST element of an array have?",
        "options": ["1", "0", "-1", "Depends on declaration"],
        "answer": 1,
        "explanation": "Arrays in OCR pseudocode are 0-indexed. First element = index 0."
    },
    {
        "topic": "Arrays",
        "tier": 2,
        "type": "mc",
        "q": "An array `scores` has 5 elements. What is the index of the LAST element?",
        "options": ["5", "4", "6", "scores.length"],
        "answer": 1,
        "explanation": "With 5 elements (0-indexed): last index = 5-1 = 4. Always: last index = length - 1."
    },
    {
        "topic": "Arrays",
        "tier": 2,
        "type": "mc",
        "q": "How do you access the THIRD element of an array called `names` in OCR pseudocode?",
        "options": ["names[3]", "names[2]", "names(3)", "names.get(2)"],
        "answer": 1,
        "explanation": "Third element = index 2 (0-indexed). Access with square brackets: names[2]."
    },
    {
        "topic": "Arrays",
        "tier": 2,
        "type": "mc",
        "q": "What does `array.length` return?",
        "options": ["The index of the last element", "The total number of elements in the array", "The first element", "The data type of elements"],
        "answer": 1,
        "explanation": "`.length` returns the total number of elements. Last index = array.length - 1."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — FILE HANDLING
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "File Handling",
        "tier": 2,
        "type": "mc",
        "q": 'In OCR pseudocode, how do you open a file called "data.txt" for reading?',
        "options": [
            'open "data.txt" for write',
            'myFile = open("data.txt")',
            'load "data.txt"',
            'read "data.txt"'
        ],
        "answer": 1,
        "explanation": 'OCR ERL: myFile = open("data.txt") — this opens the file. Then use myFile.readLine() to read.'
    },
    {
        "topic": "File Handling",
        "tier": 2,
        "type": "mc",
        "q": "In OCR pseudocode, how do you check if you have reached the end of a file?",
        "options": ["file.eof()", "file.endOfFile()", "file.finished()", "file.end()"],
        "answer": 1,
        "explanation": "myFile.endOfFile() returns True when there are no more lines. Used as: while NOT myFile.endOfFile()"
    },
    {
        "topic": "File Handling",
        "tier": 2,
        "type": "mc",
        "q": "In OCR pseudocode, which command writes a line to an open file?",
        "options": ["save(myFile, data)", "myFile.writeLine(data)", "print(myFile, data)", "write myFile data"],
        "answer": 1,
        "explanation": "OCR ERL: myFile.writeLine(data) writes a line to an open file."
    },
    {
        "topic": "File Handling",
        "tier": 2,
        "type": "self_mark",
        "q": "Write OCR pseudocode to open a file called \"scores.txt\", read and print every line until the end, then close it. [4 marks]",
        "answer": 'myFile = open("scores.txt")\nwhile NOT myFile.endOfFile()\n    line = myFile.readLine()\n    print(line)\nendwhile\nmyFile.close()',
        "explanation": "1 mark: open file\n1 mark: while NOT endOfFile() loop\n1 mark: readLine() inside loop\n1 mark: close() after loop"
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — COMPILER VS INTERPRETER
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Compiler vs Interpreter",
        "tier": 2,
        "type": "mc",
        "q": "What does a COMPILER do?",
        "options": [
            "Translates source code one line at a time and executes immediately",
            "Translates the entire program into machine code before execution, creating an executable",
            "Translates between two high-level languages",
            "Only checks for syntax errors"
        ],
        "answer": 1,
        "explanation": "A compiler translates the whole source code to machine code in one go, creating a standalone executable."
    },
    {
        "topic": "Compiler vs Interpreter",
        "tier": 2,
        "type": "mc",
        "q": "What does an INTERPRETER do differently from a compiler?",
        "options": [
            "It creates an executable file",
            "It translates and executes the program one line at a time",
            "It is faster at running the final program",
            "It cannot detect errors"
        ],
        "answer": 1,
        "explanation": "An interpreter translates and executes one statement at a time. No executable is created. Slower to run but easier to debug."
    },
    {
        "topic": "Compiler vs Interpreter",
        "tier": 2,
        "type": "mc",
        "q": "Which is an ADVANTAGE of a compiler over an interpreter?",
        "options": [
            "Easier to debug — stops at first error",
            "The compiled executable runs faster",
            "Source code stays readable by anyone",
            "No translation step is needed"
        ],
        "answer": 1,
        "explanation": "Compiled programs run faster — translation is done once up front. The executable runs directly without re-translating."
    },
    {
        "topic": "Compiler vs Interpreter",
        "tier": 2,
        "type": "mc",
        "q": "Which is an ADVANTAGE of an interpreter over a compiler?",
        "options": [
            "Produces a faster executable",
            "Source code is protected",
            "Easier to test and debug — errors reported line by line during development",
            "Only needs to translate once"
        ],
        "answer": 2,
        "explanation": "Interpreters are useful during development — they stop at the first error and report its location immediately."
    },
    {
        "topic": "Compiler vs Interpreter",
        "tier": 2,
        "type": "mc",
        "q": "A compiled program stops translating and reports all errors. An interpreter stops at...",
        "options": [
            "The end of the program",
            "The first error it encounters",
            "Every 10th line",
            "Syntax errors only"
        ],
        "answer": 1,
        "explanation": "An interpreter stops at the FIRST error it hits. A compiler translates the whole program and then reports all errors it found."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — HIGH-LEVEL VS LOW-LEVEL LANGUAGES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "High vs Low Level Languages",
        "tier": 2,
        "type": "mc",
        "q": "Which is a characteristic of a HIGH-LEVEL programming language?",
        "options": [
            "Written in binary (0s and 1s)",
            "Uses mnemonics like LDA and STA",
            "Closer to human language, easier to read and write",
            "Runs directly on the CPU without translation"
        ],
        "answer": 2,
        "explanation": "High-level languages (Python, Java) use English-like syntax. They need a compiler or interpreter to translate to machine code."
    },
    {
        "topic": "High vs Low Level Languages",
        "tier": 2,
        "type": "mc",
        "q": "Which is a LOW-LEVEL language?",
        "options": ["Python", "Java", "Assembly language", "JavaScript"],
        "answer": 2,
        "explanation": "Assembly language uses mnemonics (LDA, ADD, STA) and is specific to a processor. It is translated by an assembler."
    },
    {
        "topic": "High vs Low Level Languages",
        "tier": 2,
        "type": "mc",
        "q": "What translates ASSEMBLY LANGUAGE into machine code?",
        "options": ["Compiler", "Interpreter", "Assembler", "Linker"],
        "answer": 2,
        "explanation": "An assembler converts assembly mnemonics into machine code (binary). Compilers handle high-level languages."
    },
    {
        "topic": "High vs Low Level Languages",
        "tier": 2,
        "type": "mc",
        "q": "What is an advantage of a HIGH-LEVEL language over a low-level language?",
        "options": [
            "Runs directly on hardware without translation",
            "Easier to write, read, and maintain — portable across different hardware",
            "Gives direct control over CPU registers and memory",
            "Requires no compiler or interpreter"
        ],
        "answer": 1,
        "explanation": "High-level languages are readable, portable, and require less code. Disadvantage: less hardware control and needs translation."
    },
    {
        "topic": "High vs Low Level Languages",
        "tier": 2,
        "type": "mc",
        "q": "What is an advantage of a LOW-LEVEL language over a high-level language?",
        "options": [
            "Easier to read and maintain",
            "Portable across different hardware",
            "Gives direct control over hardware — very efficient and fast",
            "Needs no translation to run"
        ],
        "answer": 2,
        "explanation": "Low-level code runs very efficiently and gives precise hardware control. Disadvantage: harder to read, write, and maintain."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — COMPUTATIONAL THINKING
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Computational Thinking",
        "tier": 2,
        "type": "mc",
        "q": "What is DECOMPOSITION in computational thinking?",
        "options": [
            "Removing unnecessary detail from a problem",
            "Breaking a complex problem into smaller, more manageable sub-problems",
            "Representing a solution as a flowchart",
            "Finding patterns that repeat across different problems"
        ],
        "answer": 1,
        "explanation": "Decomposition breaks a large problem into smaller parts, each solvable separately. e.g. a game: input, scoring, graphics, sound."
    },
    {
        "topic": "Computational Thinking",
        "tier": 2,
        "type": "mc",
        "q": "What is ABSTRACTION in computational thinking?",
        "options": [
            "Breaking a problem into sub-problems",
            "Finding patterns across problems",
            "Removing unnecessary detail and focusing only on what is relevant to the solution",
            "Writing the algorithm as pseudocode"
        ],
        "answer": 2,
        "explanation": "Abstraction ignores irrelevant detail. e.g. a map abstracts a city — it shows roads but not every tree or building."
    },
    {
        "topic": "Computational Thinking",
        "tier": 2,
        "type": "mc",
        "q": "What is PATTERN RECOGNITION in computational thinking?",
        "options": [
            "Breaking a problem into sub-problems",
            "Writing a step-by-step solution",
            "Identifying similarities or repeating features across problems to reuse solutions",
            "Removing unnecessary detail from a problem"
        ],
        "answer": 2,
        "explanation": "Pattern recognition identifies similarities across problems. e.g. sorting is needed in many programs — a sorting solution can be reused."
    },
    {
        "topic": "Computational Thinking",
        "tier": 2,
        "type": "mc",
        "q": "What is ALGORITHMIC THINKING?",
        "options": [
            "Using an existing algorithm from a library",
            "Designing a step-by-step set of instructions to solve a problem",
            "Removing unnecessary detail",
            "Breaking a problem into sub-problems"
        ],
        "answer": 1,
        "explanation": "Algorithmic thinking is the process of designing a clear, step-by-step logical sequence of instructions to solve a problem."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — MAINTAINABILITY
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Maintainability",
        "tier": 2,
        "type": "mc",
        "q": "Which of these improves code MAINTAINABILITY?",
        "options": [
            "Using single-letter variable names",
            "Writing all code in one long block with no subroutines",
            "Adding comments and using meaningful variable names",
            "Removing all blank lines and whitespace"
        ],
        "answer": 2,
        "explanation": "Meaningful names (studentScore not x) and comments make code easier to understand and modify later."
    },
    {
        "topic": "Maintainability",
        "tier": 2,
        "type": "mc",
        "q": "How do SUBROUTINES improve maintainability?",
        "options": [
            "They make the program use less memory",
            "Repeated code is written once and called multiple times — only one place to update if logic changes",
            "They make the program run faster",
            "They prevent logic errors automatically"
        ],
        "answer": 1,
        "explanation": "Subroutines reduce duplication. If logic needs changing, you update one subroutine rather than every place the code appears."
    },
    {
        "topic": "Maintainability",
        "tier": 2,
        "type": "self_mark",
        "q": "Give TWO ways to improve the maintainability of a program. [2 marks]",
        "answer": "1. Use meaningful/descriptive variable and subroutine names so the code is self-documenting.\n2. Add comments explaining what sections of code do.\n3. Use subroutines to avoid repeating code — easier to update in one place.\n4. Use indentation consistently to show the structure of the code.",
        "explanation": "Any 2 valid points. 1 mark each. This comes up as a 2-mark question — give 2 distinct methods."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — STRING MANIPULATION
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "String Manipulation",
        "tier": 2,
        "type": "mc",
        "q": 'What does "Hello".length return in OCR pseudocode?',
        "options": ["4", "5", "6", '"Hello"'],
        "answer": 1,
        "explanation": '"Hello" has 5 characters (H, e, l, l, o). .length returns 5.'
    },
    {
        "topic": "String Manipulation",
        "tier": 2,
        "type": "mc",
        "q": 'What does "Hello".upper return in OCR pseudocode?',
        "options": ['"hello"', '"HELLO"', '"Hello"', '"HeLLo"'],
        "answer": 1,
        "explanation": '.upper converts all characters to uppercase. "Hello".upper → "HELLO".'
    },
    {
        "topic": "String Manipulation",
        "tier": 2,
        "type": "mc",
        "q": 'What does "Computer"[0] return in OCR pseudocode?',
        "options": ['"Computer"', '"C"', '"o"', '"r"'],
        "answer": 1,
        "explanation": "Strings are 0-indexed. Index 0 is the first character: 'C'."
    },
    {
        "topic": "String Manipulation",
        "tier": 2,
        "type": "mc",
        "q": "What is string CONCATENATION?",
        "options": [
            "Converting a string to uppercase",
            "Finding the length of a string",
            "Joining two or more strings together",
            "Splitting a string into individual characters"
        ],
        "answer": 2,
        "explanation": 'Concatenation joins strings. e.g. "Hello" + " " + "World" = "Hello World".'
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — IDE FEATURES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "IDE Features",
        "tier": 2,
        "type": "mc",
        "q": "What does SYNTAX HIGHLIGHTING in an IDE do?",
        "options": [
            "Highlights logic errors in red",
            "Colours different code elements (keywords, strings, comments) to improve readability",
            "Underlines all variable names",
            "Runs the code line by line"
        ],
        "answer": 1,
        "explanation": "Syntax highlighting colours code elements to make them easier to read and spot errors (keywords blue, strings green, etc.)."
    },
    {
        "topic": "IDE Features",
        "tier": 2,
        "type": "mc",
        "q": "What does 'STEPPING THROUGH CODE' in an IDE mean?",
        "options": [
            "Running the full program at high speed",
            "Executing the program one line at a time to track variable changes",
            "Automatically fixing errors",
            "Indenting all code automatically"
        ],
        "answer": 1,
        "explanation": "Stepping through executes code one line at a time, letting the developer observe exactly what each line does."
    },
    {
        "topic": "IDE Features",
        "tier": 2,
        "type": "self_mark",
        "q": "Name and describe TWO features of an IDE that can be used when testing a program. [4 marks]",
        "answer": "1. Breakpoints — pause program execution at a specific line so the developer can inspect variable values at that point.\n2. Variable watch — displays the current values of selected variables in real-time during execution.\n3. Stepping through code — execute one line at a time to trace the exact flow and spot errors.\n4. Error highlighting / error reporting — highlights syntax errors and shows their location.",
        "explanation": "1 mark per feature name, 1 mark per description = 4 marks total. This comes up every year."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 2 — CASTING
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Casting",
        "tier": 2,
        "type": "mc",
        "q": "What is CASTING in programming?",
        "options": [
            "Sending data to an output device",
            "Converting a value from one data type to another",
            "Declaring a variable",
            "Calling a function multiple times"
        ],
        "answer": 1,
        "explanation": "Casting converts between types. e.g. int('5') → integer 5. str(42) → string '42'."
    },
    {
        "topic": "Casting",
        "tier": 2,
        "type": "mc",
        "q": "Why must you cast the result of input() in Python before doing arithmetic?",
        "options": [
            "Because input() returns a Boolean",
            "Because input() always returns a String, even if the user types a number",
            "Because input() returns a Real",
            "To make the program faster"
        ],
        "answer": 1,
        "explanation": "input() always returns a String. '5' + 3 causes a TypeError. Use int(input(...)) to cast to Integer first."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 3 — FLOWCHARTS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Flowcharts",
        "tier": 3,
        "type": "mc",
        "q": "Which flowchart symbol represents a DECISION?",
        "options": ["Rectangle", "Oval/rounded rectangle", "Diamond", "Parallelogram"],
        "answer": 2,
        "explanation": "Diamond = decision (Yes/No). Rectangle = process. Oval = start/end (terminator). Parallelogram = input/output."
    },
    {
        "topic": "Flowcharts",
        "tier": 3,
        "type": "mc",
        "q": "Which flowchart symbol represents INPUT or OUTPUT?",
        "options": ["Rectangle", "Diamond", "Oval", "Parallelogram"],
        "answer": 3,
        "explanation": "Parallelogram = input/output. Rectangle = process. Diamond = decision. Oval = start/end."
    },
    {
        "topic": "Flowcharts",
        "tier": 3,
        "type": "mc",
        "q": "Which flowchart symbol represents the START or END of a program?",
        "options": ["Rectangle", "Diamond", "Oval/rounded rectangle", "Parallelogram"],
        "answer": 2,
        "explanation": "Oval (terminator) = start or end. Rectangle = process. Diamond = decision. Parallelogram = I/O."
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIER 3 — GLOBAL VS LOCAL VARIABLES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "topic": "Variables",
        "tier": 3,
        "type": "mc",
        "q": "What is a LOCAL variable?",
        "options": [
            "Accessible from anywhere in the program",
            "Declared inside a subroutine and only accessible within it",
            "A variable that stores a constant value",
            "Shared between all subroutines automatically"
        ],
        "answer": 1,
        "explanation": "A local variable exists only within the subroutine it's declared in. Created when subroutine is called, destroyed when it ends."
    },
    {
        "topic": "Variables",
        "tier": 3,
        "type": "mc",
        "q": "What is a GLOBAL variable?",
        "options": [
            "Only accessible inside one function",
            "A constant that cannot be changed",
            "Accessible from any part of the program",
            "Always an integer type"
        ],
        "answer": 2,
        "explanation": "A global variable is declared outside any subroutine and can be read/written from anywhere in the program."
    },

]

# ── Weighting ─────────────────────────────────────────────────────────────────
def get_weights(qs):
    return [3 if q["tier"] == 1 else 2 if q["tier"] == 2 else 1 for q in qs]

# ── Display ───────────────────────────────────────────────────────────────────
def header(score, total, streak):
    pct = f"{round(score/total*100)}%" if total > 0 else "—"
    streak_display = f"🔥{streak}" if streak >= 3 else str(streak)
    print(f"{BOLD}{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BOLD}  OCR J277/02 — Infinite Theory Question Bank{RESET}  {DIM}(Q to quit){RESET}")
    print(f"  Score: {GREEN}{BOLD}{score}/{total} ({pct}){RESET}  |  Streak: {YELLOW}{BOLD}{streak_display}{RESET}")
    print(f"{BOLD}{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}\n")

def ask_mc(q_data):
    tier_colour = RED if q_data["tier"]==1 else YELLOW if q_data["tier"]==2 else DIM
    print(f"  {tier_colour}{BOLD}[{q_data['topic']} — Tier {q_data['tier']}]{RESET}\n")
    print(f"  {BOLD}{q_data['q']}{RESET}\n")
    for i, opt in enumerate(q_data["options"]):
        print(f"    {BOLD}{chr(65+i)}{RESET}.  {opt}")
    print()
    while True:
        ans = input("  Answer (A/B/C/D) or S to skip, Q to quit: ").strip().upper()
        if ans in ['A','B','C','D','S','Q']:
            break
        print("  Enter A, B, C, D, S, or Q.")
    if ans == 'Q':
        return 'quit'
    if ans == 'S':
        print(f"\n  {DIM}Skipped. Answer was {BOLD}{chr(65+q_data['answer'])}: {q_data['options'][q_data['answer']]}{RESET}")
        print(f"  {YELLOW}{q_data['explanation']}{RESET}")
        return None
    user_idx = ord(ans) - 65
    correct = user_idx == q_data["answer"]
    if correct:
        print(f"\n  {GREEN}{BOLD}✓  Correct!{RESET}")
    else:
        correct_letter = chr(65 + q_data["answer"])
        print(f"\n  {RED}{BOLD}✗  Incorrect.{RESET}  The answer was {BOLD}{correct_letter}: {q_data['options'][q_data['answer']]}{RESET}")
    print(f"  {YELLOW}→  {q_data['explanation']}{RESET}")
    return correct

def ask_self_mark(q_data):
    tier_colour = RED if q_data["tier"]==1 else YELLOW if q_data["tier"]==2 else DIM
    print(f"  {tier_colour}{BOLD}[{q_data['topic']} — Tier {q_data['tier']}  |  Open-ended]{RESET}\n")
    print(f"  {BOLD}{q_data['q']}{RESET}\n")
    print(f"  {DIM}Write your answer, then press Enter to reveal the model answer.{RESET}")
    response = input("  Your answer (or Q to quit): ").strip().upper()
    if response == 'Q':
        return 'quit'
    print(f"\n  {CYAN}{BOLD}Model Answer:{RESET}")
    for line in q_data["answer"].split("\n"):
        print(f"    {line}")
    print(f"\n  {YELLOW}→  Mark scheme: {q_data['explanation']}{RESET}\n")
    while True:
        mark = input("  Did you get it right? (Y/N): ").strip().upper()
        if mark in ['Y','N']:
            break
    return mark == 'Y'

# ── Topic menu ────────────────────────────────────────────────────────────────
def topic_menu(all_qs):
    topics = sorted(set(q["topic"] for q in all_qs))
    print(f"\n  {BOLD}Select a topic to focus on, or 0 for all topics:{RESET}\n")
    for i, t in enumerate(topics):
        min_tier = min(q["tier"] for q in all_qs if q["topic"] == t)
        count = sum(1 for q in all_qs if q["topic"] == t)
        t_col = RED if min_tier==1 else YELLOW if min_tier==2 else DIM
        print(f"  {i+1:3}.  {t_col}[T{min_tier}]{RESET}  {t}  {DIM}({count} questions){RESET}")
    print(f"\n  {BOLD}  0.  All topics{RESET}\n")
    while True:
        choice = input("  Enter number: ").strip()
        if choice == "0" or choice == "":
            return all_qs
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(topics):
                filtered = [q for q in all_qs if q["topic"] == topics[idx]]
                print(f"\n  {GREEN}Focusing on: {topics[idx]}{RESET}")
                return filtered
        except ValueError:
            pass
        print("  Invalid — try again.")

# ── End stats ─────────────────────────────────────────────────────────────────
def show_stats(score, total, topic_stats):
    clear()
    print(f"\n{BOLD}{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BOLD}  SESSION COMPLETE — OCR J277/02{RESET}")
    print(f"{BOLD}{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}\n")
    if total == 0:
        print("  No questions attempted.\n")
        return
    pct = round(score / total * 100)
    col = GREEN if pct >= 70 else YELLOW if pct >= 50 else RED
    print(f"  Final: {col}{BOLD}{score}/{total}  ({pct}%){RESET}\n")
    print(f"  {BOLD}Performance by topic:{RESET}\n")
    for topic, (correct, attempted) in sorted(topic_stats.items(), key=lambda x: x[1][0]/x[1][1] if x[1][1]>0 else 0):
        if attempted == 0:
            continue
        t_pct = round(correct / attempted * 100)
        bar = "█" * (t_pct // 10) + "░" * (10 - t_pct // 10)
        col = GREEN if t_pct >= 70 else YELLOW if t_pct >= 50 else RED
        print(f"  {topic:<32}  {col}{bar}  {t_pct:3}%{RESET}  {DIM}({correct}/{attempted}){RESET}")
    print()
    if pct < 50:
        print(f"  {RED}Focus on the topics in red — those are your weak spots.{RESET}")
    elif pct < 70:
        print(f"  {YELLOW}Good effort — push to 70%+ on each topic.{RESET}")
    else:
        print(f"  {GREEN}Strong session! Keep up the regular practice.{RESET}")
    print()

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    clear()
    print(f"\n{BOLD}{CYAN}")
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║      OCR J277/02 — Infinite Theory Question Bank        ║")
    print("  ║      Built from 2022–2025 past paper analysis           ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    print(f"  {DIM}Tier 1 = guaranteed every year  |  Tier 2 = very likely  |  Tier 3 = rotates{RESET}")
    print(f"  {DIM}Commands: S = skip  |  T = change topic  |  Q = quit & see stats{RESET}\n")

    active = topic_menu(QUESTIONS)
    score = total = streak = 0
    topic_stats = {}

    while True:
        clear()
        header(score, total, streak)

        weights = get_weights(active)
        q = random.choices(active, weights=weights, k=1)[0]

        if q["type"] == "mc":
            result = ask_mc(q)
        else:
            result = ask_self_mark(q)

        if result == 'quit':
            break

        t = q["topic"]
        if t not in topic_stats:
            topic_stats[t] = [0, 0]

        if result is None:
            streak = 0
        elif result:
            score += 1
            total += 1
            streak += 1
            topic_stats[t][0] += 1
            topic_stats[t][1] += 1
        else:
            total += 1
            streak = 0
            topic_stats[t][1] += 1

        print()
        cmd = input("  Enter = next question  |  T = change topic  |  Q = quit: ").strip().upper()
        if cmd == 'Q':
            break
        if cmd == 'T':
            clear()
            active = topic_menu(QUESTIONS)

    show_stats(score, total, topic_stats)

if __name__ == "__main__":
    main()
