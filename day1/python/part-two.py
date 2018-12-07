answer = 0
repeatingAnswer = 0
previousAnswers = [0]
inputLoop = 0

while True:
    inputLoop += 1
    file = open('../input.txt', 'r')
    for line in file:
        operator = line[0]
        currentValue = int(line[1:])
        if operator == '+':
            answer += currentValue
        else:
            answer -= currentValue

        if answer in previousAnswers:
            print(f'Repeating value found = {repeatingAnswer}')
            exit(0)
        previousAnswers.append(answer)

    print(inputLoop)


