import re

def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first = ''
    second = ''
    lines = ''
    sumx = ''
    string = ''
    for problem in problems:
        if re.search('[^\s0-9.+-]', problem):
            if re.search('[/]', problem) or re.search('[*]', problem):
                return "Error: Operator must be '+' or '-'"
            return 'Error: Numbers must only contain 5 digits'

        first_num = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        second_num = problem.split(' ')[2]

        if len(first_num) >= 5 or len(second_num) >= 5:
            return 'Error: Numbers cannot be more than four digits.'

        sum = ''
        if operator == '+':
            sum = str(int(first_num) + int(second_num))
        if operator == '-':
            sum = str(int(first_num) - int(second_num))

        length = max(len(first_num), len(second_num)) + 2
        top = str(first_num).rjust(length)
        bottom = operator + str(second_num).rjust(length - 1)
        line = ''
        res = str(sum).rjust(length)
        for x in range(length):
            line += '-'

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if solve:
        string = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        string = first + "\n" + second + '\n' + lines
    return string
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))