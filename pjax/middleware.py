# -*- coding: utf-8 -*-

import logging

from .base import PJAX_BASE_TEMPLATE, BASE_TEMPLATE


logger = logging.getLogger(__name__)


class PjaxMiddleware(object):
    def process_template_response(self, request, response):
        if request.META.get('HTTP_X_PJAX', False):
            logger.debug('pjax response')
            response.context_data['base'] = PJAX_BASE_TEMPLATE
        else:
            logger.debug('full response')
            response.context_data['base'] = BASE_TEMPLATE
        return response