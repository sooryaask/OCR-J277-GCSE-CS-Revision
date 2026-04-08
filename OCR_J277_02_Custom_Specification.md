# OCR J277/02 Computational Thinking, Algorithms and Programming — Custom Priority Specification
## Based on ALL questions from June 2022, June 2023, June 2024, May 2025

> **The 80:20 Verdict: CONFIRMED.**
> Analysis across 4 exam years shows that approximately 8–9 topic areas account for
> **55–65 marks out of 80 every single year**. The remaining content rotates unpredictably.
> Focus revision energy on Tier 1 and Tier 2 below.

---

## TIER 1 — Guaranteed Every Year (4/4 years)
*These topics have appeared in every paper without exception. Learn these to near-perfection.*

---

### 1. Programming Constructs — Selection vs Iteration
**Marks: 3–4 every year | Always appears as first or early question in Section A**

**What gets tested (every year):**
- Given a code snippet (for loop, while loop, if/else, switch/case, do-until), tick whether it is Selection or Iteration
- Write pseudocode to perform a basic operation (increment a variable, add two numbers, find difference, modulus)
- Identify arithmetic operators for specific purposes (MOD for remainder, ^ or ** for power, - for subtraction)

**Exact question wording patterns:**
- "Tick (✓) one box in each row to identify whether the OCR Reference Language code given is an example of **selection** or **iteration**" [4 marks]
- "Tick (✓) one box in each row to identify the programming construct where each **keyword** is used" [3 marks]
- "Write pseudocode to [increment/add/store] the value..." [1 mark]

**Key facts to know:**
- **Selection:** `if/then/else/endif`, `switch/case/endswitch`
- **Iteration:** `for/next`, `while/endwhile`, `do/until`
- Incrementing: `score = score + 1` (also: `score += 1`, `score++`)
- MOD = modulus (remainder after division). Used to check odd/even: `num MOD 2 == 0` → even
- Power: `^` or `**` in OCR pseudocode
- Assignment: `=` (not `==` — that is comparison)

---

### 2. Logic Gates and Boolean Logic
**Marks: 5–7 every year | Always a dedicated multi-part question**

**What gets tested (every year):**
- Draw a logic diagram/circuit from a Boolean expression (e.g. P = (A OR B) AND NOT C)
- Identify logic gates from truth tables
- Complete a truth table for a given Boolean expression
- State how many rows a truth table needs (2^n for n inputs)
- Describe the purpose of a truth table
- Draw a logic circuit for expressions combining AND, OR, NOT

**Exact question wording patterns (rotate):**
- "Complete the following logic diagram for P = [expression] by drawing one logic gate in each box" [3 marks]
- "Draw a logic diagram for the [system]" [3 marks]
- "Complete the truth table for P = [expression]" [4 marks]
- "Draw a logic circuit for P = [expression]" [3 marks]
- "Identify the logic gates for truth table 1 and truth table 2" [2 marks]
- "Describe the purpose of a truth table" [2 marks]
- "State how many rows would be required in a truth table for [expression]" [1 mark]

**Key facts to know:**

| Gate | Symbol/Shape | Rule |
|------|-------------|------|
| AND | D-shape (flat left) | Output 1 only if BOTH inputs are 1 |
| OR | Curved shape | Output 1 if AT LEAST ONE input is 1 |
| NOT | Triangle with circle | Flips the input (0→1, 1→0) |
| NAND | AND with circle | Opposite of AND |
| NOR | OR with circle | Opposite of OR |
| XOR | OR with extra curve | Output 1 if inputs are DIFFERENT |

- NOT gate MUST have the circle at its output — examiners deduct marks if missing
- AND/OR gates must NOT have a circle
- Truth table rows = 2^(number of inputs): 2 inputs → 4 rows, 3 inputs → 8 rows
- Boolean expressions: AND = multiplication (.); OR = addition (+); NOT = bar or ¬

**Common expressions on past papers:**
- `P = (A OR B) AND NOT C` — 2022
- `Q = A AND NOT B AND C` — 2023
- `P = (A AND B) OR C` — 2024
- `P = NOT A AND (B OR C)` — 2024

---

### 3. Trace Tables
**Marks: 3–4 every year | Almost always in Section A and Section B**

