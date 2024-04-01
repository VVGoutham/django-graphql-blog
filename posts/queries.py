import graphene

from posts.object_types import PostType
from posts.models import Post


class PostQuery(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id = graphene.Int(required=True))
    
    def resolve_posts(self, Info):
        return Post.objects.all()
    
    def resolve_post(self, Info, id):
       return Post.objects.get(id=id)
    