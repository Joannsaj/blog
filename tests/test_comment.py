import unittest
from app.models import Comment, Blog, User
from app import db
class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.blog = Blog(title='title', text ='Random things',user = self.user_James )
        self.new_comment = Comment(id=12, comment ='commenting', blog = self.blog, user = self.user_James )
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12)
        self.assertEquals(self.new_comment.comment,'commenting')
        self.assertEquals(self.new_comment.blog,self.blog)
        self.assertEquals(self.new_comment.user,self.user_James)
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(11)
        self.assertTrue(len(got_comments) == 1)