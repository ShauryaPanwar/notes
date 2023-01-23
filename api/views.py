from django.http import JsonResponse

def getRoutes(request):

    routes =[
        {
            'Endpoint' : '/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns array of notes'
        },
        {
            'Endpoint' : '/notes/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single note objects'

        },

        {
            'Endpoint' : '/notes/create',
            'method' : 'POST',
            'body' : {'body':""},
            'description' : 'Creates new notes with data sent in post request'
        },

        {
            'Endpoint' : '/notes/id/update/',
            'method' : 'PUT',
            'body' : {'body':""},
            'description' : 'Creates existing notes with data sent in put request'
        },

        {
            'Endpoint' : '/notes/id/delete/',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes existing notes'
        }
    ]
    return JsonResponse(routes ,safe=False)