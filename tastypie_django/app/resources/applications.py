from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from app.models import Applications
from .app_users import AppUsersResource

class ApplicationsResource(ModelResource):
    #associated_by = fields.ForeignKey(UsersResource, attribute='associated_by', null=True)
    created_by = fields.ToOneField(AppUsersResource,\
    attribute = 'created_by', related_name='created_by',  null=True)
    updated_by = fields.ToOneField(AppUsersResource, \
    attribute = 'updated_by', related_name='updated_by',  null=True)
    class Meta:
        queryset = Applications.objects.all()
        resource_name = 'applications'
        detailed_resource_uri = 'app_id'
        detail_uri_name = 'app_id'
        include_resource_uri = False
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = Authentication()

