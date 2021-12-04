"""ran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from testapp import views
import testapp
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('emp',views.EmpViewset,basename='emp')

urlpatterns = [

    path('',include(router.urls)),
    # path('emp/',views.emplist ),
    # path('emp/',views.empApiView.as_view()),
    # path('emp/',views.GenApiView.as_view()),
    # path('emp/<int:pk>/',views.emp_det ),
    # path('emp/<int:id>/',views.empdet.as_view() ),
    # path('emp/<int:id>/',views.GenApiView.as_view() ),
]
