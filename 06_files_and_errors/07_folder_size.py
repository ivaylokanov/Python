import os

for root, dirs, files in os.walk('./Resources/07. Folder Size/TestFolder'):
    total_sizes = [os.stat(root + '/' + file).st_size for file in files]
open('./Resources/07. Folder Size/TestFolder/Output.txt', 'w').write(f'Total size: {sum(total_sizes) / 1024 / 1024} MB')
