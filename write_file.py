products = []
while True:
	food = input('請輸入食物名稱:')
	if food == 'q':
		break
	price = input('請輸入價格:')
	products.append([food, price])
print(products)
