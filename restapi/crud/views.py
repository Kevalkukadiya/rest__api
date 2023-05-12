from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from crud.models import Singer, Album
from crud.serializers import SingerSerializers, AlbumSerializers

# Create your views here.

class SingerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Singer.objects.all()
        serializer = SingerSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = SingerSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg': 'Singer Add Succesfull'},
                status=status.HTTP_201_CREATED
                )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def retrieve(self, request, pk=None):
        singer = Singer.objects.get(pk=pk)
        serailizer = SingerSerializers(singer)
        return Response(serailizer.data)
    

    def put(self, request, pk=None):
        queryset = Singer.objects.get(pk=pk)
        serializer = SingerSerializers(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg':'Singer Update'},
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def patch(self, request, pk=None):
        queryset = Singer.objects.get(pk=pk)
        serializer = SingerSerializers(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg':'Singer Fully Update'},
                status=status.HTTP_202_ACCEPTED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def destroy(self, request, pk=None):
        queryset = Singer.objects.get(pk=pk)
        queryset.delete()
        return Response(
            {'msg':'Singer Delete'},
            status=status.HTTP_204_NO_CONTENT
        )
    

class AlbumViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializers(queryset, many=True)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = AlbumSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Album Create"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def retrieve(self, request, pk=None):
        queryset = Album.objects.get(pk=pk)
        serializer = AlbumSerializers(queryset)
        return Response(serializer.data)
    

    def put(self, request, pk=None):
        quertset = Album.objects.get(pk=pk)
        serializer = AlbumSerializers(quertset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg" : "Album Update"},
                status=status.HTTP_202_ACCEPTED   
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def patch(self, request, pk=None):
        queryset = Album.objects.get(pk=pk)
        serializer = AlbumSerializers(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Album Update Succefully"},
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

    def destroy(self, request, pk=None):
        album = Album.objects.get(pk=pk)
        album.delete()
        return Response(
            {"msg": "Album Delete"},
            status=status.HTTP_204_NO_CONTENT
        )