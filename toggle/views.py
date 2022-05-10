from rest_framework import response, decorators, status

from toggle.models import ActiveLock
from toggle.serializers import ActiveLockObjSerializer


@decorators.api_view(['GET'])
def read_state(request):
    lock = ActiveLock.objects.last()
    serializer = ActiveLockObjSerializer(lock)
    return response.Response(serializer.data)


@decorators.api_view(['GET'])
def listall_states(request):
    records = ActiveLock.objects.all()
    serializer = ActiveLockObjSerializer(records, many=True)
    return response.Response({'state_hist':serializer.data})

@decorators.api_view(['POST'])
def create_state(request):
    '''
        "Method \"GET\" not allowed." if request.method == GET it
        returns HTTP 405 Method Not Allowed 
    '''
    print(request.data)
    newrecord = ActiveLockObjSerializer(data=request.data)
    print(newrecord)
    if not newrecord.is_valid():
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
    newrecord.save()
    return response.Response({'succsess':True})
    
