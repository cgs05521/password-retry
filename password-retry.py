test = 3
test = int(test)
password = 'a123456'

while test > 0 :
	test = test-1
	name = input('請輸入密碼： ')
	if name == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if test > 0:
			print('還有',test,'機會')
		else:
			print('沒機會嘗試了')