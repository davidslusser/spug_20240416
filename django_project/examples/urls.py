from django.urls import path
from examples import views

app_name = "examples"


urlpatterns = [
    path("", views.Index.as_view(), name="index"),

    path("example_one/", views.ExampleOne.as_view(), name="example_one"),
    path("example_two/", views.ExampleTwo.as_view(), name="example_two"),
    path('example_three/', views.ExampleThree, name='example_three'),
    path('example_four/', views.ExampleFour, name='example_four'),
    
    # htmx get partials
    path("get_joke/", views.get_joke, name="get_joke"),
    path("get_time/", views.get_time, name="get_time"),
]