**What gets tested (every year):**
- Complete a trace table for a given algorithm (tracking variables and output across line numbers)
- Variables typically include: loop counter, condition variable, score/total, output messages

**Exact question wording patterns:**
- "Complete the following trace table for the given algorithm when [inputs] are entered." [3–4 marks]
- "Complete the trace table for the algorithm when a student in year [x] [does something]" [4 marks]

**Key skills:**
- Track each variable separately in columns
- Record line number for each change
- Only write in a cell when the variable changes
- Track output messages exactly (with or without quotes — check mark scheme)
- Common traps: `total = 0` inside a loop (logic error — resets each iteration), loop starting at 1 instead of 0 (misses first element)

**Past paper trace examples:**
- 2022: Staff ID string concatenation with while loop (staffID builds up with "x" padding)
- 2023: do-until loop counting down from 3 to -1 (start=3, 2, 1, 0; stop at -1; output "Finished")
- 2024: Javelin score algorithm (nested if/elseif, year group multiplier)
- Section B trace in 2025: array of acts across stages, total calculation

---

### 4. Logic Errors — Identify and Fix
**Marks: 4 in 2022, 4 in 2023, 4 in 2024 | Appeared 3/4 years — treat as near-guaranteed**

**What gets tested:**
- Given a pseudocode algorithm, identify the line number(s) of logic errors
- Write the corrected line of code

**Exact question wording:**
- "Identify the line number of the two logic errors in the algorithm and refine the code to correct each logic error." [4 marks]
- "Identify two logic errors in the pseudocode algorithm. Write the refined line to correct each error." [4 marks]

**Common logic errors tested:**
- Array index starting at 1 instead of 0 (misses first element): `for count = 1 to array.length` → should be `0 to array.length - 1`
- `total = 0` placed inside a loop instead of before it (resets total every iteration)
- Wrong operator: `total = scores[x] + total` written as `scores[x] = total + total`
- Wrong variable in expression: `total = num1 + num1` instead of `num1 + num2`
- Condition wrong: `if total >= 10` instead of `if total >= 10 AND total <= 20`
- Loop bounds off by 1 (e.g. using `.length` without subtracting 1 for 0-indexed arrays)

**Pattern:** Always exactly 2 logic errors, always 4 marks (1 mark per line number + 1 mark per correction). Line numbers are always explicitly given.

---

### 5. Data Types
**Marks: 3–4 every year | Always in Section B in context of the scenario**

**What gets tested (every year):**
- Given a table of variables with example values, identify the most appropriate data type
- Choose from: Boolean, Char, String, Integer, Real (Float), sometimes Array

**Exact question wording:**
- "Tick (✓) one box in each row to identify the most appropriate data type for each variable." [4 marks]
- "Identify the most appropriate data type for each variable used by the program. Each data type must be different." [3 marks]
- "State the most appropriate data type for the following fields: [Nights, Room]" [2 marks]
- "Give the name of one field that could be stored as a Boolean data type." [1 mark]

**Key rules for data type selection:**

| Data Type | Use When |
|-----------|----------|
| Boolean | Only two possible values (True/False, Yes/No, on/off, armed/disarmed) |
| Integer | Whole numbers (age, year, count, number of nights) |
| Real/Float | Decimal numbers (price, distance, time in seconds with decimal precision) |
| String | Text, names, phone numbers, postcodes, anything with letters or mixed characters |
| Char | Single character |

- Phone numbers → **String** (can start with 0, may have +, spaces, brackets)
- Usernames → **String**
- Prices → **Real**
- Sensor active/armed → **Boolean**
- Timer in seconds (nearest second) → **Integer**

---

### 6. SQL Queries
**Marks: 3–4 every year | Always in Section B in context of the scenario's database**

**What gets tested (every year):**
- Write or complete a SELECT SQL statement with WHERE condition

**Exact question wording:**
- "Write an SQL statement to display [field(s)] of [records] that [condition]." [3 marks]
- "Complete the SQL statement to show [fields] of all [table records] who [condition]." [4 marks]
- "Rewrite the SQL statement so that it is correct." [4 marks]

**Standard SQL template:**
```
SELECT [field1, field2] / SELECT *
FROM [TableName]
WHERE [condition]
```

**Mark scheme pattern (consistent across all years):**
- 1 mark: correct SELECT with specified field(s)
- 1 mark: correct FROM with table name
- 1 mark: WHERE keyword present
- 1 mark: correct condition (field operator value)

