def arithmetic_arranger(op, *e):
    li = []
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    out = ""

    for i in range(len(op)) :
        op[i] = op[i].split()

        if len(op) > 5:
            return('Error: Too many problems.')

        try:
            li.append(int(op[i][0]))
        except:
            return('Error: Numbers must only contain digits.')

        if op[i][1] == '+' or op[i][1] == '-':
            li.append(op[i][1])
        else:
            return("Error: Operator must be '+' or '-'.")

        try:
            li.append(int(op[i][2]))
        except:
            return('Error: Numbers must only contain digits.')

        if len(op[i][0]) > 4 or len(op[i][2]) > 4 :
            return('Error: Numbers cannot be more than four digits.')


    for i in range(len(op)):
        size = max(len(op[i][0]),len(op[i][2])) + 2
        plus = int(op[i][0]) + int(op[i][2])
        sub = int(op[i][0]) - int(op[i][2])
        sign = op[i][1]

        line1 += op[i][0].rjust(size) + "    "
        line2 += op[i][1] + op[i][2].rjust(size-1) + "    "
        bars = ""
        for j in range(size) :
            bars += '-'
        line3 += bars + "    "
        if sign == '+':
            line4 += str(plus).rjust(size) + "    "
        else:
            line4 += str(sub).rjust(size) + "    "

    out = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    for k in e:
        if k is True:
            out += "\n" + line4.rstrip()
            break
    return out
