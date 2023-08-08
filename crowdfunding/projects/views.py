from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
import requests



class AddressAutocomplete(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        user_query = "219 Nor" #expose this to user somehow?
        
        gnaf_pred_addr_url = "https://api.psma.com.au/v1/predictive/address"   
        
        querystring = {"query": user_query }
        
        headers = {
            "Accept":"application/json",
            "Authorization":""
        } #
        addr_suggestions = requests.get(gnaf_pred_addr_url, headers=headers, params=querystring)

        return Response(addr_suggestions.json())
    
class AddressXY(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, query_addr_id):

        query_addr_id = "GAACT717940975" #get this somehow from user through suggested list/form box
        
        gnaf_addr_url = "https://api.psma.com.au/v1/predictive/address/"
      
        url = "/".join(gnaf_addr_url,query_addr_id)
        headers = {
            "Accept":"application/json",
            "Authorization":""
        }
        
        addr_details = requests.get(url, headers)

        return Response(addr_details)


# Create your views here.
class ProjectList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, query_addr_id):

        geo_data = AddressXY.get(self, request, query_addr_id)
        print(request.data)
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            #serializer.save()

            serializer.save(owner=request.user)
            #return Response(serializer.data)
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        #return Project.objects.get(pk=pk)
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)

            return project
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer =  ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsSupporterOrReadOnly]
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class PledgeDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsSupporterOrReadOnly]
    
    def get_object(self, pk):
        #return Project.objects.get(pk=pk)
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        
        except Pledge.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)
        
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer =  PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)