**Past paper SQL questions:**
- 2022: `SELECT FirstName, Surname, Nights, Room, StayComplete FROM TblBookings WHERE Nights > 1`
- 2023: `SELECT SensorID FROM events WHERE SensorType = "Door" AND Length > 20`
- 2024: `SELECT StudentID, TeamName FROM TblResult WHERE YearGroup = 11`
- 2025: SQL on festival database (exact fields not confirmed — expect similar pattern)

**Key rules:**
- Field names and table names must be spelled exactly as given
- String values in WHERE must be in quotes: `WHERE SensorType = "Door"`
- Numeric values do NOT need quotes: `WHERE Nights > 1`
- Use `>`, `<`, `>=`, `<=`, `=` in conditions
- Combining conditions: `AND`, `OR`
- `SELECT *` selects all fields (acceptable unless specific fields asked for)

---

### 7. Testing — Types, Test Plans, Test Data
**Marks: 3–8 every year (highly variable) | Appears in multiple sub-questions**

**What gets tested:**
- Classify test data as Normal / Boundary / Invalid/Erroneous
- Complete a test plan with test data and expected output
- Name and describe types of testing (final/terminal, iterative/incremental, black box, white box, boundary)
- Explain why programs should be tested before use
- Name and describe features of an IDE used in testing

**Exact question wording patterns:**
- "Complete the following test plan to check whether [variable] is validated correctly." [3 marks]
- "Identify the type of test for each piece of test data." [4 marks]
- "Explain why programs should be tested before use." [2 marks]
- "Name and describe one type of test that should be used." [2 marks]
- "Identify and describe two features of an IDE that can be used when testing." [4 marks]

**Test data types:**
| Type | Definition | Example (for range 1–100) |
|------|-----------|--------------------------|
| Normal | Typical valid data within range | 50, 27 |
| Boundary/Extreme | At the exact edge of valid range | 1, 100 |
| Invalid/Erroneous | Data that should be rejected | 0, 101, "Hello", -5 |

**2025 example (confirmed):** Program accepts integers 1–100
- 27 → Normal
- "Hello" → Invalid/Erroneous
- 105 → Invalid/Erroneous
- 100 → Boundary

**Types of testing:**
- **Iterative/Incremental:** During development, after each module
- **Final/Terminal:** At end of development, before release, tests whole product
- **Black box:** Tests without knowledge of internal code
- **White box:** Tests with access to and knowledge of the code

**IDE features for testing (4/4 years this comes up):**
- Translator/interpreter: converts and runs code, stops at errors
- Debugger: finds and helps fix errors, stepping through line by line
- Variable watch: shows contents of variables during execution
- Breakpoints: pauses program execution at a set point
- Run-time environment/output window: shows program output
- Error reporting: identifies location and details of errors

---

### 8. Writing Extended Algorithms (Section B main question)
**Marks: 6 every single year | Always the final or near-final question in Section B**

**What gets tested:**
- Write a complete algorithm using OCR Exam Reference Language (ERL) or a studied high-level language
- Usually involves: input, iteration (loop), selection (if/else), calculation, output

**Exact question wording patterns:**
- "Write an algorithm to: • [bullet list of requirements]" [6 marks]

**Past paper algorithm tasks:**
- 2022: Input quantity of numbers, loop to input each, calculate and output total AND average [6 marks]
- 2022: Input hours parked and if electric, calculate price (£4/hr or £2/hr), repeat until 0 hours [6 marks]
- 2023: Algorithm for adding game: 3 questions, random numbers 1–10, check answers, add to score, display score [6 marks]
- 2024: Input team name and score repeatedly until "stop", find team with highest score, output winner [6 marks]
- 2025: Ticket booking — input until no tickets (500) remain, output confirmation/rejection [~6 marks]

