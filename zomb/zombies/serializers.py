from rest_framework import serializers
from .models import Zombie
import datetime


class ZombieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zombie

















    # is_noob = serializers.SerializerMethodField()

    # # Noobs survived less than two weeks after the outbreak
    # def get_is_noob(self, obj):
    #     return obj.date_of_rebirth < obj.DATE_OF_OUTBREAK + datetime.timedelta(weeks=2)


# class NoobSerializer(serializers.Serializer):
#     is_noob = serializers.SerializerMethodField()
#     def get_is_noob(self, obj):
#         return obj.date_of_rebirth < obj.DATE_OF_OUTBREAK + datetime.timedelta(weeks=2)

