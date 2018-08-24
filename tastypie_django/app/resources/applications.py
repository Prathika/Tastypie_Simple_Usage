from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from app.models import Applications
from .app_users import AppUsersResource

class ApplicationsResource(ModelResource):
    created_by = fields.ForeignKey('app.resources.AppUsersResource', 'created_by')
    updated_by = fields.ForeignKey('app.resources.AppUsersResource','updated_by', null=True)
    class Meta:
        queryset = Applications.objects.all()
        resource_name = 'applications'
        detailed_resource_uri = 'app_id'
        detail_uri_name = 'app_id'
        include_resource_uri = False
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = Authentication()
