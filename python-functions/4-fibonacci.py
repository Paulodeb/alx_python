def fibonacci_sequence(n):
    if n <= 0:
        return []  # Return an empty list for invalid input

    # Initialize the Fibonacci sequence with the first two numbers.
    sequence = [0, 1]

    # Generate the remaining Fibonacci numbers.
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))