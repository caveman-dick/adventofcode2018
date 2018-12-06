answer = 0
previousAnswer = 0
previousAnswers = {}
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

        print(f'{previousAnswer} {operator} {currentValue} = {answer}')

        if answer in previousAnswers:
            print(f'Repeating value found = {answer}')
            exit(0)
        previousAnswer = answer
        previousAnswers[answer] = answer

    print(inputLoop)


