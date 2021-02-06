# Data collection
user_inputs = [] # create an empty list
count = 10

for i in range(0, 10):
    while True:
        try:
            # prompt users to enter an integer
            user_input = int(input("Enter a number then press the 'Enter' button."))
            # retain the correct values to the list
            user_inputs.append(user_input)
            count -= 1
            break
        except:
            # error message displays when user enters an non-integer value
            print("The value you have entered is not a number. Please enter a number.")

    # displays the value entered
    print("The value you have entered is:", user_input)
    # alerts users how many more values they need to enter
    print("Please repeat this step", count, "more times.")

# displays final list of values
print("You have entered the following set of numbers:", user_inputs)

# Find the minimum
# assume the first value in the list is the minimum value
min_value = user_inputs[0]

# iterate through the list
for i in user_inputs:
    # if a value is lower than the first value
    if i < min_value:
        # set the value as the minimum
        min_value = i

# Find the maximum
# assume the first value in the list is the maximum value
max_value = user_inputs[0]

# iterate through the list
for i in user_inputs:
    # if a value is higher than the first value
    if i > max_value:
        # set the value as the maximum
        max_value = i

# Find the range
# subtract minimum value from maximum value
range_value = max_value - min_value

# Find the mean
# assign input_sum as the sum of all integers in list
input_sum = sum(user_inputs)
# assign input_total as the count of all integers in list
input_total = len(user_inputs)
# assign input_avg as the sum of all integers divided by the count of all integers
input_avg = input_sum // input_total

# Find the variance
input_diff = 0

# find values in list that can be iterated
for i in range(input_total):
    # iterate through the list and find difference of the integer and mean, then square each value.
    # assign input_diff as the sum of all squared difference
    input_diff= input_diff + (user_inputs[i] - input_avg)**2

# divide the input_diff by the count of values in list
input_variance = input_diff / input_total

# Find the standard deviation
# square the variance by .05
input_sd = input_variance ** 0.5

# Display the results
print("Results - ")
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Range:", range_value)
print("Mean:", input_avg)
print("Variance:", input_variance)
print("Standard Deviation:", input_sd)