import re

while True:
    text = input()
    result_dict = {}
    if text == 'END':
        break
    replaced_text = text
    replaced_text = re.sub("%20", " ", replaced_text)
    replaced_text = re.sub("\+", " ", replaced_text)
    replaced_text = re.sub("\s+", ' ', replaced_text)
    replaced_text = replaced_text + "&"
    regex = re.compile(r"(.*?)=(.*?)[&]")
    for match in regex.finditer(replaced_text):
        key = match.group(1).strip()
        if "?" in key:
            key = key[key.index("?") + 1:]
        value = match.group(2).strip()
        if key not in result_dict:
            result_dict[key] = []
            result_dict[key].append(value)
        else:
            result_dict[key].append(value)
    for key, value in result_dict.items():
        print(f"{key}=[", end='')
        print(*result_dict[key], sep=', ', end='')
        print("]", end='')
    print()
