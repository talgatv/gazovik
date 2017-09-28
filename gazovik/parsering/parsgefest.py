from grab import Grab
from lxml.html import fromstring
g = Grab()

with open('gaz_plit_productURL2.txt') as f:
	urlFile = f.readlines()
	f.close

f = open('oboi_product_with_price.txt', 'w')

for i in range(0, len(urlFile),1):
	g.go(urlFile[i].rstrip('\n'))

	ProductParse = str(urlFile[i].rstrip('\n'))

	Name = g.doc.select('//h2[@class="item-title tov_name"]')[0].text()
	Artikul = g.doc.select('//ul[@class="item-description-short"]/span')[0].text()
	Description = str(g.doc.select('//ul[@class="list-1"]')[1].html() )
	Price = 'Null'
	#print(Price)

	#get main image
	ImageMainFull = 'https://www.gefest.com' + g.doc.select('//div[@class="slide"]/a[@class="image-big fancybox"]/@href')[0].text()
	ImageBig = 'https://www.gefest.com' + g.doc.select('//div[@class="slide"]/a/img/@src')[0].text()

	#++++++++++++++++++++++++++
	#++++++++++++++++++++++++++

	ProductParse = ProductParse + '|' + Name + '|' + Artikul + '|' + Price + '|' + Description + '|' + ImageMainFull + '|' + ImageBig
	#ProductParse2 = '|' + Name

	#print(ProductParse2)

	f.write(ProductParse + '\n' )
	print('Number i = ' + str(i) + ': ' + str(urlFile[i].rstrip('\n')))




f.close()
