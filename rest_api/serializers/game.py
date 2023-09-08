from rest_framework.serializers import ModelSerializer
from core.models import Game, Console, Region


class ConsoleSerializer(ModelSerializer):
    class Meta:
        model = Console  # Replace with your Console model
        fields = "__all__"


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region  # Replace with your Region model
        fields = "__all__"


class GameSerializer(ModelSerializer):
    console = ConsoleSerializer()
    region = RegionSerializer()

    class Meta:
        model = Game
        fields = "__all__"
