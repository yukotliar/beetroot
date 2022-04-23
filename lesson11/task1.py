# Створіть новий файл numbers.txt у текстовому редакторі і запишіть у нього 10 чисел, кожне з нового рядка.
# Напишіть програму, яка зчитує ці числа з файла і обчислює їх суму, виводить цю суму на екран і, водночас,
# записує цю суму у інший файл з назвою sum_numbers.txt.
with open('numbers.txt') as numbers:
    sum = 0
    for number in numbers:
        try:
            sum += int(number)
        except:
            pass
f = open('sum_result.txt', 'w')
f.write(str(sum))
f.close()
