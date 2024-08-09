from maybewrite import db, app
from maybewrite.models import User,Post  
#run this file to create an sqlalchemy database


with app.app_context():
    # db.create_all()
    # user_1 = User(username="Ritwik", email="rt@gmail.com", password="password")
    # db.session.add(user_1)
    # user_2 = User(username="Tarini", email="t@gmail.com", password="password")
    # db.session.add(user_2)
    # db.session.commit()
    # users = User.query.all()
    # for user in users:
    #     print(user.posts)
    #     print(user.id)
    # print(users)
    
    # post_1=Post(title='Blog 1',content='First post content!',user_id=1)
    # post_2=Post(title='Blog 2',content='Second post content!',user_id=1)
    # db.session.add(post_1)
    # db.session.add(post_2)
    # db.session.commit()
    
    # for user in users:
    #     print(user.id)
    #     print(user.posts)
    
    # posts=Post.query.all()
    # for post in posts:
    #     # print(post)
    #     print(post.author.username)
    # db.drop_all()
    
    # db.create_all()
    users=User.query.all()
    for user in users:
        print(user)
    # print(users)
    print()
    posts=Post.query.all()
    for post in posts:
        print(post)
    # db.create_all()
    
    
