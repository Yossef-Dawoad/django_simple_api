from .models import ActiveLock
from rest_framework import serializers



class ActiveLockObjSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActiveLock
        fields = ['state', 'init_state']