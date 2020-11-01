import unittest
from app.models import Blog,User
from app import db
class TestBlog(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_blog = Blog(id=2, title='title', text ='Random things' posted =2020-11-1 19:38:16.599979,user = self.user_James )
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,2)
        self.assertEquals(self.new_blog.title,'title')
        self.assertEquals(self.new_blog.text,'Random things')
        self.assertEquals(self.new_blog.posted,2020-11-1 19:38:16.599979)
        self.assertEquals(self.new_blog.user,self.user_James)
    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
    