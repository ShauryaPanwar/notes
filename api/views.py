from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NoteSelectSerializer
from .models import Note

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


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSelectSerializer(notes, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def singleNotes(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSelectSerializer(notes, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def createnotes(request):
    data=request.data

    note=Note.objects.create(
        body=data['body']
    )

    serializer = NoteSelectSerializer(note, many=False)
    return Response(serializer.data)




@api_view(['PUT'])
def updatenotes(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer = NoteSelectSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def deletenotes(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')