from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def base_view(request):
    """ Homepage view """
    logger.info('User {} called view {}.base_view'.format(request.user, __name__))

    return render(request, 'base.html', {'test': 'IT WORKS!'})
