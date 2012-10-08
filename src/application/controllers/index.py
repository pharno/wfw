from wfw.Controller import Controller


class Index(Controller):
	def index(self):
		data = {
			'title': "yoooo"
		}

		self.load.model("testmodel")

		print self.testmodel.getIndex()
		return self.load.view("asd",data)

	def sub(self):
		return "YOOOOO"