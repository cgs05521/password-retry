test = 3
test = int(test)
password = 'a123456'

while test > 0 :
	name = input('請輸入密碼： ')
	if name == password:
		print('登入成功')
	else:
		test = test-1
		if test == 0:
			break
		print('還有',test,'機會')



print('恭喜猜錯')