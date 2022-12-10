from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--all', action='store_true', help='Generate validation rules from models.')
        parser.add_argument('--models', action='store_true', help='Generate validation rules from models.')
        parser.add_argument('--forms', action='store_true', help='Generate validation rules from forms.')
        parser.add_argument('--serializers', action='store_true', help='Generate validation rules from serializers.')

    def handle(self, *args, **kwargs):
        # TODO: require at least one argument
        if kwargs['all'] or kwargs['models']:
            self.stdout.write('Generating validation rules from models...')
            # TODO: generate_from_models()
        if kwargs['all'] or kwargs['forms']:
            self.stdout.write('Generating validation rules from forms...')
            # TODO: generate_from_forms()
        if kwargs['all'] or kwargs['serializers']:
            try:
                from rest_framework import __version__
            except ImportError:
                self.stdout.write(self.style.ERROR('Error importing rest_framework, skipping serializers...'))
            else:
                self.stdout.write('Generating validation rules from serializers...')
                # TODO: generate_from_serializers()
