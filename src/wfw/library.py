

class library(object):
	def __init__(self,cont):
		self.cont = cont

	def _set(self,name,val):
		setattr(self.cont,name,val)