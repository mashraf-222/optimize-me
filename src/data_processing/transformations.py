from typing import List, Any

import pandas as pd


def pivot_table(
    df: pd.DataFrame, index: str, columns: str, values: str, aggfunc: str = "mean"
) -> dict[Any, dict[Any, float]]:
    result = {}
    if aggfunc == "mean":
        def agg_func(lst):
            return sum(lst) / len(lst)
    elif aggfunc == "sum":
        def agg_func(lst):
            return sum(lst)
    elif aggfunc == "count":
        def agg_func(lst):
            return len(lst)
    else:
        raise ValueError(f"Unsupported aggregation function: {aggfunc}")
    grouped_data = {}

    # Extract relevant columns as numpy arrays for efficient iteration
    df_index = df[index].to_numpy()
    df_columns = df[columns].to_numpy()
    df_values = df[values].to_numpy()

    for index_val, column_val, value in zip(df_index, df_columns, df_values):
        if index_val not in grouped_data:
            grouped_data[index_val] = {}
        if column_val not in grouped_data[index_val]:
            grouped_data[index_val][column_val] = []
        grouped_data[index_val][column_val].append(value)
    for index_val in grouped_data:
        result[index_val] = {}
        for column_val in grouped_data[index_val]:
            result[index_val][column_val] = agg_func(grouped_data[index_val][column_val])
    return result


def melt(df: pd.DataFrame, id_vars: List[str], value_vars: List[str]) -> pd.DataFrame:
    result_data = []
    for i in range(len(df)):
        id_values = {id_var: df.iloc[i][id_var] for id_var in id_vars}
        for value_var in value_vars:
            new_row = {
                **id_values,
                "variable": value_var,
                "value": df.iloc[i][value_var],
            }
            result_data.append(new_row)
    return pd.DataFrame(result_data)
