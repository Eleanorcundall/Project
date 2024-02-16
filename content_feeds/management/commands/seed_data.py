from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from content_feeds.models import AdPost
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with dummy data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        for _ in range(90):
            title = fake.sentence()
            content = fake.paragraph()
            category = fake.random_element(elements=('Hair', 'Skin', 'Sexual Wellness', 'Menstrual Wellness'))
            author = User.objects.first()
            AdPost.objects.create(title=title, content=content, category=category, author=author, status='published')


        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))
