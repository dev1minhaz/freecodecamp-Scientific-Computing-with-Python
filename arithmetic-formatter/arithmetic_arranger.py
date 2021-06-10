def arithmetic_arranger(p, a=False):
    
    if len(p) > 5:
        return "Error: Too many problems."
    
    operand1 = []
    opernad2 = []
    operator = []

    for i in p:
        pieces = i.split()
        operand1.append(pieces[0])
        operator.append(pieces[1])
        opernad2.append(pieces[2])

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    for i in range(len(operand1)):
        if not (operand1[i].isdigit() and opernad2[i].isdigit()):
            return "Error: Numbers must only contain digits."

    for i in range(len(operand1)):
        if len(operand1[i]) > 4 or len(opernad2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in range(len(operand1)):
        if len(operand1[i]) > len(opernad2[i]):
            line1.append(" "*2 + operand1[i])
        else:
            line1.append(" "*(len(opernad2[i]) - len(operand1[i]) + 2) + operand1[i])

    for i in range(len(opernad2)):
        if len(opernad2[i]) > len(operand1[i]):
            line2.append(operator[i] + " " + opernad2[i])
        else:
            line2.append(operator[i] + " "*(len(operand1[i]) - len(opernad2[i]) + 1) + opernad2[i])

    for i in range(len(operand1)):
        line3.append("-"*(max(len(operand1[i]), len(opernad2[i])) + 2))

    if a:
        for i in range(len(operand1)):
            if operator[i] == "+":
                ans = str(int(operand1[i]) + int(opernad2[i]))
            else:
                ans = str(int(operand1[i]) - int(opernad2[i]))

            if len(ans) > max(len(operand1[i]), len(opernad2[i])):
                line4.append(" " + ans)
            else:
                line4.append(" "*(max(len(operand1[i]), len(opernad2[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
    else:
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    return arranged_problems
