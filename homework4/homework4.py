# 3. List
# 3.1 List Operations

favorite_food = ["pizza","sushi", "burger", "steak", "ramen"]

print(favorite_food[1])

print(favorite_food[-1])

favorite_food.append("icecream")

favorite_food.insert(0, "apple")

del favorite_food[2]

print(len(favorite_food))

for food in favorite_food:
	print(food.upper())

new_list = favorite_food[:1] + favorite_food[-1:]

if "potato" in favorite_food:
	print("A potato!")
else:
	print("No potato!")

# 3.2 Slicing and Striding

numbers = list(range(21))

def get_first_15(numbers):
	return numbers[:15]

def get_every_5th(lst):
	return lst[::5]

def reverse_and_stride(lst):
	reversed_lst =  lst[::-1]
	return reversed_lst[::-3]

# 3.3 Nested Lists

numbers = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# 3.3.1 Nested List Operations

print(numbers[2])

print(numbers[1][1])

numbers.append([10, 11, 12])

def sum_nested(all_numbers):
	total = 0
	for row in all_numbers:
		for number in row:
			total += number
	return total

print(sum_nested(numbers))

# 3.4 Create a 5x5 List

def make_grid():
	grid = []
	number = 1

	for row_index in range(1,6):
		row = []

		for column_index in range(1,6):
			row.append(number)
			number += 1

		grid.append(row)

	return grid

def replace_multiples(grid):
	for row_index in range(len(grid)):
		for column_index in range(len(grid[row_index])):
			if grid[row_index][column_index] % 3 == 0:
				grid[row_index][column_index] = "?"

	return grid

def sum_remaining(grid):
	total = 0

	for row in grid:
		for number in row:
			if number != "?":
				total += number

	return total


# 4.1 Dictionary Operations

ages = {
	"Katie": 30,
	"Mariam": 42,
	"Safia": 25,
	"Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

del ages["Mariam"]

for name, age in ages.items():
	print(name, age)


print("My favorite function:")

for row in make_grid():
		print(row)
