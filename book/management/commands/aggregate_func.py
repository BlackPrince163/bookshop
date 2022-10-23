from django.core.management import BaseCommand
from django.db.models import Avg, Sum, Min, Max

from book.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(Book.objects.aggregate(Avg('price')))
        print(Book.objects.aggregate(Sum('price')))
        print(Book.objects.aggregate(Min('price')))
        print(Book.objects.aggregate(Max('price')))
