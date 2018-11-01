from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.dunco = Editor(first_name='Duncan',
                            last_name='Arani', email='aruncodunco@gmail.com')
        self.dunco.save_editor()

        # creating new tags and saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(
            title='test Article', paost='This is a random test Post', editor=self.dunco)

        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    # testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.dunco, Editor))

     # Testing Save Method
    def test_save_method(self):
        self.dunco.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_get_news_of_day(self):
        today_news = Article.news_today()
        self.assertTrue(len(news_of_day) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.news_today(date)
        self.assertTrue(len(news_by_date) == 0)
