# AI Code Review Assignment (Python)

## Candidate
- Emtital Malik
- Approximate time spent: 

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
-  The function returns the total amount of all non-cancelled orders divided by the total number of orders len(orders) without excluding cancelled orders. This leads to an incorrect average.


### Edge cases & risks
- The function does not account for orders with missing 'status' or 'amount' fields. 
- If there are no valid orders, the function will divide by zero and crash.
- If the amount value is non-numeric, it will cause type errors during calculation.

### Code quality / design issues
- The code does not handle missing or invalid fields, which affects the overall reliability of the function.

## 2) Proposed Fixes / Improvements
### Summary of changes
-   Track a separate counter for valid orders and divide by that counter instead of (len(orders))
- Handle missing status by treating it as cancelled and skipping them 
- Skip orders with missing amounts 
- Convert amount to a float before summing to handle numeric strings values.
- Return 0.0 when no valid order exists to avoid division by zero

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty list : returns 0.0 (no crash).
- All orders cancelled or invalid fields : returns 0.0.
- Mixed cancelled and non-cancelled orders : average calculated using only valid(non-cancelled) orders.
- Orders with missing status : Skipped (treated as cancelled).
- Orders with missing amount : Skipped.
- Amount as numeric string ("100.5") : correctly converted and included in the calculation.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It claims cancelled orders are excluded from the calculation, while the denominator (number of orders) still includes them.
- It does not address  division-by-zero and missing fields cases, which can lead to crashing or incorrect results.  


### Rewritten explanation
- The function computes the average order value by summing the amounts of non-cancelled orders and dividing by the number of non-cancelled orders. Orders with missing 'status' are treated as cancelled and orders with missing 'amount' are skipped, when there are no valid orders te function returns 0.0.

## 4) Final Judgment
- Decision: Request Changes 
- Justification: The original function produces an incorrect average when cancelled orders exist, and can crash or return invalid results with empty input or missing fields.
- Confidence & unknowns:High confidence in identifying the incorrect denominator and division by zero. The handling of missing 'status' or 'amount' is based on a defensive assumption, as the requirements do not specify how such cases should be treated.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The original function counts an email as valid if it contains "@" anywhere, which is not sufficient.
- It can crash if the input contains non-string values


### Edge cases & risks
- the original function does not handle where emails is None.
- Emails with spaces in the middle should not be counted as valid.
- Emails with an improper username host format(username@host) shouldn't be counted as valid.
- Emails with no "." in the host part are treated as invalid based on chosen validation rule.

### Code quality / design issues
- The validation rule is weak to check for valid emails, as the function name suggests. 
- There is no clear handling for invalid types or malformed data. 

## 2) Proposed Fixes / Improvements
### Summary of changes
- Returns 0 if the input emails list is empty or None 
- Ignore non-string entries 
- Apply a validation rule (exactly one "@" in each email, non-empty text before and after "@", no spaces, and the host contains "." that is not at the start or end of the host part).
- Increment count only when all checks pass.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty list and None input : returns 0.
- Mixed types (None, numbers, objects) : ignored.
- Invalid formats ("@", "a@", "@b.com", "a@@b.com", "a@b", "a@.com", "a@b.", "a b@c.com") : not counted.
- Valid-looking emails ("user@gmail.com", "first.last@domain.org", "a@b.co") : counted correctly.
- Leading/trailing spaces (" user@gmail.com ") : still counted after stripping.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original function does not validate emails, it only checks if the string contains "@".
- It does not safely ignore invalid entries like non-string values. 
- It does not explain what a valid email is.

### Rewritten explanation
- The function counts how many enteries in the input are valid email addresses using a basic validation rule that checks for non-string and malformed values and ignores them, counts the email as valid if it has only one "@" with a non-empty text before and after it and has a "." in the host part where it's not in the start or the end, if the input is empty or None the function returns 0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original function incorrectly clasify invalid email addresses as valid and can crash with non-string values, so it does not match its explanation
- Confidence & unknowns: High confidence in the identified issues and fixes. Email validation can be more complex in actual systems but a basic validation rule is used in this task. 

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The original function divides by len(values), even though it ignores None values in the total, which results in an incorrect average when there are missing values.
- It crashes when the list is empty due to division by zero  

### Edge cases & risks
- If all values are None or invalid, the function should not divide by zero.
- Inputs with mixed types can cause float(v) to raise errors (e.g., "", "abc", or objects).
- If values is None, iterating over it will cause the loop to crash.

### Code quality / design issues
- The original function does not handle invalid or non-numeric inputs, even though the explanation claims it safely handles them .
- The denominator logic is inconsistent with how the total is filtered, but the count is not.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Return 0.0 when the input is None or empty to avoid errors and division by zero.
- Convert values to float and ignores entries that can't be converted with try/except.
- Track the number of valid measurements and divide by that count instead of len(values).
### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list : returns 0.0 without crashing.
- None input : returns 0.0.
- All values None : returns 0.0.
- Mixed numeric values and None : averages only valid numeric values.
- Numeric strings (e.g., "10", "3.5") : correctly converted and included.
- Mixed invalid types (e.g., ["10", None, "dfg", {}, [], 3]) → ignore invalid entries without crashing and average only valid numeric values.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- None values are ignored in the total, but the denominator includes all values, which produces an incorrect average when missing values exist.
- The function does not safely handle mixed input types.
- Division-by-zero cases are not addressed.

### Rewritten explanation
- The function computes the average of valid measurements by dividing the total of measurement values by the number of valid measurements, while ignoring None values. It converts valid entries to float and skips entries that cannot be converted to numbers. If the input is empty or None or there are no valid measurements, it returns 0.0.
## 4) Final Judgment
- Decision: Request Changes
- Justification: The original function produces an incorrect average due to a wrong denominator, and can crash on empty input or an invalid entry type. so it does not match the explanation.
- Confidence & unknowns: High confidence in the identified issues and fixes. Skipping invalid/non-numeric values is a design choice made to keep the function robust and consistent with valid measurements.
