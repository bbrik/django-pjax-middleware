# -*- coding: utf-8 -*-

import logging

from .base import PJAX_BASE_TEMPLATE, BASE_TEMPLATE, PJAX_VERSION


logger = logging.getLogger(__name__)


class PjaxMiddleware(object):
    def process_template_response(self, request, response):
        if request.META.get('HTTP_X_PJAX', False):
            logger.debug('pjax response')
            response.context_data['base'] = PJAX_BASE_TEMPLATE
            # fix redirect problem
            url = '%s?%s' % (request.path, request.META['QUERY_STRING'])
            response['X-PJAX-URL'] = url
            # set version
            if PJAX_VERSION:
                response['X-PJAX-Version'] = PJAX_VERSION
        else:
            logger.debug('full response')
            response.context_data['base'] = BASE_TEMPLATE
        return response