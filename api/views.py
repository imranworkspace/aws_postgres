from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT','DELETE'])
def student(request):
    if request.method=='GET':
        id = request.data.get('id')
        if id is not None:
            stu = StudentModel.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
        stu = StudentModel.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id=request.data.get('id')
        stu=StudentModel.objects.get(pk=id)
        serializer = StudentSerializers(stu,
            data=request.data,
            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'recored updated'})
        return Response(serializer.errors)
        
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=StudentModel.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'record deleted'})