**OCR Exam Reference Language (ERL) key syntax:**
```
// Variables and assignment
x = 5
name = "Alice"

// Input/Output
x = input("Enter a number")
print("Result is " + str(x))

// Arithmetic
+   -   *   /   MOD   ^   DIV

// Comparison
==  !=  <  >  <=  >=

// Boolean operators
AND  OR  NOT

// Selection
if condition then
    // code
elseif condition then
    // code
else
    // code
endif

// Count-controlled loop
for x = 1 to 10
    // code
next x

// Condition-controlled loop
while condition
    // code
endwhile

// Post-condition loop
do
    // code
until condition

// Functions
function myFunc(param1, param2)
    // code
    return value
endfunction

// Procedures
procedure myProc(param1)
    // code
endprocedure

// Arrays
array[0]  // first element (0-indexed)
array.length  // number of elements

// 2D arrays
array[row, col]

// Random numbers
x = random(1, 10)  // generates 1 to 10 inclusive

// String operations
str.upper   str.lower
str.length  str.left(n)  str.right(n)
str.substring(start, length)

// Type conversion
int(x)   str(x)   float(x)

// File handling
myFile = open("filename.txt")
line = myFile.readLine()
myFile.writeLine(data)
myFile.close()
while NOT myFile.endOfFile()
```

**Mark scheme pattern for 6-mark algorithms (always 6 bullet points, 1 mark each):**
- BP1: Input with message stored/used
- BP2: Attempt at iteration
- BP3: Loop correct (right number of times / correct condition)
- BP4: Correct calculation within loop
- BP5: Correct selection/output within loop
- BP6: Final output after loop

---

### 9. Programming — Writing/Completing Functions and Programs
**Marks: 4–10 every year across multiple sub-questions | Section B core**

**What gets tested:**
- Complete a partially written function with missing conditions or logic
- Write a function from scratch with parameters, body, and return value
- Write a procedure (no return value)
- Write code that calls a function with correct parameters

**Exact question wording patterns:**
- "Create a function, [name()], that takes [parameters] as parameters, calculates and returns [value]." [4 marks]
- "Write program code, that uses [function()], to output [result]." [3 marks]
- "Complete the function [name()]" [4–6 marks]
- "Write a program that checks [conditions] and calls [procedure()] when appropriate." [4 marks]
- "Write the procedure [name()]" [6 marks]

**Mark scheme pattern for functions (4 marks):**
- BP1: Correct function definition header (function keyword + name)
- BP2: Correct parameter(s) in signature
- BP3: Correct calculation using parameter values
- BP4: Returns (not prints) the calculated value

**Past paper function examples:**
- 2022 `newPrice(nights, room)`: returns 60*nights or 80*nights depending on room type
- 2022 `newPrice("premium", 5)` call: print the returned value
- 2023: Program checking SystemArmed AND (DoorSensorActive OR WindowSensorActive) → call SoundAlarm()
- 2023 `SaveLogs(data, filename)`: procedure opening file, writing data, closing file
- 2024 `moveCharacter(direction, position)`: subtract/add 5, clamp 1–512, return position
- 2024 `linearSearch(studentName)`: loop through array, return True/False

**Key rules:**
- Functions RETURN a value; procedures do NOT return (they just do something)
- Parameters are listed in the function definition; must be used in the body
- Do NOT use `input()` inside a function if parameters are provided — use the parameters
- `return` sends a value back; `print()` outputs to screen — these are different!

---

## TIER 2 — High Priority (3/4 years or high marks when appears)
*Learn these well — they appear most years and carry significant marks when they do.*

---

### 10. Sorting Algorithms — Merge Sort, Bubble Sort, Insertion Sort
**Marks: 1–6 per year | Very detailed in 2022 and 2023, lighter in 2024**

**What gets tested:**
- Complete the steps of a merge sort (show each split and merge)
- Describe differences between insertion sort and bubble sort
- Describe similarities between insertion sort and bubble sort
- Explain purpose of a variable (e.g. `temp`) in a sort algorithm
- Explain why a condition-controlled loop is needed in insertion sort
- Identify which sort algorithm uses which approach (divide and conquer = merge sort)

**Exact question wording patterns:**
- "Complete the merge sort of the data by showing each step of the process." [3 marks]
- "Describe the purpose of the variable `temp` in the insertion sort pseudocode algorithm." [2 marks]
- "Explain why the inner loop needs to be a condition-controlled loop." [2 marks]
- "Describe one difference between an insertion sort and a bubble sort." [2 marks]
- "Describe two similarities between an insertion sort and a bubble sort." [2 marks]
- "Tick one box to identify the name of the sorting algorithm that splits data into individual items before recombining in order." [1 mark]

