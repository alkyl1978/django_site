# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'user_list', UserList)
router.register(r'post_list', PostList)

urlpatterns = router.urls
