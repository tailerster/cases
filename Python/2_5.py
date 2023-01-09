import random
f = open('Task_5_data.txt', encoding = 'UTF8')
data = f.read()
data = data.replace("\"<tr>\\n\",", "[")
data = data.replace("\"</tr>\\n\"", "]")
data = data.replace("<td>", "")
data = data.replace("</td>\\n", "")
data = data.replace("    ", "")
data = "[" + data + "]"
table = eval(data)

def random_elem(table, col):
    row_len = len(table[0])
    i = random.randint(0, len(table[0])-1)
    return table[i][col]

def random_line(table):
    line = []
    for col in range(0, len(table[0])):
        line.append(random_elem(table, col))
    return " ".join(line)

#def task_5():
    

#print(table)
for i in range(10):
    print(random_line(table))
