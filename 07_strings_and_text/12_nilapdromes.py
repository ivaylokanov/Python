while True:
    line = str(input())
    state = ''
    if line == 'end':
        break
    for i in range(1, len(line)//2+1):
        if line[0:i] == line[len(line)-i:len(line)]:
            state = line[0:i]
    line = line[len(state):-len(state)]
    if line != '' and state !='':
        print(f'{line}{state}{line}')
