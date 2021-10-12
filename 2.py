with open('test2.txt') as file:
    file_lines = file.readlines()
    for  num, line in enumerate(file_lines):
        count = len(line.split())
        print(f'{num+1} - {count} words')
