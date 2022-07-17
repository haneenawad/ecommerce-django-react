import pytest
from django.contrib import auth
from django.contrib.auth import user_logged_in, user_logged_out
from django.template.context_processors import request
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import Product


'''
Unit tests -> checking user creation func
'''


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.com', 'test')  # username,email,password
    count = User.objects.all().count()
    assert count == 1


@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")


@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True


@pytest.mark.django_db
def test_get_user_by_Id():
    user_created = User.objects.create_user('test', 'test@test.com', 'test')  # username,email,password
    get_user = User.objects.get(id=user_created.id)
    assert get_user.id == user_created.id


@pytest.mark.django_db
def test_update_user_email():
    user_created = User.objects.create_user('test1', 'test1@test.com', 'test1')  # username,email,password
    get_user = User.objects.get(id=user_created.id)
    get_user.email = 'test2@test.com'
    get_user.save()
    updated_user = User.objects.get(id=user_created.id)
    assert updated_user.email == "test2@test.com"


@pytest.mark.django_db
def test_update_user_username():  # Don't update the username!!!! (solve : replace username by first_name)
    user_created = User.objects.create_user(username='test1', email='test1@test.com', password='test1')  # username,email,password
    get_user = User.objects.get(id=user_created.id)
    get_user.first_name = 'test2'
    get_user.save()
    print(get_user.first_name)
    updated_user = User.objects.get(id=get_user.id)
    print(updated_user.first_name)
    assert updated_user.first_name == "test2"

@pytest.mark.django_db
def test_delete_user(user_1):
    # user_created = User.objects.create_user('test3', 'test3@test.com', 'test3')  # username,email,password
    get_user = User.objects.get(id=user_1.id)
    get_user.delete()
    count = User.objects.all().count()
    assert count == 0



# @pytest.mark.django_db
# def test_user_logout():
#     User.objects.create_user('test', 'test@test.com', 'test')  # username,email,password
#     auth.logout(request)
#     assert user_1.is_active == False


'''
Unit tests -> checking superuser creation func
'''


@pytest.mark.django_db
def test_superuser_create():
    User.objects.create_superuser('super', 'super@test.com', 'super')  # username,email,password
    count = User.objects.all().count()
    assert count == 1


@pytest.fixture()
def user_2(db):
    return User.objects.create_superuser("test-superuser")


@pytest.mark.django_db
def test_set_check_password(user_2):
    user_2.set_password("new-password")
    assert user_2.check_password("new-password") is True

