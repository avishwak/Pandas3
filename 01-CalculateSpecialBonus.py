# Problem 1 :Calculate Special Bonus ( https://leetcode.com/problems/calculate-special-bonus/)

import pandas as pd

# solution 1: using a loop to iterate through the DataFrame
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(employees)):
        id = employees['employee_id'][i]
        name = employees['name'][i]
        salary = employees['salary'][i]
        if (id%2==0) or (name[0]=='M'):
            result.append([id, 0])
        else: 
            result.append([id, employees['salary'][i]])
    df = pd.DataFrame(result, columns=(['employee_id', 'bonus'])).sort_values(by=['employee_id'])
    return df

# solution 2: using a loop to iterate through the DataFrame; just added the bonus column to the original DataFrame
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    for i in range(len(employees)):
        id = employees['employee_id'][i]
        name = employees['name'][i]
        salary = employees['salary'][i]
        if (id%2==0) or (name[0]=='M'):
            employees['bonus'][i] = 0
        else: 
            employees['bonus'][i] = salary
    return employees[['employee_id','bonus']].sort_values(by=['employee_id'])

# solution 3: using a vectorized approach
# Row-wise computation using DataFrame.apply() with a lambda function
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda x: x['salary'] if x['employee_id']%2!=0 and not x['name'].startswith('M') else 0,
        axis=1
    )
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')

# solution 4: Fully vectorized approach using boolean indexing and Series.where()
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
   employees['bonus'] = employees['salary'].where(
       (~employees['name'].str.startswith('M')) & (employees['employee_id'] % 2 == 1), 0
   )
   return employees[['employee_id', 'bonus']].sort_values('employee_id')

"""
# Note:

.str is used for vectorized string operations on a Series (e.g., employees['name'].str.startswith('M')).
In apply with axis=1, x['name'] is a scalar string, so native startswith() works without .str.

# The .where() method is used to replace values where the condition is False.
It keeps the original values where the condition is True and replaces them with 0 where the condition is False.
"""
