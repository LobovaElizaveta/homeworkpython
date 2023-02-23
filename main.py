song = input("Напишите песню: ")
volwes = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
parts = song.split()
result = list()
for item in parts:
    syllable = 0
    for letter in item:
        if letter in volwes:
            syllable += 1
    result.append(syllable)
if len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
