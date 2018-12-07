file1 = open('input.txt', 'r')
file1_lines = file1.readlines()
file1.close()

file2 = open('input.txt', 'r')
file2_lines = file2.readlines()
file2.close()

for line1 in file1_lines:
    line1 = line1.replace('\n', '')
    for line2 in file2_lines:
        line2 = line2.replace('\n', '')

        line_differences = 0
        common_chars = ""
        for x in range(len(line1)):
            if line1[x] != line2[x]:
                line_differences += 1
            else:
                common_chars += line1[x]

        if line_differences == 1:
            print(line1)
            print(line2)
            print(common_chars)
            exit(0)

