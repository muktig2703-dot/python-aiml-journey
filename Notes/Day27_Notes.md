# Day 27 Notes - Logging in Python
# Topics Covered
Logging
`logging` Module
Logging Levels
`logging.basicConfig()`
Logging to a File
Log Format
Student Login Logger Project

# 1. What is Logging?
## Definition
Logging is the process of recording information about a program while it is running.
Instead of displaying messages only on the screen using `print()`, logging stores important information that helps developers monitor, debug, and maintain applications.
Logging is widely used in backend development, web applications, automation, artificial intelligence, and large software systems.

# 2. Why Use Logging?
Logging provides several advantages over using `print()` statements.
It helps developers to:
Monitor program execution.
Track application events.
Record warnings and errors.
Debug problems more efficiently.
Save logs for future analysis.
Understand what happened after a program finishes running.
Professional applications almost always use logging instead of `print()` for recording important events.

# 3. The `logging` Module
Python provides a built-in module named `logging`.
Import statement:
python
import logging
No installation is required because it is included with Python.

# 4. `logging.basicConfig()`
The `basicConfig()` function configures how logging behaves.
Example:
python
import logging
logging.basicConfig(level=logging.INFO)
It allows developers to specify:
Logging level
Output file
Message format
Other logging options

# 5. Logging Levels
Python supports multiple logging levels.
| Level    | Purpose                                            |
| -------- | -------------------------------------------------- |
| DEBUG    | Detailed debugging information                     |
| INFO     | General application events                         |
| WARNING  | Unexpected situations that do not stop the program |
| ERROR    | Errors that affect part of the program             |
| CRITICAL | Serious errors that may stop the application       |
Example:
python
logging.debug("Debug message")
logging.info("Information")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error")

# 6. Logging to a File
Instead of displaying messages in the terminal, logs can be saved to a file.
Example:
python
import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
logging.info("Application started.")
This creates a file named:
text
app.log
which stores all log messages.

# 7. Log Format
A custom log format makes log files easier to read.
Example:
python
logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
Example Output:
text
2026-07-22 10:15:30 - INFO - Student Login Successful
Useful format options include:
`%(asctime)s` → Date and time
`%(levelname)s` → Logging level
`%(message)s` → Log message

# 8. Student Login Logger Project
Today's mini project performed the following tasks:
Accepted student name.
Accepted student branch.
Recorded login information in a log file.
Confirmed successful logging.
This demonstrated how logging can be used to maintain application records.

# 9. Advantages of Logging
Helps debug applications.
Records important events.
Stores information permanently.
Makes error tracking easier.
Improves application monitoring.
Standard practice in professional software development.

# 10. Keywords Learned Today
Logging
`logging`
`basicConfig()`
DEBUG
INFO
WARNING
ERROR
CRITICAL
Log File
Log Format