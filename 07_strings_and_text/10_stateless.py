while True:
    state = input()
    if state == 'collapse':
        break
    fiction = input()
    while True:
        if len(fiction) == 0:
            break
        state = state.replace(fiction, '')
        if len(fiction) == 1:
            break
        else:
            fiction = fiction[1:len(fiction) - 1]
    if state == '':
        print("(void)")
    else:
        print(state.strip())
