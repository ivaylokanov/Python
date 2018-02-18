with open('./Resources/02. Line Numbers/Input.txt', 'r') as current_file:
    temp_list = current_file.read().split('\n')
    output_file = [f'{index+1}. {item}' for index, item in enumerate(temp_list)]
    open('./Resources/02. Line Numbers/Output.txt', 'w').write('\n'.join(output_file[:-1]))
