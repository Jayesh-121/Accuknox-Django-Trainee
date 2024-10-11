"""
Yes, django signals and the caller both run in the same thread.
This can be observed using the threading module to get the thread ids for both.
"""
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)

---------
import threading

@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, **kwargs):
    print(f"Thread: {threading.get_ident()}") #Prints thread id

----------

print(f"Main thread: {threading.get_ident()}") #prints main thread id
instance = MyModel.objects.create(name="New Instance") #prints signal handler thread id


""" 
In the above example the thread ids corresponding to both the caller (main) and the 
receiver (signal_handler) are observed to be the same.
"""