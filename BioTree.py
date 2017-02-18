#-*- coding: utf-8 -*-

class Taxon:
  name=''
  year=''
  author=''
  type=''
  children=() # А почему бы нам не использовать dict - () тут вместо list - [] ? Мы же ничего тут не меняем :)

  def __init__(self, name, type="", year="", author="", children=() ):
      '''
      Если мы используем дефолтные значения для вызова функции, нам не нужно их явно задавать при каждом из вызовов этой функции,
      т.е. это нам позволяет писать вызовы типа PS=Taxon('Gobiidae'), вместо обязательных PS=Taxon(name="", year="", author="", type="", children=() ) в противном случае
      Более подробно рекомендую почитать об этом, например, вот тут: http://younglinux.info/oopython/init.php
      '''
      self.name=name
      self.type=type
      self.year=year
      self.author=author
      self.children=children
      
  def __repr__(self):
	  '''
	  Эта функция используется для так называемой репрезентации объекта и отвечает за то, что будет выводиться при попытке вывести объект - print Obj.
	  '''
	  if self.type:
	     return "{0} {1} ({2})".format(self.name, self.year, self.type)
	  else:
	     return "{0} {1}".format(self.name, self.year)
      

'''
Создаем корень нашего дерева, в нашем случае это будет семейство Бычковых, которое будет содержать в себе подсемейства Benthophilinae, итд.
'''

PS=Taxon(name='Gobiidae',
         type='Семейство',
         children = (
	                 Taxon(name='Benthophilinae',
	                       type='Подсемейство',
	                       children=(
		                             Taxon(name='Benthophilini',
		                                   type='Триба',
		                                   children=(
			                                         Taxon(name='Benthophiloides',
			                                               type='Род',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Taxon(name='Benthophiloides brauneri',
				                                                           type='Вид',
				                                                           author='Iljin',
				                                                           year='1927'),
				                                     
			                                               )),
			                                         Taxon(name='Benthophilus',
			                                               type='Род',
			                                               author='Eichwald',
			                                               year='1831',
			                                               children=(
				                                                     Taxon(name='Benthophilus magistri',
				                                                           type='Вид',
				                                                           author='Iljin',
				                                                           year='1927'),
				                                                     Taxon(name='Benthophilus nudus',
				                                                           type='Вид',
				                                                           author='Berg',
				                                                           year='1898'),
				                                                     Taxon(name='Benthophilus stellatus',
				                                                           type='Вид',
				                                                           author='Sauvage',
				                                                           year='1874'),		                                     
			                                               )),
			                                         Taxon(name='Caspiosoma',
			                                               type='Род',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Taxon(name='Caspiosoma caspium',
				                                                           type='Вид',
				                                                           author='Kessler',
				                                                           year='1877'),
				                                     
			                                               )),			                                               
		                                   )),
		                             Taxon(name='Neogobiini',
		                                   type='Триба',
		                                   children=(
			                                         Taxon(name='Neogobius',
			                                               type='Род',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Taxon(name='Neogobius fluviatilis',
				                                                           type='Вид',
				                                                           author='Pallas',
				                                                           year='1814'),
				                                                     Taxon(name='Neogobius melanostomus',
				                                                           type='Вид',
				                                                           author='Pallas',
				                                                           year='1814'),				                                     
			                                               )),		                                               
		                                   )),
		                             Taxon(name='Ponticolini',
		                                   type='Триба',
		                                   children=(
			                                         Taxon(name='Babka',
			                                               type='Род',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Taxon(name='Babka gymnotrachelus',
				                                                           type='Вид',
				                                                           author='Kessler',
				                                                           year='1857'),			                                     
			                                               )),		                                               
			                                         Taxon(name='Mesogobius',
			                                               type='Род',
			                                               author='Bleeker',
			                                               year='1874',
			                                               children=(
				                                                     Taxon(name='Mesogobius batrachocephalus',
				                                                           type='Вид',
				                                                           author='Pallas',
				                                                           year='1814'),			                                     
			                                               )),
			                                         Taxon(name='Ponticola',
			                                               type='Род',
			                                               author='Iljin',
			                                               year='1874',
			                                               children=(
				                                                     Taxon(name='Ponticola cephalargoides',
				                                                           type='Вид',
				                                                           author='Pinchuk',
				                                                           year='1976'),			                                     
				                                                     Taxon(name='Ponticola eurycephalus eurycephalus',
				                                                           type='Вид',
				                                                           author='Kessler',
				                                                           year='1874'),
				                                                     Taxon(name='Ponticola eurycephalus odessicus',
				                                                           type='Вид',
				                                                           author='Pinchuk',
				                                                           year='1977'),
				                                                     Taxon(name='Ponticola kessleri',
				                                                           type='Вид',
				                                                           author='Gunther',
				                                                           year='1861'),
				                                                     Taxon(name='Ponticola platyrostris',
				                                                           type='Вид',
				                                                           author='Pallas',
				                                                           year='1814'),
				                                                     Taxon(name='Ponticola ratan',
				                                                           type='Вид',
				                                                           author='Nordmann',
				                                                           year='1840'),
			                                               )),
			                                         Taxon(name='Proterorhinus',
			                                               type='Род',
			                                               author='Smitt',
			                                               year='1899',
			                                               children=(
				                                                     Taxon(name='Proterorhinus marmoratus',
				                                                           type='Вид',
				                                                           author='Pallas',
				                                                           year='1814'),			                                     
			                                               )),
		                                   )),
	                       )),
))