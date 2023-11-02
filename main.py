f = open("three_digit_numbers.txt", "r")
sample = f.read()
num_list = sample.split()
num_list2 = []
for col in num_list:
    num = int(col)
    num_list2.append(num)
start = min(num_list2)
for count in range(start, max(num_list2)):
    if count not in num_list2:
        print (f"{count} is missing")