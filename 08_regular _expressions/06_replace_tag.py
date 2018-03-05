import re

while True:
    text = input()
    if text == 'end':
        break
    replaced_text = text

    replaced_text = re.sub("<a[ ]?", "[URL ", replaced_text)
    replaced_text = re.sub("</a>", "[/URL]", replaced_text)
    replaced_text = re.sub("\">", "\"]", replaced_text)
    print(replaced_text)
