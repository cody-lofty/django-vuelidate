import importlib
import inspect

from django.apps import apps
from django.core.management.base import BaseCommand
from django.forms import Form


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app_name')
        parser.add_argument('--models', action='store_true', help='Generate validation rules from models.')
        parser.add_argument('--forms', action='store_true', help='Generate validation rules from forms.')
        parser.add_argument('--serializers', action='store_true', help='Generate validation rules from serializers.')

    def handle(self, *args, **options):
        app_name = options['app_name']

        try:
            app = apps.get_app_config(app_name)
        except LookupError:
            self.stderr.write(self.style.ERROR('App `{}` not found.'.format(app_name)))
            return

        generate_all = not options['models'] and not options['forms'] and not options['serializers']
        if generate_all or options['models']:
            self.stdout.write('Generating validation rules from models...')
            if not app.models:
                self.stdout.write('No models registered.')
            for model in app.models:
                # TODO: generate_from_model(model)
                pass
        if generate_all or options['forms']:
            self.stdout.write('Generating validation rules from forms...')
            try:
                app_forms_module = importlib.import_module('{}.forms'.format(app_name))
                app_forms = inspect.getmembers(app_forms_module, lambda a : inspect.isclass(a) and issubclass(a, Form))
                for form in app_forms:
                    # TODO: generate_from_form(form)
                    pass
            except ModuleNotFoundError:
                self.stdout.write('No form module found.')
        if generate_all or options['serializers']:
            try:
                from rest_framework.serializers import Serializer
            except ImportError:
                self.stdout.write(self.style.ERROR('Error importing rest_framework, skipping serializers...'))
            else:
                self.stdout.write('Generating validation rules from serializers...')
                try:
                    app_serializers_module = importlib.import_module('{}.serializers'.format(app_name))
                    app_serializers = inspect.getmembers(app_serializers_module, lambda a : inspect.isclass(a) and issubclass(a, Serializer))
                    for serializer in app_serializers:
                        # TODO: generate_from_serializer(serializer)
                        pass
                except ModuleNotFoundError:
                    self.stdout.write('No serializer module found.')
