from random import randint

def random_char():
    return chr(randint(ord('0'), ord('9')))

def random_string(max_len=10):
    line = ''
    for i in range(randint(1, max_len)):
        line += random_char()
    return line

def random_list(max_len=10):
    lst = []
    for i in range(randint(1, max_len)):
        lst.append(random_string())
    return lst

def task_1_1(lst):
    return [int(elem) for elem in lst]

lst = random_list()

def test_task_1():
    for i in range(10):
        lst = random_list()
        new_lst = task_1(lst)
        assert lst == list(task_1_1(lst))

#print(lst)
#print(task_1_1(lst))

def task_1_2(lst):
    return len(set(lst))

#print(lst)
#print(task_1_2(lst))

def task_1_3(lst):
    rev_lst = []
    lst = lst.copy()
    while len(lst) != 0:
        rev_lst.append(lst.pop())
    return rev_lst
    
def test_task_1_3():
    for i in range(10):
        lst = random_list()
        new_lst = task_3(lst)
        print(lst, new_lst)
        lst.reverse()
        assert new_lst == new_lst
        
#test_task_1_3()
#print(lst)
#print(task_1_3(lst))

def task_1_4(lst, x): 
	indexes = []
	for i in range(len(lst)): 
		if lst[i] == X:
			indexes.append(1)
	return indexes

def task_1_4_2 (lst, x):
	return [i for i in range(len(lst)) if lst[i] == x]


def task_1_6(t):
    max_line = ' '
    for line in t:
        if len(line) > len(max_line):
            max_line = line
    return max_line

test = ['a', 'adsd', 'sdasd', 's']

def test_task_1_6():
    print(task_1_6(test))

def test_task_1_6_2(t):
    return max (t, key=len)
