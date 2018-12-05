file = open('../input.txt', 'r')
answer = 0

for line in file:
    operator = line[0]
    currentValue = int(line[1:])
    previousAnswer = answer
    if operator == '+':
        answer += currentValue
    else:
        answer -= currentValue
    print(f'{previousAnswer} {operator} {currentValue} = {answer}')

