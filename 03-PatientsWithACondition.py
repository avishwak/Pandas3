# Problem 3 : Patients with a Condition ( https://leetcode.com/problems/patients-with-a-condition/)

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(patients)):
        p_id = patients['patient_id'][i]
        p_name = patients['patient_name'][i]
        cond = patients['conditions'][i]
        for c in cond.split():
            if c.startswith('DIAB1'):
                result.append([p_id, p_name, cond])
                break
    return pd.DataFrame(result, columns=['patient_id','patient_name', 'conditions'])

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients['conditions'].str.startswith('DIAB1') | patients['conditions'].str.contains(' DIAB1')]
    return df

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r"(^|\s)DIAB1", regex=True)]

"""
# Note: isin matches the whole string and is not suitable for this case.
r: raw string
^: matches the start of the string
\s: matches any whitespace character (space, tab, newline)
DIAB1: the condition we are looking for
The regex pattern r"(^|\s)DIAB1" ensures that "DIAB1" is either at the start of the string or preceded by a whitespace character.
"""