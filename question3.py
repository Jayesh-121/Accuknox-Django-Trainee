"""
Yes django signals by default run in the same trasaction as the caller.
This can be demonstrated by using a signal handler for a model that creates another model object.
An exception can be deliberately raised to invoke a rollback which nullifies both the transactions.

The below snippet has two models, Model1 and Model2. The signal handler for Model1 (post_save) also
creates an object for Model2.
"""
from django.db import models

class Model1(models.Model):
    name = models.CharField(max_length=200)

class Model2(models.Model):
    type = models.CharField(max_length=200)

--------
@receiver(post_save, sender=Model1)
def create_model(sender, instance, **kwargs):
    #Model2 object is created when signal handler for model 1 is executed
    Model2.objects.create(description=f"Created for {instance.name}")
    print("Signal handler executed and Model2 created")
---------


from myapp.models import Model1, Model2

try:
    with transaction.atomic():
        instance = Model1.objects.create(name="Instance1")
        print("Model1 instance created") #Model2 instance is also created

        #Exception is raised to rollbock both database transactions
        raise Exception("Transaction rolled back")

except Exception as e:
    print(f"Exception occurred: {e}")

# Check for Model1 entries
print(Model1.objects.all())  #Will return an empty set
# Check for Model2 entries
print(Model2.objects.all())  #Will return an empty set

"""
When Model1's object creation throws an exception, this rolls back Model2's object creation as they were
both within the same transaction. 
"""
