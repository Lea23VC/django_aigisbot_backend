import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from core.models import Game, Console, Region


class GameType(DjangoObjectType):
    class Meta:
        model = Game
        # fields = ("id", "name", "console")
        filter_fields = {
            "name": ["iexact", "icontains", "istartswith"],
            "console__name": ["iexact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)


class ConsoleType(DjangoObjectType):
    class Meta:
        model = Console
        fields = ("id", "name")


class Query(graphene.ObjectType):
    all_games = DjangoFilterConnectionField(GameType)
    game = relay.Node.Field(GameType)
    # all_games = graphene.List(GameType)
    # console_by_name = graphene.Field(ConsoleType, name=graphene.String(required=True))

    # def resolve_all_games(root, info):
    #     # We can easily optimize query count in the resolve method
    #     return Game.objects.select_related("console").all()

    # def resolve_console_by_name(root, info, name):
    #     try:
    #         return Console.objects.get(name=name)
    #     except Console.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query)
