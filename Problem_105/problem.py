from threading import Timer

def debounce(N):
	
	def wrapper(fn):
		
		def setup(*args, **kwargs):
			
			def call():
				fn(*args, **kwargs)
			
			try:
				setup.t.cancel()
			except (AttributeError):
				pass

			# GitHub post on this, never knew attributes were a thing like this.
			setup.t = Timer(N, call)
			setup.t.start()
		
		return setup			

	return wrapper
