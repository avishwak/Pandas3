# Problem 2 : Fix Names in a Table	(	https://leetcode.com/problems/fix-names-in-a-table/ )

import pandas as pd

# solution 1: manual implementation
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by=['user_id'])

# solution 2: inbuilt method
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by=['user_id'])

'''
#Note: there is a .title(), but it is will capitalizes the first letter of each word.
'''