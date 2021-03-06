#-*- coding: utf-8 -*-
from rlbig.BioAlg import flattenTree, flattenDictTree, flattenSearch, flattenLSearch, flattenDSearch, flattenOSearch
from rlbig.BioOptimization import findOptimumSearch



class Taxon:
  searchAlg = ''

  def __init__(self, name, type="", year="", author="", children=(), is_root=False):
      '''
      Initialization
      '''
      self.name=name
      self.type=type
      self.year=year
      self.author=author
      self.children=children
      self.is_root = is_root
      self.parent = self
      
  def __call__(self, optimization_runs=2**4):
      '''
      Determinate based on build-in tests which searching algorithm is optimal for the current Tree structure and size.
      '''
      if self.is_root:
         self.searchAlg = findOptimumSearch(self, runs = optimization_runs, algs=['findF','find_linear','find_dict_linear','findO'], warmup=['flatten','flattenDict'])
         self.setParents(self)
      return self

  def __repr__(self):
      '''
      Self-representation
      '''
      if self.type:
         return "{0} {1} ({2})".format(self.name, self.year, self.type)
      else:
         return "{0} {1}".format(self.name, self.year)


  def flattenDict(self,printout=False):
      '''
      Returns a flattened copy of the tree.
      '''
      return flattenDictTree(self, 0, printout)


  def flatten(self,printout=False):
      '''
      Returns a flattened copy of the tree.
      '''
      return flattenTree(self, 0, printout)


  def setParents(self, parent):
      '''
      Sets recursively parent node for each children node
      '''
      self.parent = parent
      for c in self.children:
          c.setParents(self)
  


  def find(self, text='',type='',raw=False,alg=None):
      '''
      Searches in it's own tree. 
      Use the dynamical search function based on result of calling findOptimumSearch
      '''
      sfunc = getattr(self, self.searchAlg) if not alg else getattr(self, alg)
      return sfunc(text, type, raw)


  def findF(self, text='',type='',raw=False):
      '''
      Searches in it's own tree. 
      Return raw information, if raw parameter is given.
      '''
      return flattenSearch(self, text, type, raw)


  def findO(self, text='',type='',raw=False):
      '''
      Searches in it's own tree. 
      Return raw information, if raw parameter is given.
      '''
      return flattenOSearch(self, text, type, raw)


  def find_linear(self, text='',type='',raw=False):
      '''
      Searches in it's own tree. 
      Return raw information, if raw parameter is given.
      '''
      return flattenLSearch(self, text, type, raw)


  def find_dict_linear(self, text='',type='',raw=False):
      '''
      Searches in it's own tree. 
      Return raw information, if raw parameter is given.
      '''
      return flattenDSearch(self, text, type, raw)