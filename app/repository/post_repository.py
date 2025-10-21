from app import db
from app.models.post import Post

class PostRepository:

    def getAllArticle(self, limit, offset):
        posts = Post.query.offset(offset).limit(limit).all()
        total_items = db.session.query(Post.id).count()

        return posts, total_items
    
    def createArticle(self, posts):
        db.session.add(posts)
        db.session.commit()
        return posts
    
    def getArticleById(self, id):
        return Post.query.get(id)
    
    def updateArticle(self, post_to_update):
        db.session.commit()
        return post_to_update
    
    def deleteArticle(self, id):
        post = Post.query.get(id)

        if not post:
            return False
        
        db.session.delete(post)
        db.session.commit()
        return True

