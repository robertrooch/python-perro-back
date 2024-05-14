import graphene
from graphene_django import DjangoObjectType

from .models import Link
from users.schema import UserType
from links.models import Link, Vote
from graphql import GraphQLError
from django.db.models import Q


class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    links = graphene.List(LinkType)
    votes = graphene.List(VoteType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

class CreateLink(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    raza = graphene.String()
    edad = graphene.Int()
    foto = graphene.String()
    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
        nombre = graphene.String()
        raza = graphene.String()
        edad = graphene.Int()
        foto = graphene.String()

    #3
    def mutate(self, info, nombre, raza, edad, foto):
        user = info.context.user or None

        link = Link(
                nombre=nombre, 
                raza=raza, 
                edad=edad, 
                foto=foto,
                posted_by=user,
                )
        link.save()

        return CreateLink(
            id=link.id,
            nombre=link.nombre,
            raza=link.raza,
            edad=link.edad,
            foto=link.foto,
            posted_by=link.posted_by,
        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise GraphQLError('Invalid Link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
