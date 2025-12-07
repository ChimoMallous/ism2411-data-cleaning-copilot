# Reflection on Using GitHub Copilot

## What Copilot Generated
Copilot generated the first five functions after I wrote the function signatures and docstrings. After creating the comments for the step, purpose, and why, I used GitHub Copilot to follow the steps while also making the code pythonic. 

## What I Modified
I made four key changes to Copilot's code. First, I added error handling to the load_data() function with a try-except block. Second, I added print statements to track how many rows were dropped. Third, I added function to convert price and qty to numeric types as it was causing errors at first, and lastly added the stripping of whitespace before converting to lowercase.

## What I Learned
This project taught me that data cleaning requires understanding your actual data structure. My script initially failed because the CSV had whitespace in column names that I didn't expect, and the price and qty columns were not being converted to numeric types. I learned to always inspect the raw data first before writing cleaning logic.

Using Copilot was helpful for writing code quickly, but it's not perfect. It gave me working code but didn't include error handling or helpful print statements. The biggest takeaway is that Copilot speeds up coding but doesn't replace critical thinking - you still need to test the code, understand what it does, and modify it for your specific needs.