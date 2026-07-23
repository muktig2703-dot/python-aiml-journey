#Exercise 1
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Program started successfully.")

#Exercise 2
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")
logging.info("Information")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error")

#Exercise 3
import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
logging.info("Application started.")
logging.warning("Low memory warning.")
logging.error("Something went wrong.")

#Student Login Logger
import logging
logging.basicConfig(
    filename="student.log",
    level=logging.INFO
)
name = input("Enter Name: ")
branch = input("Enter Branch: ")
logging.info(f"Student Login -> Name: {name}, Branch: {branch}")
print("Student login recorded successfully!")