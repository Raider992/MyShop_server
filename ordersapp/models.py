from django.db import models

from django.conf import settings
from django.db import models

from cartapp.models import Cart
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCESS = 'STP'
    PROCESSED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    DONE = 'DN'
    CANCELLED = 'CNC'

    ORDER_STATUSES = (
        (FORMING,'формируется'),
        (SENT_TO_PROCESS, 'отправлен на обработку'),
        (PROCESSED, 'обработан'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (DONE, 'выдан'),
        (CANCELLED, 'отменён'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='изменён')

    status = models.CharField(
        verbose_name='статус',
        choices=ORDER_STATUSES,
        max_length=4,
        default=FORMING
    )

    is_active = models.BooleanField(default=True, verbose_name='активен')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created_at',)

    def get_total_quantity(self):
        _items = self.orderitems.select_related()
        _total_quantity = sum(list(map(lambda x: x.quantity , _items)))
        return _total_quantity

    def get_total_price(self):
        _items = self.orderitems.select_related()
        _total_cost = sum(list(map(lambda x: x.quantity * x.product.price, _items)))

        return _total_cost

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')

    def get_product_cost(self):
        return self.product.price * self.quantity

    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()
