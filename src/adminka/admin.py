from sqladmin import ModelView

from src.models import Users, Projects, Credentials


class UserAdmin(ModelView, model=Users):
    name = 'User'
    name_plural = 'Users'
    icon = 'fa-solid fa-user'

    column_list = [
        Users.user_id,
        Users.name,
        Users.email,
        Users.is_active,
        Users.created_at,
    ]
    form_excluded_columns = [Users.created_at]
    column_sortable_list = [Users.user_id, Users.is_active, Users.created_at]
    column_details_list = [Users.user_id, Users.is_active, Users.email, Users.name, Users.created_at]


class ProjectAdmin(ModelView, model=Projects):
    name = 'Project'
    name_plural = 'Projects'
    icon = 'fa fa-book'

    column_list = [
        Projects.project_id,
        Projects.name,
        Projects.description,
        Projects.created_at,
    ]
    form_excluded_columns = [Projects.created_at]
    column_sortable_list = [Projects.project_id, Projects.created_at]
    column_details_list = [Projects.project_id, Projects.name, Projects.description, Projects.created_at]


class CredentialsAdmin(ModelView, model=Credentials):
    name = 'Credential'
    name_plural = 'Credentials'
    icon = 'fa fa-key'

    form_excluded_columns = [Credentials.created_at]
    column_list = [Credentials.credential_id, Credentials.name, Credentials.is_active, Credentials.created_at]
    column_sortable_list = [Credentials.credential_id, Credentials.is_active, Credentials.created_at]
    column_details_list = [Credentials.credential_id, Credentials.name, Credentials.is_active, Credentials.created_at]
