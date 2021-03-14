#1.git add 檔名 
#eg.git add 123.py
#2.git commit -m "message"
#eg.git commit -m "my file name is 123.py"
#3.git push origin main

# c = input('請輸入攝氏溫度: ')
# c = float(c)
# f = c * 9 / 5 + 32
# print('華氏溫度為: ', f)

h = int(input('anwser your height: '))
w = int(input('anwser your weight: '))
bmi = w / h**2
if bmi < 18.5:
    print('過輕')
elif bmi >= 18.5 and bmi <24:
    print('正常')
elif bmi >= 24 and bmi < 27:
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥')
elif bmi >= 30 and bmi < 35:
    print('中度肥')
else:
    print('重度肥')