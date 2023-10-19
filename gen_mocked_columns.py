"""Functions to generate mocked pandas columns for demo purposes"""
import pandas as pd

from gen_array_defined_sum import gen_array_defined_sum

def gen_int_series_with_defined_sum(col_names: list[str], total: int):
    """Generate series based on their names and a total sum"""
    quantity = len(col_names)
    generated_values = gen_array_defined_sum(quantity, total)
    values_dict = dict(zip(col_names, generated_values))
    return pd.Series(values_dict)

def __main__():
    col_names = ["col1", "col2", "col3", "col4", "col5"]
    total = 100
    generated_values = gen_int_series_with_defined_sum(col_names, total)
    print("Generated Values", generated_values)

if __name__ == "__main__":
    __main__()
