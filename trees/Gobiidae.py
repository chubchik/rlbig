#-*- coding: utf-8 -*-
from rlbig.models import *

Gobiidae = Taxon(name='Gobiidae',
                 type='Family',
                 children = (
	                 Taxon(name='Benthophilinae',
	                       type='Subfamily',
	                       children=(
		                             Taxon(name='Benthophilini',
		                                   type='Tribe',
		                                   children=(
			                                         Taxon(name='Benthophiloides',
			                                               type='Genus',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Species(name='Benthophiloides brauneri',
				                                                             author='Iljin',
				                                                             year='1927',
				                                                             length=21,
				                                                             children=(
					                                                             Head(length=6, children=(
						                                                             Spot(size=10, color=(55, 200, 15)),
						                                                             Spot(size=7, color=(5, 200, 150)),
						                                                             Spot(size=1, color=(155, 200, 15)),
						                                                             Spot(size=15, color=(255, 0, 150)),
					                                                             )),
					                                                             Body(length=10),
					                                                             Tail(length=5, color=(255, 200, 15)),
				                                                             )),
				                                     
			                                               )),
			                                         Taxon(name='Benthophilus',
			                                               type='Genus',
			                                               author='Eichwald',
			                                               year='1831',
			                                               children=(
				                                                     Species(name='Benthophilus magistri',
				                                                             author='Iljin',
				                                                             year='1927'),
				                                                     Species(name='Benthophilus nudus',
				                                                             author='Berg',
				                                                             year='1898'),
				                                                     Species(name='Benthophilus stellatus',
				                                                             author='Sauvage',
				                                                             year='1874'),		                                     
			                                               )),
			                                         Taxon(name='Caspiosoma',
			                                               type='Genus',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Species(name='Caspiosoma caspium',
				                                                             author='Kessler',
				                                                             year='1877'),
			                                               )),			                                               
		                                   )),
		                             Taxon(name='Neogobiini',
		                                   type='Tribe',
		                                   children=(
			                                         Taxon(name='Neogobius',
			                                               type='Genus',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Species(name='Neogobius fluviatilis',
				                                                             author='Pallas',
				                                                             year='1814'),
				                                                     Species(name='Neogobius melanostomus',
				                                                             author='Pallas',
				                                                             year='1814'),				                                     
			                                               )),		                                               
		                                   )),
		                             Taxon(name='Ponticolini',
		                                   type='Tribe',
		                                   children=(
			                                         Taxon(name='Babka',
			                                               type='Genus',
			                                               author='Iljin',
			                                               year='1927',
			                                               children=(
				                                                     Species(name='Babka gymnotrachelus',
				                                                             author='Kessler',
				                                                             year='1857'),			                                     
			                                               )),		                                               
			                                         Taxon(name='Mesogobius',
			                                               type='Genus',
			                                               author='Bleeker',
			                                               year='1874',
			                                               children=(
				                                                     Species(name='Mesogobius batrachocephalus',
				                                                             author='Pallas',
				                                                             year='1814'),			                                     
			                                               )),
			                                         Taxon(name='Ponticola',
			                                               type='Genus',
			                                               author='Iljin',
			                                               year='1874',
			                                               children=(
				                                                     Species(name='Ponticola cephalargoides',
				                                                             author='Pinchuk',
				                                                             year='1976'),			                                     
				                                                     Species(name='Ponticola eurycephalus eurycephalus',
				                                                             author='Kessler',
				                                                             year='1874'),
				                                                     Species(name='Ponticola eurycephalus odessicus',
				                                                             author='Pinchuk',
				                                                             year='1977'),
				                                                     Species(name='Ponticola kessleri',
				                                                             author='Gunther',
				                                                             year='1861'),
				                                                     Species(name='Ponticola platyrostris',
				                                                             author='Pallas',
				                                                             year='1814'),
				                                                     Species(name='Ponticola ratan',
				                                                             author='Nordmann',
				                                                             year='1840'),
			                                               )),
			                                         Taxon(name='Proterorhinus',
			                                               type='Genus',
			                                               author='Smitt',
			                                               year='1899',
			                                               children=(
				                                                     Species(name='Proterorhinus marmoratus',
				                                                             author='Pallas',
				                                                             year='1814'),			                                     
			                                               )),
		                                   )),
	                       )),
), is_root=True)