# Data collection
user_inputs = [] # create an empty list
count = 10

for i in range(0, 10):
    while True:
        try:
            user_input = int(input("Enter a number then press the 'Enter' button.")) # prompt users to enter an integer
            user_inputs.append(user_input) # retain the correct values to the list
            count -= 1
            break
        except:
            print("The value you have entered is not a number. Please enter a number.") # error message displays when user enters an non-integer value

    print("The value you have entered is:", user_input) # displays the value entered

    print("Please repeat this step", count, "more times.") # alerts users how many more values they need to enter

print("You have entered the following set of numbers:", user_inputs) # displays final list of values

# Find the minimum
min_value = user_inputs[0] # assume the first value in the list is the minimum value

for i in user_inputs: # iterate through the list
    if i < min_value: # if a value is lower than the first value
        min_value = i # set the value as the minimum

# Find the maximum
max_value = user_inputs[0] # assume the first value in the list is the maximum value

for i in user_inputs: # iterate through the list
    if i > max_value: # if a value is higher than the first value
        max_value = i # set the value as the maximum

# Find the range
range_value = max_value - min_value # subtract minimum value from maximum value

# Find the mean
input_sum = sum(user_inputs) # assign input_sum as the sum of all integers in list
input_total = len(user_inputs) # assign input_total as the count of all integers in list
input_avg = input_sum // input_total # assign input_avg as the sum of all integers divided by the count of all integers

# Find the variance
input_diff = 0

for i in range(input_total): # find values in list that can be iterated
    # iterate through the list and find difference of the integer and mean, then square each value.
    # assign input_diff as the sum of all squared difference
    input_diff= input_diff + (user_inputs[i] - input_avg)**2

input_variance = input_diff / input_total # divide the input_diff by the count of values in list

# Find the standard deviation
input_sd = input_variance ** 0.5 # square the variance by .05

# Display the results
print("Results - ")
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Range:", range_value)
print("Mean:", input_avg)
print("Variance:", input_variance)
print("Standard Deviation:", input_sd)