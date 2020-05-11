products = []
while True:
	food = input('請輸入食物名稱:')
	if food == 'q':
		break
	price = input('請輸入價格:')
	p = []
	p.append(food)
	p.append(price)
	products.append(p)
print(products)