**Merge sort steps:**
1. Split entire list into individual elements (one at a time)
2. Merge pairs into sorted pairs
3. Merge sorted pairs into sorted groups of 4
4. Merge sorted groups until one fully sorted list remains

**Example from 2022:** 45 12 -99 100 -13 0 17 -27
- Split: [45][12][-99][100][-13][0][17][-27]
- Merge pairs: [12 45][-99 100][-13 0][-27 17]
- Merge fours: [-99 12 45 100][-27 -13 0 17]
- Merge: [-99 -27 -13 0 12 17 45 100]

**Insertion vs Bubble sort:**

| | Insertion Sort | Bubble Sort |
|--|----------------|------------|
| Difference | Inserts values into correct position; starts sorted partition at left | Compares/swaps pairs; bubbles highest to top; needs multiple passes |
| Similarity | Both produce a sorted list; both use loops; both compare values; both may need multiple passes |

**temp variable:** Holds a value temporarily during a swap so it is not lost when one array position is overwritten.

---

### 11. Searching Algorithms — Binary Search and Linear Search
**Marks: 6 in 2022, 4 in 2024 | Skipped in 2023 and 2025**

**What gets tested:**
- Describe steps of a binary search on a sorted list
- Show a binary search finding a specific value (step by step)
- Describe steps of a linear search (including when the value is NOT found)
- State a pre-requisite for binary search (data must be sorted)

**Exact question wording:**
- "Describe the steps a binary search will follow to look for a number in a sorted list." [4 marks]
- "Describe the steps a linear search would follow when searching for a number that is not in the given list." [2 marks]
- "Show how a binary search will be used to find the number [x] in the following data set." [3 marks]
- "State one pre-requisite for a binary search algorithm." [1 mark]

**Binary search steps (4 marks):**
1. Select/pick the middle number
2. Check if it equals the target
3. If target is larger, discard left half; if smaller, discard right half
4. Repeat until found or list is empty/size 1 (not found)

**Linear search steps (2 marks):**
1. Start with the first value
2. Check each value in order (until found OR all values checked and not found)

**Pre-requisite:** Data must be **sorted/in order**.

---

### 12. Validation
**Marks: 2–6 | Appeared 2022, 2023, 2024, 2025 (varies 3/4 years)**

**What gets tested:**
- Name two types of validation and explain how they work in context
- Complete a validation algorithm (input with condition checking)
- Describe what each validation type does

**Exact question wording:**
- "Identify two methods of validation and explain how they can be used on this [program]." [6 marks]
- "Write an algorithm to take [input] and output 'VALID'/'NOT VALID' depending on [condition]." [4 marks]
- "Complete the following program to validate the inputs." [5 marks]

**Types of validation:**

| Type | What it checks | Example use |
|------|----------------|-------------|
| Range check | Value is within min/max limits | Nights must be 1–5 |
| Type check | Data is correct data type | Answer must be integer |
| Presence check | Field is not empty/blank | Name not empty |
| Length check | Number of characters | Username 6–12 chars |
| Format check | Matches a set pattern | Postcode format |
| Look-up/table check | Value is from a known list | Room must be "basic" or "premium" |

**Writing validation algorithms (mark scheme pattern for 5 marks):**
```
firstName = input("Enter first name")
room = input("Enter basic or premium")
nights = int(input("Enter 1 to 5 nights"))

if firstName != "" and room == "basic" or room == "premium" and nights >= 1 and nights <= 5 then
    print("ALLOWED")
else
    print("NOT ALLOWED")
endif
```
- 1 mark: checks string not empty
- 1 mark: checks string is from valid list
- 1 mark: checks numeric value within range (both boundaries)
- 1 mark: outputs NOT ALLOWED if any invalid
- 1 mark: outputs ALLOWED only if all valid

---

### 13. Arrays (1D and 2D)
**Marks: 6 in 2023 (2D array), 4 in 2025 (1D array trace) | Appeared 2/4 years**

**What gets tested:**
- Write a program using a 2D array to access elements by row/column
- Complete a linear search using a 1D array
- Trace through an algorithm using an array
- Identify correct indexing (0-indexed in OCR)
- Convert non-string data before storing in a string array (casting)

