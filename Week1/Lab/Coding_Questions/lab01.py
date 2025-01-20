# Sample Coding Questions 01 Week 01

# Meric Yassine

# Array declaration
numbers = [1, 4, 7, 9]

# Variable declaration
a = 1
b = 2
c = 3
d = 4

# Arithmatic operation
# e = a - b ** c // d + a % c
# Fully bracketed version of the arithmatic operation
e = ((a - ((b ** c) // d)) + (a % c))

temperature = 32.6

st = "The temperature today is: {:.3f} degrees Celsius"
print(st.format(temperature))

# User input
userAge = input("What is your age?")
userAge = int(userAge) + 22
output = "Now showing the shop items filtered by age: {}"
print(output.format(userAge))


