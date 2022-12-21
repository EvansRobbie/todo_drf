from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
"""
    Using the @api_view decorator
"""
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/todo/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/todo/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/todo/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/todo/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/todo/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getTodo(request, *args, **kwargs):
    todo_instance = Todo.objects.filter(user = request.user.id)
    serializer = TodoSerializer(todo_instance, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def postTodo(request):
    data = {
        'task': request.data.get('task'),
        'completed': request.data.get('completed'),
        'user':request.user.id
    }
    serializer = TodoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET'])
def getTodoDetail(request,todo_id):
    try:
        todo_instance =  Todo.objects.get(id = todo_id, user =request.user.id)
    except Todo.DoesNotExist:
        raise status.HTTP_400_BAD_REQUEST
    if not todo_instance:
        return Response(
            {'res': 'Object with that id doesn\'t exist'},
            status= status.HTTP_400_BAD_REQUEST
        )
    # if request.method == 'GET':
    #     todo_instance = Todo.objects.get(todo_id)
    serializer = TodoSerializer(todo_instance)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['PUT'])
def updateDetail(request, todo_id):
    try:
        todo_instance = Todo.objects.get(id = todo_id,user= request.user.id)
    except Todo.DoesNotExist:
        raise status.HTTP_400_BAD_REQUEST
    if not todo_instance:
        return Response(
            {'res': 'Object with that id doesn\'t exist'},
            status= status.HTTP_400_BAD_REQUEST
        )
    data ={
        'task':request.data.get('task'),
        'completed': request.data.get('completed'),
        'user':request.user.id
    }
    serializer = TodoSerializer(instance=todo_instance, data=data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTodoDetail(request, todo_id):
    try:
        todo_instance = Todo.objects.get(id= todo_id, user = request.user.id)
    except Todo.DoesNotExist:
        raise status.HTTP_400_BAD_REQUEST
    if not todo_instance:
        return Response(
            {'res': 'Object with that id doesn\'t exist'},
            status= status.HTTP_400_BAD_REQUEST
        )
    todo_instance.delete()
    return Response({
        'res':'object detail deleted successfully'
    }, status=status.HTTP_200_OK)
       
"""
    using the APIView
"""
# class TodoApiview(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         '''
#             List all todos for the specific user
#         '''
#         todo_instance = Todo.objects.filter(user = request.user.id)
#         serializer = TodoSerializer(todo_instance, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#         # Create a todo list
#     def post(self,request, *args, **kwargs):
#             '''
#             create a Todo with given todo data
#             '''
#             data = {
#                 'task': request.data.get('task'),
#                 'completed': request.data.get('completed'),
#                 'user': request.user.id
#             }
#             serializer = TodoSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status=status.HTTP_201_CREATED)
            
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TodoDetailsApiview(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get_object(self, todo_id, user_id):
#         try:
#             return Todo.objects.get(id = todo_id, user = user_id)
#         except Todo.DoesNotExist:
#             raise status.HTTP_400_BAD_REQUEST

#     #Retrieve
#     def get(self, request,todo_id, *args, **kwargs):
#         todo_instance= self.get_object(todo_id, request.user.id)
#         if not todo_instance:
#             return Response(
#                 {'res': 'Object with the note id does not exist'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         serializer = TodoSerializer(todo_instance)
#         return Response(serializer.data, status= status.HTTP_200_OK)
    
#     # Update
#     def put(self, request, todo_id, *args, **kwargs):
#         todo_instance = self.get_object(todo_id, request.user.id)
#         if not todo_instance:
#             return Response(
#                 {'res': 'Object with the note id does not exist'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'task': request.data.get('task'),
#             'completed': request.data.get('completed'),
#             'user': request.user.id
#         }
#         serializer = TodoSerializer(instance=todo_instance, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#     # Delete
#     def delete(self, request, todo_id, *args, **kwargs):
#         todo_instance = self.get_object(todo_id, request.user.id)
#         if not todo_instance:
#             return Response(
#                 {'res': 'Object with the note id does not exist'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         todo_instance.delete()
#         return Response ({'res':'Object Deleted'},
#         status=status.HTTP_200_OK
#         )





