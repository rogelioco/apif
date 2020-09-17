from django.db import models
from django.utils import timezone

# Create your models here.
class Benefactor(models.Model):
    full_name = models.CharField(max_length = 50, null = False)
    curp = models.CharField(max_length = 100, null = False)
    nss =  models.CharField(max_length = 100, null = False)
    genre = models.CharField(max_length = 50, null = False)
    blood_type = models.CharField(max_length = 25, null = False)
    address = models.CharField(max_length = 50, null = False)
    country = models.CharField(max_length = 50, null = False)
    state = models.CharField(max_length = 50, null = False)
    city = models.CharField(max_length = 50, null = False)
    postal_code = models.CharField(max_length = 50, null = False)
    email = models.CharField(max_length = 50, null = False)
    phone_number = models.CharField(max_length = 50, null = False)
    salary = models.CharField(max_length = 50, null = False)
    insured_amount = models.CharField(max_length = 50, null = False)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'm_insurance_benefactor'

class MedicReport(models.Model):
    id_insurance_benefactor = models.ForeignKey(Benefactor, on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    weight = models.FloatField(null = False)
    imc = models.FloatField(null = False)
    blood_pressure = models.FloatField(null = False)
    uric_acid = models.FloatField(null = False)
    cholesterol = models.FloatField(null = False)
    triglycerides = models.FloatField(null = False)
    creatine = models.FloatField(null = False)
    chronic_deseases = models.CharField(max_length = 50, null = False)

    def __str__(self):
        return self.id_insurance_benefactor
    
    class Meta:
        db_table = 'm_insurance_medic_report'

class Beneficiary(models.Model):
    id_insurance_benefactor = models.ForeignKey(Benefactor, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 50, null = False)
    curp = models.CharField(max_length = 100, null = False)
    nss =  models.CharField(max_length = 100, null = False)
    genre = models.CharField(max_length = 50, null = False)
    blood_type = models.CharField(max_length = 50, null = False)
    address = models.CharField(max_length = 50, null = False)
    country = models.CharField(max_length = 50, null = False)
    state = models.CharField(max_length = 50, null = False)
    city = models.CharField(max_length = 50, null = False)
    postal_code = models.CharField(max_length = 50, null = False)
    email = models.CharField(max_length = 50, null = False)
    phone_number = models.CharField(max_length = 50, null = False)
    salary = models.CharField(max_length = 50, null = False)
    insured_amount = models.CharField(max_length = 50, null = False)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'm_insurance_beneficiary'
