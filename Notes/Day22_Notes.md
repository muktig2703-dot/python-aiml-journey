# Day 22 Notes - Working with Date and Time in Python
# Topics Covered
`datetime` Module
`datetime.now()`
`date.today()`
`strftime()`
Creating Custom Dates
Date Calculations
Student Age Calculator Project

# 1. Introduction to the `datetime` Module
## Definition
The `datetime` module is a built-in Python module used to work with dates and times.
It helps programmers perform operations such as:
Getting the current date and time
Formatting dates and times
Creating custom dates
Calculating age
Measuring time differences
Recording timestamps
The `datetime` module is widely used in web development, automation, AI, data analysis, and software applications.

# 2. Importing the Module
To use the `datetime` module:
python id="2uvvje"
from datetime import datetime
To work only with dates:
python id="kttv87"
from datetime import date

# 3. `datetime.now()`
The `datetime.now()` function returns the current date and time of the system.
Example:
python id="yshjlwm"
from datetime import datetime
now = datetime.now()
print(now)
Example Output:
text id="ekw3ci"
2026-07-17 15:30:45.123456

# 4. `date.today()`
The `date.today()` function returns only the current date.
Example:
python id="xte5v6"
from datetime import date
today = date.today()
print(today)
Example Output:
text id="1e1mjl"
2026-07-17

# 5. `strftime()`
The `strftime()` function formats a date or time into a readable string.
Example:
python id="e38vqz"
from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%I:%M:%S %p"))
Example Output:
text id="ydgs84"
17-07-2026
03:30:45 PM

# 6. Common Format Codes
| Format Code | Meaning               | Example |
| ----------- | --------------------- | ------- |
| `%d`        | Day                   | 17      |
| `%m`        | Month                 | 07      |
| `%Y`        | Year                  | 2026    |
| `%H`        | Hour (24-hour format) | 15      |
| `%I`        | Hour (12-hour format) | 03      |
| `%M`        | Minutes               | 30      |
| `%S`        | Seconds               | 45      |
| `%p`        | AM / PM               | PM      |

# 7. Creating a Custom Date
A custom date can be created by passing the year, month, and day to the `datetime()` constructor.
Example:
python id="7kduik"
from datetime import datetime
birthday = datetime(2007, 3, 27)
print(birthday)
This creates a specific date instead of using the current system date.

# 8. Date Calculations
The current year can be accessed using:
python id="eozmcz"
current_year = datetime.now().year
Age can then be calculated as:
python id="3r4xem"
age = current_year - birth_year
This is a simple and common calculation used in many applications.

# 9. Student Age Calculator Project
Today's mini project included:
Taking user input
Getting the current year
Calculating the student's age
Displaying today's date
Displaying the current time
The project combined user input, arithmetic operations, and the `datetime` module into one practical application.

# 10. Advantages of the `datetime` Module
Built into Python
Easy to use
Accurate date and time calculations
Flexible date formatting
Useful for logging and scheduling
Widely used in real-world software development

# 11. Keywords Learned Today
`datetime`
`date`
`datetime.now()`
`date.today()`
`strftime()`
Timestamp
Date Formatting
Current Year
Custom Date