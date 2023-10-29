import json
import os.path

from django.core.management import BaseCommand
from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Путь к файлам с данными
        path_category = os.path.join(BASE_DIR, 'category_data.json')
        path_product = os.path.join(BASE_DIR, 'product_data.json')

        # Обновление категорий
        with open(path_category) as f:
            category_content = f.read()
            categories_info = json.loads(category_content)
            for info in categories_info:
                category_id = info['fields']['category']
                Category.objects.update_or_create(category=category_id, defaults=info["fields"])

        # Обновление продуктов
        with open(path_product) as f:
            products_info = json.load(f)
            products_for_create = []
            for info in products_info:
                cat_id = info['fields']['category']
                if Category.objects.filter(id=cat_id).exists():
                    category = Category.objects.get(id=cat_id)
                    info['fields']['category'] = category
                    products_for_create.append(Product(**info["fields"]))
                else:
                    # Обработка случаев, когда категория не найдена
                    print(f"Категория с id {cat_id} не найдена.")

            Product.objects.bulk_create(products_for_create)


