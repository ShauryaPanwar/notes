from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [

        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of notes'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'Creates a new note with data sent by post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ''},
            'description': 'Updates a note with data sent by put request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a note'
        }
    ]
    return Response(routes)
