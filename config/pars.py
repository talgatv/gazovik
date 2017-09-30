# Получаю данные с плиты с файла  gaz_plit_productURL.txt
from grab import Grab
import sqlite3
import requests
conn = sqlite3.connect('gazovik.sqlite3')
g = Grab()

with open('gaz_plit_productURL2.txt') as f:
	urlFile = f.readlines()
	f.close

f = open('oboi_product_with_price.txt', 'w')

for i in range(0, len(urlFile),1):
	g.go(urlFile[i].rstrip('\n'))

	ProductParse = str(urlFile[i].rstrip('\n'))
	slug = result2 = ProductParse.lstrip('https://www.gefest.com/catalog/gazovye-plity/').lstrip('https://www.gefest.com/catalog/gazoelektricheskie-plity/').rstrip('/')
	Name = g.doc.select('//h2[@class="item-title tov_name"]')[0].text()
	Artikul = g.doc.select('//ul[@class="item-description-short"]/span')[0].text()
	Description = str(g.doc.select('//ul[@class="list-1"]')[1].html() )
	Price = 'Null'
	#print(Price)

	#get main image
	ImageNameFull = g.doc.select('//div[@class="slide"]/a[@class="image-big fancybox"]/@href')[0].text()
	ImageNameSlugFull2 = ImageNameFull[19:-4]
	ImageNameFull2 = ImageNameSlugFull2 + '.jpg'
	ImageMainFull = 'https://www.gefest.com' + ImageNameFull
	ImageNameBig = g.doc.select('//div[@class="slide"]/a/img/@src')[0].text()
	ImageNameBig2 = ImageNameBig.lstrip('/upload/imager/')
	ImageBig = 'https://www.gefest.com' + ImageNameBig
	BigimageDB = 'upload/images/' + ImageNameFull2
	MiniImageDB = 'upload/images/' + ImageNameBig2
	# urllib.urlretrieve(ImageMainFull, ImageNameFull2)
	# urllib.urlretrieve(ImageBig, ImageNameBig2)
	# r = requests.get(ImageMainFull)
	# with open(ImageNameFull2, "wb") as code:
    # 	code.write(r.content)


	# p = requests.get(ImageMainFull)
	# out = open(ImageNameFull2, "wb")
	# out.write(p.content)
	# out.close()
	#
	# p = requests.get(ImageBig)
	# out = open(ImageNameBig2, "wb")
	# out.write(p.content)
	# out.close()


	#++++++++++++++++++++++++++
	#++++++++++++++++++++++++++

	ProductParse = ProductParse + '|' + Name + '|' + Artikul + '|' + Price + '|' + Description + '|' + ImageMainFull + '|' + ImageBig
	#ProductParse2 = '|' + Name

	#print(ProductParse2)  (slug,name,description,price,data,category_id,image_mini,image)
	# cursor = conn.cursor()

	# conn.execute("INSERT INTO webapp_tovar VALUES (ImageNameSlugFull2 , Name,Description,Price,'2017-09-28 18:10:06','1',MiniImageDB,BigimageDB)" )
	# cursor.execute("INSERT OR IGNORE INTO webapp_tovar (slug,name,description,price,data,category_id,image_mini,image) VALUES (? ? ? ? ? ? ? ?)", (ImageNameSlugFull2 , Name,Description,Price,'2017-09-28 18:10:06','1',MiniImageDB,BigimageDB))
	conn.execute("INSERT INTO webapp_tovar (slug, name, description, price, data, category_id, image_mini, image) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (slug, Name, Description, Price, '2017-09-28 18:10:06', '1', MiniImageDB, BigimageDB))
	f.write(ProductParse + '\n' )
	print('Number i = ' + str(i) + ': ' + str(urlFile[i].rstrip('\n')))




f.close()
conn.commit()
print ("Records created successfully")
conn.close()
