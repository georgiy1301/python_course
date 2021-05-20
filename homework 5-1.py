with open('myfile.txt', 'w', encoding='utf-8') as f:
   while True:
       line = input('Введите строку - ')
       if not line:
           break
print('End')
