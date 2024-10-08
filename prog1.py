import random

def simple_rng(min_value=1, max_value=100):
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

# Generate a random number without user input
random_number = simple_rng()
print(f"Random number between 1 and 100: {random_number}")

