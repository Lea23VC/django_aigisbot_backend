from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Game
from rest_framework.pagination import PageNumberPagination
from rest_api.serializers.game import GameSerializer


@api_view(["GET"])
def game_list(request):
    # Create a paginator instance with the fixed page size of 10
    paginator = PageNumberPagination()
    paginator.page_size = 10

    # Get the paginated games for the requested page
    games = Game.objects.all()
    print("### query: ", games.query)
    paginated_games = paginator.paginate_queryset(games, request, view=None)

    # Serialize the paginated games
    serializer = GameSerializer(paginated_games, many=True)

    # Return the paginated games in the response
    return paginator.get_paginated_response(serializer.data)