**Key facts:**
- OCR arrays are **0-indexed** (first element is at index 0)
- `array.length` returns the number of elements
- 0-indexed loop: `for count = 0 to array.length - 1`
- 2D array: `array[row, col]` or `array[row][col]`
- 2D array example: `arrayEvents[0, 3]` = first row, fourth column (Length)

**Linear search function pattern (2024):**
```
function linearSearch(studentName)
    for count = 0 to theTeam.length - 1
        if theTeam[count] == studentName then
            return True
        endif
    next count
    return False
endfunction
```

---

### 14. File Handling
**Marks: 6 in 2023, 6 in 2025 | Appeared 2/4 years — now 2 years in a row, becoming more likely**

**What gets tested:**
- Write a procedure that opens a file, writes data, closes a file
- Complete an algorithm using file reading operations (readLine, endOfFile, close)
- Identify how casting is used when reading from a file

**OCR ERL file handling syntax:**
```
// Open file (for reading)
myFile = open("filename.txt")

// Read one line
line = myFile.readLine()

// Check end of file
while NOT myFile.endOfFile()
    data = myFile.readLine()
    // process data
endwhile

// Write to file
myFile.writeLine(data)

// Close file (always required)
myFile.close()
```

**2025 file handling question (confirmed):**
```
myFile = open("data.txt")
while NOT myFile.endOfFile()
    temp = myFile.readLine()
    if int(temp) != 0
        print(temp)
    endif
endwhile
myFile.close()
```
- Casting: `int(temp)` converts string from file to integer for comparison

**2023 procedure pattern:**
```
procedure SaveLogs(data, filename)
    logFile = open(filename)
    logFile.writeLine(data)
    logFile.close()
endprocedure
```

---

### 15. Translators — Compiler vs Interpreter
**Marks: 3–5 in 2022 and 2024 | Appeared 2/4 years**

**What gets tested:**
- Describe benefits of using a compiler instead of an interpreter
- Identify what type of language a program is written in
- Explain what happens when each type of translator encounters an error
- Name translator types in fill-in-the-blank

**Compiler vs Interpreter:**

| | Compiler | Interpreter |
|--|---------|------------|
| Process | Translates ALL code at once | Translates ONE LINE at a time |
| Error handling | Shows ALL errors at end; doesn't run until error-free | **STOPS** at first error; can be corrected and continued from same point |
| Output | Produces **executable file** | No executable file |
| End user needs | Does NOT need compiler to run | Needs interpreter to run |
| Speed | Runs FASTER (already translated) | Runs SLOWER (translating each time) |
| Source code | End users do NOT get source code | Easier for debugging |
| Best for | Distribution to end users | Development/debugging |

**Fill-in-the-blank (2022):** "Jack writes his program in a **high-level** language...an interpreter...it **stops** when an error is found...A compiler...The code will not run until there are **no** errors. The **executable** file produced can be run **without** the compiler."

---

### 16. Maintainability
**Marks: 2–4 in 2022 and 2024 | Appeared 2/4 years**

**What gets tested:**
- Give two ways to improve the maintainability of a program
- Describe each method with an example

**Methods and descriptions:**
| Method | What it does |
|--------|-------------|
| Add comments | Explains what code does; makes it easier for other programmers to follow |
| Meaningful variable names | Variables named to show their purpose (e.g. `totalScore` not `x`) |
| Use subroutines/functions | Breaks code into reusable blocks; easier to follow and update |
| Use constants | Stores fixed values in one place (e.g. `constant PRICE = 60`) so only needs changing once |

**Exact wording (2022):** "Give two ways that the maintainability of this program could be improved." — answer: add comments; use meaningful variable names; put code into subroutines; use a loop/iteration.

**Note:** Indentation is NOT usually accepted (if code is already indented). Focus on the 4 methods above.

---

### 17. Computational Thinking — Decomposition and Abstraction
**Marks: 2 in 2022, 2 in 2024 | Appeared 2/4 years**

**What gets tested:**
- Name the computational thinking technique from a description
- Identify one way abstraction or decomposition has been used in a specific program design

**Key definitions:**
- **Decomposition:** Breaking a complex problem down into smaller, more manageable problems/sub-problems
- **Abstraction:** Hiding or removing irrelevant details from a problem to reduce complexity; focusing on what is important

**Question pattern 1 (2022):** "State the name of each of the following computational thinking techniques."
- "Breaking a complex problem down into smaller problems." → Decomposition
- "Hiding or removing irrelevant details from a problem to reduce the complexity." → Abstraction

