while True:
    line = input()
    state = ''
    if line == 'end':
        break
    for i in range(1, len(line)//2+1):
        if line[0:i] == line[len(line)-i:len(line)]:
            state = line[0:i]
    line = line.replace(state,'')
    if line != '' and state !='':
        print(f'{line}{state}{line}')