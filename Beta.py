odd_numbers = [num for num in range(1, 21) if num % 2 != 0]
print(odd_numbers)

sum_of_evens = sum(num for num in range(1, 21) if num % 2 == 0)
print(sum_of_evens)

def get_sum_of_evens(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)

start = int(input("Enter start: "))
end = int(input("Enter end: "))
print(f"Sum of even numbers from {start} to {end}: {get_sum_of_evens(start, end)}")

