#name = input('Как звали президента России, который был у власти, когда вы родились? ')
#other_name = input('Как зовут нынешнего президента России? ')
#name == other_name

#if(name == other_name):
    #print('Вы неудачник, ха-ха')
#else:
#print('Супер!')


#name = input('Введите число: ')
#x = int(name)
#print(x*2)

#number = input('Введите число: ')
#a = int(number)
#b = a + 1
#c = a - 1
#print('За числом ', number, ' следует число ', b)
#print('Перед числом ', number, ' следует число ', c)


print('С помощью магии я превращу любое написанное вами число в 4!')
a = input('Напишите число: ')
b = float(a)
c = b * 2
print('Число ', b,' умножить на 2 равно ', c)
d = c + 8
print('Число ', c, ' плюс 8 равно ', d)
e = d / 2
print('Число ', d, ' делить на 2 равно ', e)
f = e - b
print('Число ', e, ' минус ', b, ' равно ', f)
print('Hello world bla bla bla')

# из двух вводов делаем словарь
list_rus = input().split()
list_eng = input().split()
i = 0
dictionary = {}
while len(list_rus) == len(list_eng):
    dictionary[list_rus[i]] = list_eng[i]
    i += 1
    if i >= len(list_rus):
        print(dictionary)
        break
