from django.db import models
from django.contrib.auth.models import User

class ManagementInfo(models.Model):
    m_name=models.CharField(max_length=100)
    m_id=models.IntegerField(blank=True,null=True)

    def __str__ (self):
        return self.m_name


class PbsInfo(models.Model):
    m_id=models.ForeignKey(ManagementInfo, on_delete=models.CASCADE)
    pbs_name=models.CharField(max_length=100, blank=True, null=True)
    pbs_code=models.IntegerField(blank=True, null= True)
    email=models.EmailField(blank=True,null=True)
    address=models.TextField(blank=True, null=True)
    mobile_no=models.TextField(blank=True , null=True)

    def __str__(self):
        return self.pbs_name
    
    




