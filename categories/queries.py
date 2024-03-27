import graphene

from categories.object_types import CategoryType
from categories.models import Category


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int(required=True))

    def resolve_categories(self, Info):
        return Category.objects.all()
    
    def resolve_category(self, Info, id):
        return Category.objects.get(id=id)
    