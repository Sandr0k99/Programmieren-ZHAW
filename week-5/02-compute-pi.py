import math

def estimate_pi():
    sum_value = 0
    n = 0
    term = 1

    while term > 1e-15:  # Continue until the term is less than 1e-15
        # Calculate the term based on the provided formula
        numerator = math.factorial(4 * n) * (1103 + 26390 * n)
        denominator = ((math.factorial(n)) ** 4) * (396 ** (4 * n))
        term = numerator / denominator

        sum_value += term
        n += 1

    # Calculate the final estimate of π
    pi_estimate = ((2 * math.sqrt(2)) / 9801) * sum_value

    return pi_estimate


estimated_pi = estimate_pi()
print(f"Estimated value of π: {1/estimated_pi}")
print(f"Value of math.pi: {math.pi}")
