from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.core.cache import cache

from .models import CartItems

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量',min_value=1)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ['quantity','id']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        id = cleaned_data.get('id')
        cart_item = get_object_or_404(CartItems,pk=id)
        if quantity  is None or cart_item.product.stock is None:
            raise ValidationError(f'在庫数を超えています。{cart_item.product.stock}以下にしてください')
        
from .models import Addresses

class AddressInputForm(forms.ModelForm):
    address = forms.CharField(label='住所',widget=forms.TextInput(attrs={'size':'80'}))

    class Meta:
        model = Addresses
        fields = ['zip_code','prefecture','address']
        labels = {
            'zip_code':'郵便番号',
            'prefecture':'都道府県',
        }
    def save(self, commit=True):
        address = super().save(commit=False)
        address.user =self.user
        try:
            address.validate_unique()
            address.save()
        except ValidationError as e:
            pass

        if commit:
            address.save()
            cache.set(f'address_user_{address.user.id}', address)
        return address
    