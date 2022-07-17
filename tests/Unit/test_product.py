from typing import Dict

import pytest

# @pytest.mark.django_db
# def test_product_created():
#   Product.objects.create
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from django.template.context_processors import request

from base.models import Product
from django.contrib.auth.models import User


def create_product():
    return Product.objects.create(
        name=" Product Name ",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" "
    )


@pytest.mark.django_db
def test_product_creation():
    p = create_product()
    assert isinstance(p, Product) is True
    assert p.name == " Product Name "


# @pytest.mark.django_db
# def test_get_product():
#     p = create_product()
#     get_product = Product.objects.get(id=p.id)
#     # get_product=Product.objects.get(p.name)
#     # p.name="New Name"
#     # p.save()
#     # assert p.name=="New Name"


# @pytest.mark.django_db
# def test_product_updating():
#     p = create_product()
#     p.name = "new_product"
#     p.save()
#     assert p
