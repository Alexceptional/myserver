from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def base_view(request):
    """ Homepage view """
    logger.info('Rendering base view/home...')
    return render(request, 'base.html', {'test': 'IT WORKS!'})
