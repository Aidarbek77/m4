from django.core.management.base import BaseCommand
from posts.models import Category, Tag, Post

class Command(BaseCommand):
    help = 'Creates initial data for the blog'

    def handle(self, *args, **kwargs):
        # Create categories
        categories = [
            'Technology',
            'Travel',
            'Food',
            'Health',
            'Entertainment'
        ]
        
        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)
        
        self.stdout.write(self.style.SUCCESS('Categories created successfully!'))
        
        # Create tags
        tags = [
            'Python', 'Django', 'Web Development', 'Data Science',
            'Europe', 'Asia', 'Adventure', 'Budget Travel',
            'Recipes', 'Restaurant Reviews', 'Cooking Tips',
            'Fitness', 'Mental Health', 'Nutrition',
            'Movies', 'Music', 'Books', 'TV Shows'
        ]
        
        for tag_name in tags:
            Tag.objects.get_or_create(name=tag_name)
        
        self.stdout.write(self.style.SUCCESS('Tags created successfully!'))
        
        # Create some sample posts if none exist
        if Post.objects.count() == 0:
            tech_category = Category.objects.get(name='Technology')
            travel_category = Category.objects.get(name='Travel')
            
            # Create a tech post
            tech_post = Post.objects.create(
                title='Getting Started with Django',
                content='Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.',
                rate=5,
                category=tech_category
            )
            
            # Add tags to the tech post
            tech_post.tags.add(
                Tag.objects.get(name='Python'),
                Tag.objects.get(name='Django'),
                Tag.objects.get(name='Web Development')
            )
            
            # Create a travel post
            travel_post = Post.objects.create(
                title='10 Must-Visit Places in Europe',
                content='Europe is filled with incredible destinations. From the romantic streets of Paris to the historic ruins of Rome, there\'s something for every traveler. Here are our top 10 must-visit places in Europe that should be on your bucket list.',
                rate=4,
                category=travel_category
            )
            
            # Add tags to the travel post
            travel_post.tags.add(
                Tag.objects.get(name='Europe'),
                Tag.objects.get(name='Adventure'),
                Tag.objects.get(name='Budget Travel')
            )
            
            self.stdout.write(self.style.SUCCESS('Sample posts created successfully!'))
        else:
            self.stdout.write(self.style.SUCCESS('Posts already exist, skipping sample post creation.'))
            pass