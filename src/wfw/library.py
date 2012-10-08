from autoloader import autoloader


class library(autoloader):
	def __init__(self,cont):
		self.cont = cont

	def _set(self,name,val):
		setattr(self.cont,name,val)