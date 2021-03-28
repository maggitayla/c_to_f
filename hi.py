#1.git add 檔名 
#eg.git add 123.py
#2.git commit -m "message"
#eg.git commit -m "my file name is 123.py"
#3.git push origin main

# c = input('請輸入攝氏溫度: ')
# c = float(c)
# f = c * 9 / 5 + 32
# print('華氏溫度為: ', f)

# h = int(input('anwser your height: '))
# w = int(input('anwser your weight: '))
# bmi = w / h**2
# if bmi < 18.5:
#     print('過輕')
# elif bmi >= 18.5 and bmi <24:
#     print('正常')
# elif bmi >= 24 and bmi < 27:
#     print('過重')
# elif bmi >= 27 and bmi < 30:
#     print('輕度肥')
# elif bmi >= 30 and bmi < 35:
#     print('中度肥')
# else:
#     print('重度肥')

# driving = input('請問是否開過車?(Y/N) ')
# age = int(input('輸入年齡'))
# if driving == 'Y':
#     if age >= 18:
#         print('pass')
#     else:
#         print('that is weird!')
# else:
#     print('ok,bye~')

# x = 3
# while x < 10:
#     print('keep going')
#     x = x + 2
# print("it's done")

# while True: #無限迴圈
#     mode = input('輸入模式')
#     if mode == 'q': #quit
#         break
#     elif mode == '1':
#         print('啟動模式一')
#     elif mode == '2':
#         print('啟動模式二')
#     else:
#         print('只能輸入q/1/2')

# password = 'a123456'
# times = 3
# while times > 0:
#     ans_pwd = input('輸入密碼:')
#     if ans_pwd == password:
#         print('ok')
#         break
#     else:
#         times = times - 1
#         if times == 0:
#             print('your account is blocked')
#         else:
#             print('chance left: ', times)
#         # if times == 0:
#         #     print('your account is blocked')
#         #     break

# import random
# r = random.randint(1,100)
# t = 0
# while True:
#     t += 1
#     guess = int(input('猜數字'))
#     if t > 10:
#         print('猜超過10次了QQ byebye')
#         break
#     else: 
#         if guess == r:
#             print('答對了~~ 共猜了', t, '次')
#             break
#         elif guess > r:
#             print('太大了')
#         else:
#             print('太小了')

# a = ['toyota', 'honda']
# a.append('audi')
# # print(a)
# # print(a[1])
# # print('toyota' in a)
# b = 0
# for car in a:
#     b += 1
#     print(b,'.', car)

# students = ['Allen', 'Tom', 'Mayday', \
#     'JJ', 'Jolin', 'Jay', 'Jam']
# for student in students:
#     print('Hi', student)

# data = []
# with open('food.txt', 'r') as f:
#     for line in f:
#         data.append(line.strip()) #strip對字串去除空白
# print(data)

# data = []
# with open('reviews.txt', 'r') as f:
#     for line in f:
#         data.append(line)

# sum_len = 0

# for d in data:
#     sum_len = len(d) + sum_len
# print(sum_len / len(data))
# # print(len(data))
# # print(data[0])

# new=[]
# for d in line:
#     if len(d) < 100:
#         new.append(d)
# print(len(new))

# # good = []
# # for d in data:
# #     if 'good' in d:
# #         good.append(d)

# good = [d for d in data if 'good' in d]

# print(len(good))

#range的使用方式，藉由range的數字做為重複顯示的數量

# import random

# a = range(5)
# for i in a:
#     r = random.randint(1,100)
#     print(r)
# b = range(50, 10, -21)
# for j in b:
#     print(j)

products = []
while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入價格')
    p = [name, price]
    # p.append(name)
    # p.append(price)
    products.append(p)
print(products[0])

for p in products:
    print(p[0], '價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
