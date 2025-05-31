from django.core.management.base import BaseCommand
from mainapp.gentestdata import gentestdata


class Command(BaseCommand):
    help = 'Генерирует тестовые данные для автомобилей'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help='Количество автомобилей для создания (по умолчанию: 100)',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Удалить все существующие автомобили перед генерацией',
        )

    def handle(self, *args, **options):
        from mainapp.models import Car
        
        count = options['count']
        
        if options['clear']:
            Car.objects.all().delete()
            self.stdout.write(
                self.style.WARNING('Все существующие автомобили удалены.')
            )
        
        # Генерируем данные
        gentestdata(count)
        
        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {count} автомобилей.')
        ) 