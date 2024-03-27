import graphene

from categories.mutations import CreateCategory, DeleteCategory, UpdateCategory


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()