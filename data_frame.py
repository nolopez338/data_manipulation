# Basic
import numpy as np
import pandas as pd


def search_df(df, entry):
    """ Check if entry appears anywhere in the DataFrame df """
    appears = df.apply(lambda x: x.astype(str).str.contains(entry)).any().any()
    if appears:  # Positive search: 'entry' is found
        print(f"{entry} : Appears\n")
        results = find_entry_in_dataframe(df, entry)
        display(results)
    else:  # Negative search: 'entry' is not found
        print(f"{entry} : No result\n")


def find_entry_in_dataframe(df, entry):
    results = {}  # Dictionary to store column indices where 'entry' is found

    for column in df.columns:
        # Find row indices where 'entry' is found in the column
        indices = [index for index, value in enumerate(df[column]) if value == entry]
        if indices:
            results[column] = indices

    max_len = max(len(indices) for indices in results.values())

    # Create a dictionary with column names as keys and lists of indices as values,
    # where the lists are padded with None values to have the same length
    padded_results = {col: idxs + [None] * (max_len - len(idxs)) for col, idxs in results.items()}

    return pd.DataFrame(padded_results)


def divide_table_by_coldata(data, colname, groups, name='G'):
    """
    Divide a DataFrame into multiple tables based on a list of groups.

    Args:
    - data (pd.DataFrame): The DataFrame to divide.
    - colname (str): The column to use for grouping.
    - groups (list of lists): A list of lists, where each inner list contains values of a group.

    Returns:
    - A dictionary of DataFrames, where keys are group names and values are corresponding DataFrames.
    """
    divided_tables = {}

    for i, group_values in enumerate(groups):
        group_name = f'{name}{i + 1}'
        group_table = data[data[colname].isin(group_values)].copy()
        group_table.reset_index(drop=True, inplace=True)
        divided_tables[group_name] = group_table

    return divided_tables