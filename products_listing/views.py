from django.shortcuts import render
from openpyxl import load_workbook
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Product, ProductVariation
import os
def index(request):
    products = Product.objects.all()
    for product in products:
        product_variations = ProductVariation.objects.filter(product_id=product.uid)
        product.variations = product_variations
    print(type (products))
    context = {
        'products': products,
    }
    return render(request, 'products_listing/main.html', context)

@csrf_exempt
def add_product(request):
    if request.method == 'POST' and request.FILES['excel']:
        # Get the uploaded file
        file = request.FILES['excel']
        # Load the XLSX file
        workbook = load_workbook(filename=file)

        sheet_name = workbook.sheetnames[0]
        worksheet = workbook[sheet_name]
        for i, row in enumerate(worksheet.iter_rows()):
            if i == 0:
                continue

            print(row[0].value, row[1].value, row[2].value)

            products = Product.objects.filter(name=row[0].value)
            if products:
                for product in Product.objects.filter(name=row[0].value):
                    print('product exists')
                    product_variations_list = ProductVariation.objects.filter(product_id=product.uid, variation_text=row[1].value)
                    if product_variations_list:
                        for product_variation in product_variations_list:
                            product_variation.stock += row[2].value
                            product_variation.save()
                    else:
                        ProductVariation.objects.create(
                            product_id=product,
                            variation_text=row[1].value,
                            stock=row[2].value,
                        )
                # TODO: Update the product's lowest price, update TIMESTAMP
            else:
                product = Product.objects.create(
                    name=row[0].value,
                    lowest_price=row[2].value,
                )
                product.save()
                ProductVariation.objects.create(
                    product_id=product,
                    variation_text=row[1].value,
                    stock=row[2].value,
                ).save()
    
    return JsonResponse({'success': True})
