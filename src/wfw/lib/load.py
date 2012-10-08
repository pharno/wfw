from wfw.library import library
from wfw.constants import *

from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader

searchpath = [WFW_APPPATH+"views/"]
engine = Engine(
    loader=FileLoader(searchpath),
    extensions=[CoreExtension()]
)

class load(library):
	def view(self,name,data={}):

		template = engine.get_template(name+".tpl")

		return str(template.render(data))

	def model(self,name):

		pack = WFW_APPFOLDER+".models."+name

		package = __import__(pack,fromlist=[name])


		cl = getattr(package,name)
		
		self._set(name,cl())
