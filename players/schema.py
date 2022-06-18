import graphene
from graphene_django import DjangoObjectType

from .models import Player


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class Query(graphene.ObjectType):
    players = graphene.List(PlayerType)

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()


#1
class CreatePlayer(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    nationality = graphene.String()
    date = graphene.String()
    team = graphene.String()
    url = graphene.String()
    

    #2
    class Arguments:
        name = graphene.String()
        nationality = graphene.String()
        date = graphene.String()
        team = graphene.String()
        url = graphene.String()
        

    #3
    def mutate(self, info, name, nationality, date, team, url):
        player = Player(name=name, nationality=nationality, date=date, team=team, url=url)
        player.save()

        return CreatePlayer(
            id=player.id,
            name=player.name,
            nationality=player.nationality,
            date=player.date,
            team=player.team,
            url=player.url,
            
        )


#4
class Mutation(graphene.ObjectType):
    create_player = CreatePlayer.Field()
