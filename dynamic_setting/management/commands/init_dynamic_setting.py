import logging

from django.core.management import BaseCommand

from ...helpers import init_setting_if_not_exist

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        init_setting_if_not_exist()
