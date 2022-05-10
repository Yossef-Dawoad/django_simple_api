from typing_extensions import Required
from django.db import models
from numpy import require



class ActiveLock(models.Model):
    # user = models.CharField(User, max_length=200)
    state = models.BooleanField()
    created_in = models.DateTimeField(auto_now_add=True)
    init_state = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name 
