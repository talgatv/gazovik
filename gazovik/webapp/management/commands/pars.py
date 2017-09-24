'''

'''
import requests
from grab import Grab
import time
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from gazovik.webapp.models import *
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Migrate'


    print ('**************NACHALO******************')
#тут начинается цикл команды manage.py
    def handle(self, *args, **options):
#позже изменю на не постоянную
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
#
# #объект old_users переделывает в список из таблицы UserGroup с фильтром только group_id=2
#         old_users = UserGroup.objects.filter(group_id=group.id,out_time=None).values_list('vk_id', flat=True)
#         print(group.vk_groip_id)
# # начинается цикл обращения к вк
#         while offset < count:
#             r = requests.get('https://api.vk.com/method/groups.getMembers',
#             params={'group_id': group.vk_groip_id, 'offset':offset}).json()
# # парсер json ответа
#             response = r['response']
#             count = response['count']
# # цикл который обрабатывет json ответ с параметром users
#             for user in response['users']:
#
# # говориткакие столбцы таблицы UserGroup заполнять
#                 vk_users = UserGroup(
#                     vk_id = user,
#                     group = group,
#                     name = 'user' #по умолчанию в поле name параметр user
#
#                 )
#
# # сохраняет всё столбцы в таблицу и если выдаёт ошибку "IntegrityError" что означает что запись уже есть в таблице, то пичатает рядом скип и невносит в таблицу
#                 try:
#                     vk_users.save()
#                     print (vk_users.vk_id)
#                     new_users.append(vk_users.vk_id)
#                 except IntegrityError:
#                     print(str(vk_users.vk_id) +' -skip')
#                     a.append(vk_users.vk_id)
#                 else:
#                     print(str(vk_users.vk_id) +' -out_time')
#                     # vk_users.filter(group_id=group.id,out_time=None).out_time='2017-09-06 16:04:00.732845'
#                     # vk_users.save()
#
#
#
#
# # Что такое offset ????????????
#             offset = offset + 1000
#             print(offset)
#             time.sleep(0.37)
#         print('first done')
#
# #объект new_users переделывает в список из таблицы UserGroup с фильтром только group_id=2 ,
#         new_users = UserGroup.objects.filter(group_id=group.id).values_list('vk_id', flat=True)
#         print('new_users ',len(new_users))
#         print('как было, old_users ',len(old_users))
#         print('на данный момент, a ',len(a))
#
#
#         A = set(a)
#         B = set(old_users)
#
#         vishli = list(A - B)
#         vstupili = list(B - A)
#         print('Вышло пользователей:',len(vishli) )
#         print('Вступило пользователей:',len(vstupili) )
#         # print(vstupili)
#
#
#         # old_users = a





# выводит что все нормально
        self.stdout.write(self.style.SUCCESS('Successfully ' ))


#
# if __name__ == '__main__':
#     categories()
