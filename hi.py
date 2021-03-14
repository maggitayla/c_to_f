#1.git add 檔名 
#eg.git add 123.py
#2.git commit -m "message"
#eg.git commit -m "my file name is 123.py"
#3.git push origin main

c = input('請輸入攝氏溫度: ')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為: ', f)