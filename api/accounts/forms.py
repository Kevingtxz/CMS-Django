from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # __all__ -> return every attribute of Order
        fields = '__all__'
