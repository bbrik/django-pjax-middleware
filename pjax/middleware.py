# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from .base import PJAX_BASE_TEMPLATE, BASE_TEMPLATE


class PjaxMiddleware(object):
    def process_template_response(self, request, response):
        if request.META.get('HTTP_X_PJAX', False):
            response.context_data['base'] = PJAX_BASE_TEMPLATE
        else:
            response.context_data['base'] = BASE_TEMPLATE
        return response