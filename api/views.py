from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import BenefactorSerializers, MedicReportSerializers, BeneficiarySerializers
from api.models import Benefactor, MedicReport, Beneficiary

# Create your views here.

@api_view(['GET'])
def benefactorShow (request):
    benefactor = Benefactor.objects.all()
    serializer = BenefactorSerializers(benefactor, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def benefactorCreate (request):
    serializer =BenefactorSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def benefactorRead (request, pk):
    benefactor = Benefactor.objects.get(id = pk)
    serializer = BenefactorSerializers(benefactor, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def benefactorUpdate(request, pk):
    benefactor = Benefactor.objects.get(id = pk)
    serializer = BenefactorSerializers(instance = benefactor, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def benefactorDelete(request, pk):
    benefactor = Benefactor.objects.get(id = pk)
    benefactor.delete()
    return Response('Eliminado')




@api_view(['GET'])
def medicReportShow (request):
    report = MedicReport.objects.all()
    serializer = MedicReportSerializers(report, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def medicReportCreate (request):
    serializer =MedicReportSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def medicReportRead (request, pk):
    report = MedicReport.objects.get(id = pk)
    serializer = MedicReportSerializers(report, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def medicReportUpdate(request, pk):
    report = MedicReport.objects.get(id = pk)
    serializer = MedicReportSerializers(instance = report, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def medicReportDelete(request, pk):
    report = MedicReport.objects.get(id = pk)
    report.delete()
    return Response('Eliminado')



@api_view(['GET'])
def beneficiaryShow (request):
    beneficiary = Beneficiary.objects.all()
    serializer = BeneficiarySerializers(beneficiary, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def beneficiaryCreate (request):
    serializer =BeneficiarySerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def beneficiaryRead (request, pk):
    beneficiary = Beneficiary.objects.get(id = pk)
    serializer = BeneficiarySerializers(beneficiary, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def beneficiaryUpdate(request, pk):
    beneficiary = Beneficiary.objects.get(id = pk)
    serializer = BeneficiarySerializers(instance = beneficiary, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def beneficiaryDelete(request, pk):
    beneficiary = Beneficiary.objects.get(id = pk)
    beneficiary.delete()
    return Response('Eliminado')   

