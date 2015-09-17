# Exercise 5.1
not_done = True
count = 0
sum = 0

while not_done:
    input = raw_input("Enter a number:")
    if input == "done":
        break
    try:
        num = int(input)
    except:
        print "Invalid input"
        continue
    count = count + 1
    sum = sum + num

if count > 0:
    print "Sum: ", sum, "Count: ", count, "Average: ", sum/count

