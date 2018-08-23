from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from app.models import AppUsers

class AppUsersResource(ModelResource):
    class Meta:
        queryset = AppUsers.objects.all()
        resource_name = 'app_users'
        detailed_resource_uri = 'user_id'
        detail_uri_name = 'user_id'
        include_resource_uri = False
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = Authentication()

