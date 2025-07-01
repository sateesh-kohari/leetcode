# Combine Two Tables
"SELECT firstName, lastName, city, state FROM person PER LEFT JOIN Address ADD ON PER.personId = ADD.personId"


# Second Highest Salary
"SELECT (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1,1) Aas SecondHihestSalary"