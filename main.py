f = open("three_digit_numbers.txt", "r")
sample = f.read()
num_list = sample.split()
num_list2 = []
for col in num_list:
    num = int(col)
    num_list2.append(num)
for count in range(300, 501):
    if count not in num_list2:
        a = (f"{count} is missing\n")
        print(a)
        file_write = open("sortedNumbers", "a")
        file_write.write(a)
        file_write.close()
