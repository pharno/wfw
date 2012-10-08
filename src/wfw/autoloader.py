

class autoloader(object):
	def __getattr__(self,name):
		mod = __import__("wfw.lib."+name,fromlist=[name])


		cl = getattr(mod,name)


		return cl(self) 