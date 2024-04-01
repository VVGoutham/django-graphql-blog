import graphene

from categories.mutations import CreateCategory, DeleteCategory, UpdateCategory
from posts.mutations import CreatePost, DeletePost, UpdatePost


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    