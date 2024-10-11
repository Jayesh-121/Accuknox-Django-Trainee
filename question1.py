"""
Django signals are synchronous by default and the main thread is blocked until all the
signal receivers have finished execution in the order they are defined.
"""
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
------

@receiver(post_save, sender=MyModel)
def first_signal_handler(sender, instance, **kwargs):
    print("First signal handler started")
    time.sleep(10)  #delay execution completion
    print("First signal handler finished")

@receiver(post_save, sender=MyModel)
def second_signal_handler(sender, instance, **kwargs): #waits for first signal handler to finish
    print("Second signal handler executed")

-------


instance = MyModel.objects.create(name="First") #corresponding signal handlers are executed

"""
When an instance of the model is created in line 24, the first signal handler is executed and completed 
before the second handler is then executed. 

In the above example, we will see print statements in the following order:
"First signal handler started"
"First signal handler finished"
"Second signal handler executed"

If Django signals allowed asynchronous execution, the long running first signal would not have blocked
the shorter second signal handler.
"""

