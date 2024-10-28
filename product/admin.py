import decimal
from django.contrib import admin
from django.utils.text import slugify
from mptt.admin import DraggableMPTTAdmin
from .models import *


# Register your models here.
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True
        )
        qs = Category.objects.add_related_count(qs,
                                                Product,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    ordering = ['title']
    search_fields = ['title']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]

    def apply_discount(self, request, queryset):
        for prod in queryset:
            prod.price = decimal.Decimal(prod.price) * decimal.Decimal('0.9')
            prod.save()

    actions = [apply_discount]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'create_at']
    readonly_fields = ('subject', 'comment', 'ip', 'product', 'rate', 'id')


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'img']


class ShopeeAdmin(admin.ModelAdmin):
    list_display = ['title', 'variants']
    readonly_fields = ['product_url', 'img_urls',
                       'price', 'description', 'categories',
                       'variants', 'brand', 'supplier']

    def add_to_product(self, request, queryset):
        for qur in queryset:
            try:
                product = Product.objects.create(
                    title=qur.title,
                    slug=slugify(qur.title),
                    description=qur.description,
                    price=qur.price,
                    src_url=qur.product_url,
                    variant=qur.variant_type,
                    category=Category.objects.get(title=qur.categories[-1])
                )

                product.img_url = qur.img_urls[0]
                product.image = product.get_remote_image()
                product.save()

                # Add images
                for img_url in qur.img_urls[1:]:
                    img = Images(product=product, img_url=img_url)
                    img.image = img.get_remote_image()
                    img.save()

                # Add variants
                for var_title in qur.variants:
                    variant = Variants(product=product, title=var_title)
                    variant.save()

            except Exception as e:
                self.message_user(request, f'Error processing {qur.title}: {str(e)}', level='error')

    actions = [add_to_product]


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductFromShopee, ShopeeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Variants, VariantsAdmin)
admin.site.register(Slider, SliderAdmin)