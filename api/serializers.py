from rest_framework import serializers
from api.models import Benefactor, MedicReport, Beneficiary

class BenefactorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = ('__all__')

class MedicReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicReport
        fields = ('__all__')

class BeneficiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ('__all__')