# django-vuelidate

Generate vuelidate validation rules from Django models, forms, and serializers.

## Usage

Add `django_vuelidate` to your INSTALLED_APPS.
Run `python manage.py vuelidate`.

## Contributing

`poetry install`
`poetry run shell`
`ln -s $(pwd)/django_vuelidate/ $(pwd)/testproject/django_vuelidate`
`cd testproject && python manage.py vuelidate`
