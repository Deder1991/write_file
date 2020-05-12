import os	#載入作業系統
products = []
count = 2

if os.path.isfile('products.csv'):	#詢問有沒有此檔案
	print('有此檔案')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品名稱,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('無此檔案')
	
#輸入物品和價格
while count > 0:
	name = input('請輸入物品名稱:')
	price = input('請輸入物品價格:')
	price = int(price)
	products.append([name, price])
	#也可以寫成
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	count -=1
print(products)

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品名稱,價格\n')
	for line in products:
		f.write(line[0] + ',' + str(line[1]) + '\n')


