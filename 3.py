with open('test3.txt') as file:
    file_lines = file.readlines()
    data = {}
    sum=0
    for line in file_lines:
        words = line.split()
        data.update({words[0]: float(words[1])})
        sum+=float(words[1])
    for keys, values in data.items():
        if values < 20000:
            print(f'{keys}')
    srednee = sum / len(data)
    print(srednee)