**Question pattern 2 (2024):**
- "Identify one way that abstraction has been used in the design of this program." → Must be specific to the scenario, e.g. "focus on student names and events, ignore students' favourite subjects"
- "Identify one way that decomposition has been used in the design of this program." → Must be specific, e.g. "splits the program into different events (javelin, high jump, etc.)"

---

### 18. Flowcharts
**Marks: 4–5 in 2022 and 2024 | Appeared 2/4 years**

**What gets tested:**
- Complete a flowchart (add missing boxes/conditions)
- Draw a flowchart from an algorithm description

**Flowchart shapes:**
| Shape | Name | Use for |
|-------|------|---------|
| Rounded rectangle (oval) | Terminal | Start and End |
| Parallelogram | Input/Output | INPUT and OUTPUT operations |
| Rectangle | Process | Calculations and assignments |
| Diamond | Decision | If/else conditions (two exits: Yes and No) |
| Arrow | Flow line | Connecting boxes |

**Exact shape marking:** The mark scheme is strict about shapes:
- Inputs and outputs MUST use parallelogram
- Decisions MUST use diamond with exactly two lines out
- Penalise wrong shapes but only once, then follow through

---

### 19. Low-Level vs High-Level Languages
**Marks: 2–4 in 2023 and 2024 | Appeared 2/4 years**

**What gets tested:**
- Tick table identifying characteristics of low-level vs high-level language
- Give reasons why some programs are written in low-level languages

**Low-level language characteristics:**
- Allows direct manipulation of memory/hardware
- Machine/architecture specific
- Instructions map directly to processor instructions
- More efficient (no translation needed at runtime)
- Faster execution
- Assembly language: one-to-one mapping to machine code

**High-level language characteristics:**
- Platform-independent (same language across different hardware)
- Uses English-like words
- Needs translation (compiler or interpreter) to run
- Easier to write and debug
- Abstracted from hardware

**Reasons to use low-level:**
1. Does not need to be translated (faster execution)
2. Direct control of hardware/memory
3. Can optimise code more specifically
4. Less memory usage
5. Can program for specific hardware

---

### 20. String Manipulation
**Marks: 6 in 2024 | Appeared 1/4 years but carries high marks**

**What gets tested:**
- Apply string functions and predict output
- Write pseudocode using string concatenation

**OCR ERL string operations:**
```
message = "abcd1234"
message.length         // 8 (number of characters)
message.upper          // "ABCD1234"
message.lower          // "abcd1234"
message.left(4)        // "abcd" (first 4 characters)
message.right(4)       // "1234" (last 4 characters)
message.substring(2,3) // 3 chars starting from position 2
int(message.right(4))  // converts "1234" to integer 1234
```

**Concatenation:** Using `+` to join strings
```
word1 = "Hello"
word2 = "Everyone"
message = word1 + word2   // "HelloEveryone"
```

**2024 example:**
- `print(message.length)` → 8
- `print(message.upper)` → ABCD1234
- `print(message.left(4))` → abcd
- `print(int(message.right(4))*2)` → 2468

---

### 21. Casting (Type Conversion)
**Marks: 1–2 | Appeared 3/4 years but usually 1–2 marks**

**What gets tested:**
- Define casting
- Identify the line number where casting occurs
- Identify the process that converts integer to string (or string to integer)

**Definition:** Casting is the process of converting a value from one data type to another.

**OCR ERL casting functions:**
- `int(x)` — converts to integer
- `str(x)` — converts to string
- `float(x)` or `real(x)` — converts to real/float

**Past paper examples:**
- 2022: `str(year)` on line 03 converts integer year to string for concatenation in staffID
- 2023: `int()` converts string from 2D array to integer for arithmetic
- 2025: `int(temp)` in file handling converts string read from file to integer for comparison

---

### 22. IDE Features
**Marks: 4 | Appeared 2023 and 2025 (2/4 years)**

**What gets tested:**
- Name and describe two features of an IDE (almost always for testing)

