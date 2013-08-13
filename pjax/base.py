# -*- coding: utf-8 -*-

from django.conf import settings


PJAX_BASE_TEMPLATE = getattr(settings, 'PJAX_BASE_TEMPLATE', 'pjax_base.html')
BASE_TEMPLATE = getattr(settings, 'BASE_TEMPLATE', 'base.html')

