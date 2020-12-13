input = 'aabcd#'
# inputLst = list(input)

m = {
    'a': '1',
    'b': '2',
    'c': '3',
    '#': '4',
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': '#'
}

def accept():
    print('accept')

def reject():
    print('reject')

def isAbc(word, index):
    current = word[index]
    if index == 0:
        if current != 'a':
            reject()
        else:
            index += 1
            isAbc(word, index)
    else:
        last = word[index - 1]
        if current == last or current == m[str(int(m[last]) + 1)]:
            if current == '#':
                accept()
            else:
                isAbc(word, index + 1)
        else:
            reject()

