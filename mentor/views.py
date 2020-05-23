from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request,format=None):
    response = Response({
        'urls' #будут все ссылки по которым можно будет переходить
    })
    return response