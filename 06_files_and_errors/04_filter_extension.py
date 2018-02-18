import os

extension = input()
for root, dirs, files in os.walk('./Resources/04. Filter-Extensions/input'):
    new_files = [file for file in files if
                 file.rpartition('.')[-1] == extension]
open('./Resources/04. Filter-Extensions/Output.txt', 'a').write("\n".join(new_files))
