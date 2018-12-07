file = open('input.txt', 'r')
answer = 0

twoLetterCount = 0
threeLetterCount = 0

for line in file:
    twoLetter = False
    threeLetter = False

    for letter in line:
        letterCount = line.count(letter)
        if letterCount == 2:
            twoLetter = True

        if letterCount == 3:
            threeLetter = True

        if twoLetter & threeLetter:
            break

    if twoLetter:
        twoLetterCount += 1
    if threeLetter:
        threeLetterCount += 1


print(f'Checksum = {twoLetterCount * threeLetterCount}')

