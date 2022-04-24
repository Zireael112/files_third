catalog = ['1.txt', '2.txt', '3.txt']
text = []
dict = {}
flag = True

for log in catalog:
    calc = 0
    with open(log, encoding='utf-8') as file:
        tmp = []
        for i in file.read().split('\n'):
            tmp.append(i)
            calc += 1
        dict[log] = calc
        print(dict)
        text.append(tmp)
    text.sort(reverse=True)

with open('result.txt', mode='w', encoding='utf-8') as r_file:
    for i in text:
        for val, num in list(dict.items()):
            if len(i) == num:
                r_file.write(f'{val}\n')
                r_file.write(f'{num}\n')
                for j in i:
                    r_file.write(f'{j}\n')