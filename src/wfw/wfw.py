import constants

import traceback


def serve_page(request):
	request.setHeader("content-type", "text/plain")
	URL = request.postpath

	try:
		controller = URL[0]
		if not controller:
			raise
	except:
		controller = "index"

	try:
		function = URL[1]
	except:
		function = "index"

	try:
		arguments = URL[2:]
	except:
		arguments = []

	controllepath = constants.WFW_APPFOLDER +".controllers."+controller
	cont = __import__(controllepath,fromlist=[controller])

	contclass = getattr(cont,controller.title())()


	function = getattr(contclass,function)
	return function(*arguments)



def start(port=8080):
	print constants.WFW_VERSION
	from twisted.web import server, resource
	from twisted.internet import reactor

	class HelloResource(resource.Resource):
		isLeaf = True		
		def render_GET(self, request):
			try:
				return serve_page(request)
			except Exception as ex:
				return traceback.format_exc()



	reactor.listenTCP(port, server.Site(HelloResource()))
	reactor.run()