import _thread
import time

from Imprime import Imprime

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 8:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

	  
imp = Imprime()	  
	  
# Create two threads as follows
try:
   #_thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   #_thread.start_new_thread( print_time, ("Thread-2", 0.5, ) )
   _thread.start_new_thread( imp.incrementa, () )
except:
   print ("Error: unable to start thread")

i = 0
while i < 10:
	print(str(i)+"fora")
	time.sleep(0.5)
	i+=1
   
while 1:
   pass