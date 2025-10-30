import threading
import time

def print_numbers():
	for iterator in range(1, 500):
		print(iterator, end=",")
	print("completed printing numbers")

def print_letters():
	for ch in range(65, 91):
		print(chr(ch), end=",")
	print("completed printing alphabets")


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

start = time.time()


thread1.start()
thread2.start()


thread1.join()
thread2.join()

end = time.time()
print(f"\nTotal time taken: {end - start:.2f} seconds")
