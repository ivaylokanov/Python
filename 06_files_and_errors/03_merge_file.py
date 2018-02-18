temp_list = []


def append_to_list(file_path):
    with open(file_path, 'r') as temp_file:
        [temp_list.append(item) for item in temp_file.read().split()]


append_to_list('./Resources/03. Merge Files/FileOne.txt')
append_to_list('./Resources/03. Merge Files/FileTwo.txt')
open('./Resources/03. Merge Files/Output.txt', 'w').write('\n'.join(sorted(temp_list)))
