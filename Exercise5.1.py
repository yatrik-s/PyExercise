# Exercise 5.1
# Calculate total and average of numbers using list
#

num_list = list()

while True:
    input = raw_input('Enter a number: ')
    if input == 'done':
        break
    else:
        try:
            num = int(input)
        except:
            print "Invalid input"
            continue
    num_list.append(num)

if len(num_list) != 0:
    print "Sum: ", sum(num_list), "Count: ", len(num_list), \
          "Average: ", sum(num_list)/len(num_list)
