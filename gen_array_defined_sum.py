"""Functions to generate mocked arrays for demo purposes"""
import numpy as np

def gen_array_defined_sum(quantity: int, total: int):
    """Generate int list of size quantity with sum total"""
    normalized_values = np.random.dirichlet(np.ones(quantity), size=1)[0]
    floor_values = np.floor(normalized_values * total).astype(int)

    floor_sum = np.sum(floor_values)

    if floor_sum < total:
        floor_values[0] += (total - floor_sum)

    return floor_values

def __main__():
    total = 13089
    quantity = 12

    generated_values = gen_array_defined_sum(quantity, total)

    print("Generated Values", generated_values)

    print("Sum of generated values: ", np.sum(generated_values))

if __name__ == "__main__":
    __main__()
