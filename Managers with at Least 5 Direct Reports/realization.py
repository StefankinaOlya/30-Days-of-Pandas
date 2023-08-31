import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    output = employee.groupby(['managerId'])['id'].agg(['count']).reset_index()
    output = output.loc[output['count']>=5,['managerId']]
    output = employee.loc[employee['id'].isin(output['managerId']),['name']]

    return output
