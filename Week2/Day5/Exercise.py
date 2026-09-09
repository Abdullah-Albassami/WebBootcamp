# =========================================================
# EXERCISE — GUIDED PRACTICE
# =========================================================

# Ask the user for a maximum number.
# Loop from 1 through that number.
# Identify each value as even or odd.
# Count the even values.
# Accumulate the even values into a total.
# Display the count and final total.

even_count = 0
even_total = 0
max = int(input("Enter a maximum number: "))

for number in range(1, max + 1):
    if number % 2 == 0:
        print(f"{number} is even")
        even_count += 1
        even_total += number
    else:
        print(f"{number} is odd")

print(f"Total even numbers: {even_count}")
print(f"Sum of even numbers: {even_total}")