from members.models import Member #we need the model we want to serialize
from rest_framework import serializers 

class MemberSerializer(serializers.ModelSerializer):
    class Meta:#always its name is meta
        model=Member
        fields=['firstname','lastname','email']     #fields we want to serialize from object python to json    