# Data collection
user_inputs = []
count = 10

for i in range(0, 10):
    while True:
        try:
            user_input = int(input("Enter a number then press the 'Enter' button."))
            user_inputs.append(user_input)
            count -= 1
            break
        except:
            print("The value you have entered is not a number. Please enter a number.")

    print("The value you have entered is:", user_input)

    print("Please repeat this step", count, "more times.")

print("You have entered the following set of numbers:", user_inputs)

# Find the minimum
min_value = user_inputs[0]

for i in user_inputs:
    if i < min_value:
        min_value = i

# Find the maximum
max_value = user_inputs[0]

for i in user_inputs:
    if i > max_value:
        max_value = i

# Find the range
range_value = max_value - min_value

# Find the mean
input_sum = sum(user_inputs)
input_total = len(user_inputs)
input_avg = input_sum // input_total

# Find the variance
input_diff = 0

for i in range(input_total):
    input_diff= input_diff + (user_inputs[i] - input_avg)**2

input_variance = input_diff / input_total

# Find the standard deviation
input_sd = input_variance ** 0.5

# Display the results
print("Results - ")
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Range:", range_value)
print("Mean:", input_avg)
print("Variance:", input_variance)
print("Standard Deviation:", input_sd)