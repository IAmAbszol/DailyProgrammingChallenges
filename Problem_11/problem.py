import threading
import time

# Construct a job handler - naive approach
def create_job(f, n):
	def sleep_n_call():
		time.sleep(n)
		f()
	t = threading.Thread(target=sleep_n_call)
	t.start()


def print_lol():
	print("lol")


