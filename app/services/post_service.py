import math
from app.models.post import Post
from app.repository.post_repository import PostRepository


class PostService:

    def __init__(self):
        self.repository = PostRepository()
        self.DEFAULT_LIMIT = 20
        self.MAX_LIMIT = 100

    def getAllArticle(self, limit, offset):

        if limit <= 0:
            limit = self.DEFAULT_LIMIT

        if limit > self.MAX_LIMIT:
            limit = self.MAX_LIMIT

        if offset < 0:
            offset = 0

        posts, total_items = self.repository.getAllArticle(limit, offset)

        posts_list = [post.to_dict() for post in posts]

        total_pages = math.ceil(total_items / limit) if total_items > 0 else 1

        return {
            'posts': posts_list,
            'total_items': total_items,
            'limit': limit,
            'offset': offset,
            'total_pages': total_pages
        }
    
    def createArticle(self, data):
        posts = Post(
            title=data['title'],
            content=data['content'],
            category=data['category'],
            status=data['status']
        )

        return self.repository.createArticle(posts)
    
    def getArticleById(self, id):
        return self.repository.getArticleById(id)
    
    def updateArticle(self, id, data):
        posts = self.repository.getArticleById(id)

        if not posts:
            return None
        
        posts.title = data.get('title', posts.title)
        posts.content = data.get('content', posts.content)
        posts.category = data.get('category', posts.category)
        posts.status = data.get('status', posts.status)

        return self.repository.updateArticle(posts)
    

    def deleteArticle(self, id):
        posts = self.repository.deleteArticle(id)
        return posts