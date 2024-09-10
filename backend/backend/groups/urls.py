from django.urls import path

from groups.views import GroupListView, AddGroupView, DeleteGroupView, GetGroupView

urlpatterns = [
    path("", GroupListView.as_view(), name="group_list"),
    path("/add", AddGroupView.as_view(), name="group_add"),
    path("/delete/<int:pk>", DeleteGroupView.as_view(), name="group_delete"),
    path("/<int:pk>", GetGroupView.as_view(), name="group_get"),
]