**Key IDE features and descriptions:**
| Feature | Description |
|---------|-------------|
| Translator/Interpreter/Compiler | Converts code to machine code so it can be run/executed |
| Debugger | Helps find and fix errors; can step through code line by line |
| Variable watch | Shows the contents/values held in variables during execution |
| Breakpoints | Pauses program execution at a chosen/set position |
| Run-time environment / Output window | Allows the program to be run; shows output of code |
| Error reporting / diagnostics | Identifies location and detail of errors; suggests fixes |
| Text/code editor | Allows program code to be written, entered, changed |
| Pretty printing / keyword highlighting | Colours/identifies keywords and variables |
| Keyword completion / syntax suggestion | Suggests code/syntax when first part is entered |

**Pattern:** "Identify and describe two features of an IDE that can be used when [testing / implementing the flowchart]." [4 marks] = 1 mark per feature name + 1 mark per matching description.

---

## TIER 3 — Lower Priority (1/4 years or very low marks)
*Know the basics but do not over-invest revision time.*

- **Arithmetic operators** (*, /, +, -, MOD, ^) — usually only 1–2 marks, tested as sub-parts
- **Pseudocode reading** — understanding what code does (always embedded in larger questions)
- **Code analysis (line numbers, concatenation, function calls)** — appeared in 2023 for 4 marks total across 5 sub-parts worth 1 mark each
- **Programming constructs in code** (sequence, selection, iteration) — "name two programming constructs used" [2 marks]

---

## PAPER STRUCTURE OVERVIEW

| Section | Time | Marks | Character |
|---------|------|-------|-----------|
| Section A | ~50 mins | ~40 marks | Standalone questions; broad topic coverage; shorter answers; tests knowledge and understanding across the whole spec |
| Section B | ~40 mins | ~40 marks | Single extended scenario; 8–10 sub-questions on ONE context; programming-heavy; OCR ERL or high-level language required |

**Section A always includes:**
- Selection/iteration identification tick table [3–4 marks]
- Logic gate drawing or truth table [5–7 marks]
- Trace table or algorithm tracing [3–4 marks]
- Logic error identification [4 marks in 3/4 years]
- Testing questions [2–8 marks]
- At least one definition question

**Section B always includes:**
- Data type identification [3–4 marks]
- SQL query [3–4 marks]
- Programming (function/procedure/algorithm) [4–10 marks]
- Extended algorithm writing [6 marks]
- Often: trace table [3–4 marks]
- Increasingly: file handling [5–6 marks, 2023 and 2025]

---

## QUICK REFERENCE — MARK SCHEME ANSWER PATTERNS

### Things examiners accept
- Any logically equivalent code (not just exact OCR ERL syntax)
- High-level language syntax (Python, Java, C#, Visual Basic, etc.) for programming questions
- Either 0-indexing or 1-indexing for loops (with ±1 tolerance)
- Alternative variable names as long as consistent
- Minor spelling variations in answer (not for keywords or field names)

### Things examiners do NOT accept
- Structured English or flowcharts for programming questions (Section B)
- `print()` instead of `return` in a function definition
- `>=` without the second boundary (for range validation you need BOTH limits)
- Missing quotation marks around string values in SQL WHERE clauses
- `SELECT *` when specific fields are required
- Definition of a function when a function CALL is asked for
- Repeating the type name without description (e.g. "boundary test, tests the boundary")

### Common trap answers to avoid
- `while hours > 0` — wrong! Use `while hours != 0` (negative hours would bypass this)
- `for count = 1 to array.length` — misses element at index 0
- `total = 0` inside a loop — resets total each iteration
- `if firstname or surname == ""` — logically incorrect (OR doesn't work this way)
- `score + 1` (without assignment) — doesn't update score; needs `score = score + 1`

---

## SECTION B SCENARIO PREDICTION

Based on 4-year pattern analysis, Section B scenarios follow this pattern:
- A real-world system with named variables, a database, and programming tasks
- Always includes: data storage, user input, validation or calculation, database query (SQL), programming output
- 2022: Hotel → 2023: Security → 2024: Sports day → 2025: Music festival

**For 2026 — possible contexts based on what hasn't appeared:**
- Library system, hospital/medical system, e-commerce/shop system, transport/travel system, school management system

**Regardless of context, Section B will always test:**
1. Data types from the scenario's variables
2. SQL on the scenario's database
3. A programming task (function, procedure, or algorithm)
4. A trace table for one of the scenario's algorithms
5. Either validation OR file handling (both have appeared recently)
6. A 6-mark extended algorithm as the final question
